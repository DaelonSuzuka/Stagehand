from flask import Flask, render_template
from urllib.parse import urlparse
from qtstrap import *
from qtpy.QtWebSockets import *
from qtpy.QtNetwork import *
import threading
from stagehand.actions import ActionWidget, ActionWidgetGroup
from stagehand.components import StagehandWidget, SidebarButton
import socket
import json
import qtawesome as qta


# disable flask logging
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# disable flask console output
import click
def secho(text, file=None, nl=None, err=None, color=None, **styles):
    pass
def echo(text, file=None, nl=None, err=None, color=None, **styles):
    pass
click.echo = echo
click.secho = secho


def start_flask():
    template_path = Path(Path(__file__).parent / 'pages')
    static_path = Path(template_path / 'static').as_posix()
    app = Flask(__name__, template_folder=template_path, static_folder=static_path)

    @app.route("/")
    def home():
        return render_template('index.html')

    @app.route("/<page>")
    def others(page):
        if f'{page}.html' in [f.parts[-1] for f in template_path.rglob('*.html')]:
            return render_template(f'{page}.html')
        return render_template('404.html')

    app.run(host='0.0.0.0', debug=True, use_reloader=False)


def get_ip():
    # this is a dirty hack to get our current machine's IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

@singleton
class SocketListener(QObject):
    new_connection = Signal()
    message_recieved = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clients = []
        
        self.server = QWebSocketServer('flask', QWebSocketServer.NonSecureMode)
        self.server.listen(address=QHostAddress.Any, port=5001)
        
        # if self.server.listen(address=QHostAddress.Any, port=5001):
        #     print(f"Device server listening at: {self.server.serverAddress().toString()}:{str(self.server.serverPort())}")
        # else:
        #     print('Failed to start device server.')
        
        self.server.newConnection.connect(self.on_new_connection)

    def on_new_connection(self):
        socket = self.server.nextPendingConnection()
        self.clients.append(socket)
        socket.textMessageReceived.connect(self.message_recieved.emit)
        self.new_connection.emit()


class WebInterfaceManager(StagehandWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.sidebar_button = SidebarButton(target=self, icon=qta.icon('mdi.web'))

        self.socket = SocketListener()
        self.socket.new_connection.connect(self.rename_buttons)
        self.socket.message_recieved.connect(self.processTextMessage)

        self.flask = threading.Thread(name='Web App', target=start_flask, daemon=True)
        self.flask.start()
        
        self.sidebar_widget = QPushButton(iconSize=QSize(40, 40), icon=qta.icon('mdi.web'), flat=True)

        self.local_link = LinkLabel(both='http://localhost:5000')
        self.lan_link = LinkLabel(both=f'http://{get_ip()}:5000')

        self.group = ActionWidgetGroup(f'web_actions/actions', self)

        self.actions = {}
        for i in range(1, 13):
            name = f'Web Action {i}'
            self.actions[name] = ActionWidget(name, self.group, changed=self.rename_buttons)

        with CVBoxLayout(self) as layout:
            with layout.hbox():
                layout.add(QLabel('Local Link:'))
                layout.add(self.local_link)
                layout.add(QLabel())
                layout.add(QLabel('LAN Link:'))
                layout.add(self.lan_link)
                layout.add(QLabel(), 1)
            layout.add(QLabel())
            layout.add(HLine())

            layout.add([a for _, a in self.actions.items()])
            layout.add(QLabel(), 1)

    def rename_buttons(self):
        for client in self.socket.clients:
            for i, action in self.actions.items():
                client.sendTextMessage(f'{{"command":"rename", "number":"{i[len("Web Action "):]}", "name":"{action.label.text()}"}}')

    def processTextMessage(self, text):
        try:
            msg = json.loads(text)
            if 'command' in msg and msg['command'] == 'click':
                btn_name = f"Web Action {msg['button']}"
                if btn_name in self.actions:
                    self.actions[btn_name].run()
        except:
            pass