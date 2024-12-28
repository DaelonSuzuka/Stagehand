from qtstrap import *
from qtpy.QtWebSockets import *
from qtpy.QtNetwork import *
import threading
from stagehand.actions import CompactActionWidget, ActionWidget, ActionWidgetGroup
from stagehand.components import StagehandPage
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
    message_received = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clients = []

        self.server = QWebSocketServer('stagehand_web_control', QWebSocketServer.NonSecureMode)
        self.server.listen(address=QHostAddress.Any, port=5001)

        # if self.server.listen(address=QHostAddress.Any, port=5001):
        #     print(f"Device server listening at: {self.server.serverAddress().toString()}:{str(self.server.serverPort())}")
        # else:
        #     print('Failed to start device server.')

        self.server.newConnection.connect(self.on_new_connection)

    def on_new_connection(self):
        socket = self.server.nextPendingConnection()
        self.clients.append(socket)
        socket.textMessageReceived.connect(self.message_received.emit)
        self.new_connection.emit()


class WebInterfacePage(StagehandPage):
    page_type = 'Web Actions'
    changed = Signal()

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name
        self.icon_name = 'mdi.web'

        self.label = LabelEdit(f'Page {name}', changed=self.changed)

        self.socket = SocketListener()
        self.socket.new_connection.connect(self.rename_buttons)
        self.socket.message_received.connect(self.processTextMessage)

        self.httpd = None
        self.httpd_thread = None

        self.local_link = LinkLabel(both='')
        self.lan_link = LinkLabel(both='')

        self.port = QLineEdit('5000')
        self.port.textChanged.connect(self.port_changed)
        self.port.setValidator(QIntValidator())
        self.port.setPlaceholderText('default: 5000')

        self.autostart = QCheckBox()
        self.autostart.stateChanged.connect(lambda _: self.changed.emit())
        self.start = QPushButton('Start Server', clicked=self.start_thread)
        self.stop = QPushButton('Stop Server', clicked=self.stop_thread)
        self.stop.hide()

        self.group = ActionWidgetGroup(name, changed=self.on_change, parent=self, autosave=False)

        self.actions = {}
        self.actions_container = CVBoxLayout()

        self.enabled = AnimatedToggle()
        self.enabled.stateChanged.connect(lambda _: self.changed.emit())

        if changed:
            self.changed.connect(changed)

        if data is not None:
            self.set_data(data)

        if not self.port.text():
            self.start.setEnabled(False)
        else:
            if self.autostart.isChecked():
                self.start_thread()

        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(margins=0):
                layout.add(QWidget())
                layout.add(self.label)
                layout.add(QLabel(), 1)
                layout.add(self.enabled)
                layout.add(self.group.filter)
                layout.add(QWidget())
            with layout.hbox(margins=0):
                layout.add(QWidget())
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

            with layout.scroll(margins=0):
                layout.setStretchFactor(layout._layout, 1)
                layout.add(self.actions_container)
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
        self.changed.emit()

    def rename_buttons(self):
        for client in self.socket.clients:
            for i, action in self.actions.items():
                client.sendTextMessage(
                    f'{{"command":"rename", "number":"{i[len("Web Action "):]}", "name":"{action.label.text()}"}}'
                )

    def processTextMessage(self, text):
        try:
            msg = json.loads(text)
            if msg.get('command', '') == 'click':
                btn_name = f"Web Action {msg['button']}"
                if btn_name in self.actions:
                    self.actions[btn_name].run()
        except json.JSONDecodeError:
            pass

    def get_name(self):
        return self.label.text()

    def on_change(self):
        self.changed.emit()

    def set_data(self, data):
        self.data = data
        self.group.set_data(self.data)

        self.label.setText(data.get('name', self.name))

        self.port.setText(str(data.get('port', '5000')))
        self.autostart.setChecked(data.get('autostart', False))
        self.enabled.setChecked(data.get('enabled', True))

        if actions := data.get('actions'):
            for action_data in actions:
                action = CompactActionWidget(action_data['name'], group=self.group)
                action.set_data(action_data)
                self.actions[action.name] = action
                self.actions_container.add(action)
        else:
            self.actions = {}
            for i in range(1, 13):
                name = f'Web Action {i}'
                action = CompactActionWidget(name=name, group=self.group, changed=self.rename_buttons)
                self.actions[name] = action
                action.set_data(
                    {
                        **CompactActionWidget.default_data,
                        'name': name,
                    }
                )

            self.actions_container.add(list(self.actions.values()))

    def get_data(self):
        return {
            'page_type': self.page_type,
            'name': self.label.text(),
            'port': self.port.text(),
            'autostart': self.autostart.isChecked(),
            'enabled': self.enabled.isChecked(),
            **self.group.get_data(),
        }
