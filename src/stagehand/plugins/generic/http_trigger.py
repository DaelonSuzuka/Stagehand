from qtstrap import *
from qtstrap.extras.command_palette import Command
from qtstrap.extras.settings_model import SettingsModel
from stagehand.components import StagehandStatusBarItem
from stagehand.main_window import MainWindow
from stagehand.actions import TriggerItem
import json
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class HttpServerSettings(SettingsModel):
    port: int = 8080
    enabled: bool = False

    class Config:
        prefix = 'plugins/http_server'


class HttpTriggerHandler(BaseHTTPRequestHandler):
    """Handler for incoming HTTP requests that trigger actions."""
    
    callbacks: list = []  # List of callback functions to call on request
    
    def log_message(self, format, *args):
        """Log each incoming request."""
        print(f"[HTTP Trigger] {args[0]}")
    
    def _send_json_response(self, data: dict, status: int = 200):
        """Send a JSON response."""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def _get_request_body(self) -> dict:
        """Parse JSON request body."""
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            return {}
        try:
            body = self.rfile.read(content_length)
            return json.loads(body.decode())
        except json.JSONDecodeError:
            return {}
    
    def _trigger_callbacks(self, method: str, path: str, query: dict, body: dict):
        """Call all registered callbacks with the request data."""
        request_data = {
            'method': method,
            'path': path,
            'query': query,
            'body': body,
            'headers': dict(self.headers),
        }
        for callback in self.callbacks:
            try:
                callback(request_data)
            except Exception as e:
                print(f"[HTTP Trigger] Callback error: {e}")
    
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)
        # Convert single-value lists to values
        query = {k: v[0] if len(v) == 1 else v for k, v in query.items()}
        
        self._trigger_callbacks('GET', path, query, {})
        self._send_json_response({'status': 'ok', 'method': 'GET', 'path': path})
    
    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        body = self._get_request_body()
        
        self._trigger_callbacks('POST', path, {}, body)
        self._send_json_response({'status': 'ok', 'method': 'POST', 'path': path})
    
    def do_PUT(self):
        parsed = urlparse(self.path)
        path = parsed.path
        body = self._get_request_body()
        
        self._trigger_callbacks('PUT', path, {}, body)
        self._send_json_response({'status': 'ok', 'method': 'PUT', 'path': path})
    
    def do_PATCH(self):
        parsed = urlparse(self.path)
        path = parsed.path
        body = self._get_request_body()
        
        self._trigger_callbacks('PATCH', path, {}, body)
        self._send_json_response({'status': 'ok', 'method': 'PATCH', 'path': path})
    
    def do_DELETE(self):
        parsed = urlparse(self.path)
        path = parsed.path
        
        self._trigger_callbacks('DELETE', path, {}, {})
        self._send_json_response({'status': 'ok', 'method': 'DELETE', 'path': path})
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


@singleton
class HttpServerManager(QObject):
    """Singleton manager for the HTTP trigger server."""
    
    request_received = Signal(dict)  # Emits request data
    status_changed = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.server: HTTPServer = None
        self.thread: threading.Thread = None
        self.settings = HttpServerSettings()
        self._running = False
    
    def start(self, port: int = None):
        """Start the HTTP server."""
        if self._running:
            return
        
        if port is None:
            port = self.settings.port
        
        try:
            HttpTriggerHandler.callbacks = [self._on_request]
            self.server = HTTPServer(('0.0.0.0', port), HttpTriggerHandler)
            self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self.thread.start()
            self._running = True
            self.settings.port = port
            self.settings.enabled = True
            self.status_changed.emit('active')
            print(f"[HTTP Trigger] Server started on port {port}")
        except OSError as e:
            print(f"[HTTP Trigger] Failed to start server: {e}")
            self.status_changed.emit('error')
    
    def stop(self):
        """Stop the HTTP server."""
        if self.server and self._running:
            self.server.shutdown()
            self.server = None
            self.thread = None
            self._running = False
            self.settings.enabled = False
            self.status_changed.emit('inactive')
            print("[HTTP Trigger] Server stopped")
    
    def _on_request(self, request_data: dict):
        """Handle incoming request."""
        self.request_received.emit(request_data)
    
    @property
    def is_running(self) -> bool:
        return self._running
    
    @property
    def url(self) -> str:
        return f"http://localhost:{self.settings.port}"


@singleton
class HttpServerStatusWidget(StagehandStatusBarItem):
    """Status bar widget for HTTP server status."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.manager = HttpServerManager()
        self.manager.status_changed.connect(self._update_status)
        
        self.status_label = QLabel('HTTP: Off')
        
        # Load settings
        if self.manager.settings.enabled:
            self.manager.start()
        
        self.commands = [
            Command('HTTP Server: Start', triggered=self._start_server),
            Command('HTTP Server: Stop', triggered=self._stop_server),
            Command('HTTP Server: Open Settings', triggered=self._open_settings),
        ]
        
        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.status_label)
            layout.add(QLabel())
    
    def _update_status(self, status: str):
        messages = {
            'active': f'HTTP:{self.manager.settings.port}',
            'inactive': 'HTTP: Off',
            'error': 'HTTP: Error',
        }
        self.status_label.setText(messages.get(status, 'HTTP: ?'))
    
    def _start_server(self):
        if not self.manager.is_running:
            self.manager.start()
    
    def _stop_server(self):
        self.manager.stop()
    
    def _open_settings(self):
        MainWindow().tabs.create_page('HTTP Server Settings')
    
    def contextMenuEvent(self, event):
        menu = QMenu()
        if self.manager.is_running:
            menu.addAction('Stop Server').triggered.connect(self._stop_server)
        else:
            menu.addAction('Start Server').triggered.connect(self._start_server)
        menu.addAction('Open Settings').triggered.connect(self._open_settings)
        menu.exec_(event.globalPos())


class HttpTrigger(TriggerItem):
    """HTTP trigger - fires when an HTTP request is received."""
    
    name = 'http'
    triggered = Signal()
    
    def __init__(self, changed, run, owner=None):
        super().__init__()
        
        self.owner = owner
        self._changed = changed
        self.triggered.connect(run)
        
        self.manager = HttpServerManager()
        self.manager.request_received.connect(self._on_request)
        
        # Filter settings
        self.path_filter = QLineEdit()
        self.path_filter.setPlaceholderText('/path (leave empty for any)')
        self.path_filter.textChanged.connect(changed)
        
        self.method = QComboBox()
        self.method.addItems(['ANY', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
        self.method.currentIndexChanged.connect(changed)
        
        with CHBoxLayout(self, margins=0) as layout:
            layout.add(QLabel('Method:'))
            layout.add(self.method)
            layout.add(QLabel('Path:'))
            layout.add(self.path_filter, 1)
    
    def _on_request(self, request_data: dict):
        """Called when an HTTP request is received."""
        # Check method filter
        method_filter = self.method.currentText()
        if method_filter != 'ANY' and request_data['method'] != method_filter:
            return
        
        # Check path filter
        path_filter = self.path_filter.text().strip()
        if path_filter and request_data['path'] != path_filter:
            return
        
        # Trigger the action
        self.triggered.emit()
    
    def set_data(self, data: dict):
        self.method.setCurrentText(data.get('method', 'ANY'))
        self.path_filter.setText(data.get('path', ''))
    
    def get_data(self) -> dict:
        return {
            'method': self.method.currentText(),
            'path': self.path_filter.text(),
        }