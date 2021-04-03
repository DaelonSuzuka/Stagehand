from flask import Flask, render_template_string
from urllib.parse import urlparse
from qtstrap import *
from qtpy.QtWebSockets import *
from qtpy.QtNetwork import *
from codex import SubscriptionManager
import threading
from obs import ActionWidget
import socket
from .web_template import web_template


# disable flask logging
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def start_flask():
    app = Flask(__name__)

    @app.route("/")
    def nothing():
        return render_template_string(web_template)

    app.run(host='0.0.0.0', debug=True, use_reloader=False)


def get_ip():
    # this is a dirty hack to get our current machine's IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


@SubscriptionManager.subscribe
class WebInterfaceManager(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.server = QWebSocketServer('flask', QWebSocketServer.NonSecureMode)
        self.server.newConnection.connect(self.on_new_connection)
        self.clients = []

        if self.server.listen(address=QHostAddress.Any, port=5001):
            print(f"Device server listening at: {self.server.serverAddress().toString()}:{str(self.server.serverPort())}")
        else:
            print('Failed to start device server.')

        self.flask = threading.Thread(name='Web App', target=start_flask, daemon=True)
        self.flask.start()

        self.local_link = LinkLabel(both='http://localhost:5000')
        self.lan_link = LinkLabel(both=f'http://{get_ip()}:5000')

        self.actions = {i: ActionWidget(f'Web Action {i}', self.rename_buttons) for i in range(1, 13)}

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
            
            for _, action in self.actions.items():
                layout.add(action)

            layout.add(QLabel(), 1)

    def rename_buttons(self):
        for client in self.clients:
            for i, action in self.actions.items():
                client.sendTextMessage(f'{{"command":"rename", "number":"{i}", "name":"{action.label.text()}"}}')

    def on_new_connection(self):
        socket = self.server.nextPendingConnection()
        self.clients.append(socket)
        
        socket.textMessageReceived.connect(self.processTextMessage)
        self.rename_buttons()

    def processTextMessage(self, message):
        if int(message) in self.actions:
            self.actions[int(message)].run()