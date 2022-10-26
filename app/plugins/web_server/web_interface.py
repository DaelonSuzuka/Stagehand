from qtstrap import *
from urllib.parse import urlparse
from qtpy.QtWebSockets import *
from qtpy.QtNetwork import *
import threading
from stagehand.actions import ActionWidget, ActionWidgetGroup
from stagehand.components import StagehandWidget
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


pages = {}

base_dir = Path(Path(__file__).parent / 'pages')

for f in base_dir.rglob('*'):
    rel = f.relative_to(base_dir)
    pages[rel.as_posix()] = f
    if rel.suffix == '.html':
        pages[rel.as_posix().removesuffix('.html')] = f


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # silence log messages
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        path = self.path.lstrip('/')
        if path == '':
            path = 'index.html'

        if path in pages:
            path = pages[path]
        else:
            path = pages['404']

        self.wfile.write(path.read_text().encode())


server_port = 5000
httpd = None


def start_server():
    global httpd
    httpd = HTTPServer(('', server_port), Handler)
    httpd.serve_forever()


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
        super().__init__(icon_name='mdi.web', parent=parent)

        self.socket = SocketListener()
        self.socket.new_connection.connect(self.rename_buttons)
        self.socket.message_recieved.connect(self.processTextMessage)

        self.httpd = None
        self.httpd_thread = None

        self.local_link = LinkLabel(both='')
        self.lan_link = LinkLabel(both='')

        self.port = PersistentLineEdit('web_server/port', default='5000', changed=self.port_changed)
        self.port.setValidator(QIntValidator())
        self.port.setPlaceholderText('default: 5000')

        self.autostart = PersistentCheckBox('web_server/autostart')
        self.start = QPushButton('Start Server', clicked=self.start_thread)
        self.stop = QPushButton('Stop Server', clicked=self.stop_thread)
        self.stop.hide()

        if not self.port.text():
            self.start.setEnabled(False)
            
        if self.autostart:
            self.start_thread()

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
                layout.add(QLabel('Autostart Server:'))
                layout.add(self.autostart)
                layout.add(QLabel('Port:'))
                layout.add(self.port)
                layout.add(self.start)
                layout.add(self.stop)
            layout.add(HLine())

            layout.add([a for _, a in self.actions.items()])
            layout.add(QLabel(), 1)

    def start_thread(self):
        self.httpd_thread = threading.Thread(name='Web App', target=start_server, daemon=True)
        self.httpd_thread.start()
        self.start.hide()
        self.stop.show()
        self.port.setEnabled(False)
        self.local_link.setBoth(f'http://localhost:{self.port.text()}')
        self.lan_link.setBoth(f'http://{get_ip()}:{self.port.text()}')

    def stop_thread(self):
        httpd.shutdown()
        self.start.show()
        self.stop.hide()
        self.port.setEnabled(True)
        self.local_link.setBoth('')
        self.lan_link.setBoth('')

    def port_changed(self, value):
        self.start.setEnabled(True)
        if not value:
            self.start.setEnabled(False)
            return
        global server_port
        server_port = int(value)

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