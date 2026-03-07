"""
Simple HTTP test server for testing HTTP actions and extensions.

Run with: uv run python -m stagehand.utils.http_test_server
Or programmatically:
    from stagehand.utils.http_test_server import HttpTestServer
    server = HttpTestServer()
    server.start()
    # ... make requests to http://localhost:8080/...
    server.stop()
"""

import json
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import time


class HttpTestHandler(BaseHTTPRequestHandler):
    """Handler for test HTTP requests with various endpoints."""
    
    # Store received requests for verification in tests
    requests_log: list = []
    
    def log_message(self, format, *args):
        """Log each incoming request."""
        method = self.command if hasattr(self, 'command') else '?'
        path = self.path if hasattr(self, 'path') else '?'
        print(f"[HTTP] {method} {path}")
    
    def _send_json_response(self, data: dict, status: int = 200):
        """Send a JSON response."""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        print(f"[HTTP] <- {status} {json.dumps(data)[:200]}")
    
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
    
    def _log_request(self, method: str, body: dict = None):
        """Log the request for test verification."""
        self.requests_log.append({
            'method': method,
            'path': self.path,
            'headers': dict(self.headers),
            'body': body,
            'timestamp': time.time(),
        })
    
    # Echo endpoint - returns request details
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)
        
        if path == '/':
            self._send_json_response({
                'message': 'HTTP Test Server',
                'endpoints': {
                    'GET /': 'This help message',
                    'GET /echo': 'Echo request details (supports ?param=value)',
                    'GET /status/200': 'Return 200 OK',
                    'GET /status/404': 'Return 404 Not Found',
                    'GET /status/500': 'Return 500 Internal Server Error',
                    'POST /echo': 'Echo POST body',
                    'PUT /echo': 'Echo PUT body',
                    'PATCH /echo': 'Echo PATCH body',
                    'DELETE /echo': 'Echo DELETE with info',
                    'GET /slow': 'Slow response (1 second delay)',
                    'GET /json': 'Return sample JSON',
                    'GET /count': 'Return request count',
                    'GET /requests': 'Return all logged requests',
                    'DELETE /requests': 'Clear request log',
                }
            })
        
        elif path == '/echo':
            self._log_request('GET')
            self._send_json_response({
                'method': 'GET',
                'path': path,
                'query': query,
            })
        
        elif path.startswith('/status/'):
            try:
                code = int(path.split('/')[-1])
                self.send_response(code)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': code}).encode())
            except ValueError:
                self._send_json_response({'error': 'Invalid status code'}, 400)
        
        elif path == '/slow':
            time.sleep(1)
            self._send_json_response({'message': 'Delayed response'})
        
        elif path == '/json':
            self._send_json_response({
                'name': 'Stagehand',
                'version': '1.0',
                'features': ['http', 'actions', 'plugins'],
                'nested': {
                    'key': 'value',
                    'number': 42,
                }
            })
        
        elif path == '/count':
            self._send_json_response({'count': len(self.requests_log)})
        
        elif path == '/requests':
            self._send_json_response({'requests': self.requests_log[-100:]})
        
        else:
            self._send_json_response({'error': 'Not found'}, 404)
    
    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        body = self._get_request_body()
        self._log_request('POST', body)
        
        if path == '/echo':
            self._send_json_response({
                'method': 'POST',
                'path': path,
                'body': body,
            })
        elif path == '/requests/clear':
            self.requests_log.clear()
            self._send_json_response({'message': 'Request log cleared'})
        else:
            self._send_json_response({'error': 'Not found'}, 404)
    
    def do_PUT(self):
        body = self._get_request_body()
        self._log_request('PUT', body)
        
        if urlparse(self.path).path == '/echo':
            self._send_json_response({
                'method': 'PUT',
                'path': self.path,
                'body': body,
            })
        else:
            self._send_json_response({'error': 'Not found'}, 404)
    
    def do_PATCH(self):
        body = self._get_request_body()
        self._log_request('PATCH', body)
        
        if urlparse(self.path).path == '/echo':
            self._send_json_response({
                'method': 'PATCH',
                'path': self.path,
                'body': body,
            })
        else:
            self._send_json_response({'error': 'Not found'}, 404)
    
    def do_DELETE(self):
        self._log_request('DELETE')
        
        path = urlparse(self.path).path
        
        if path == '/requests':
            self.requests_log.clear()
            self._send_json_response({'message': 'Request log cleared'})
        elif path == '/echo':
            self._send_json_response({
                'method': 'DELETE',
                'path': path,
                'headers': dict(self.headers),
            })
        else:
            self._send_json_response({'error': 'Not found'}, 404)


class HttpTestServer:
    """Manage a test HTTP server."""
    
    def __init__(self, port: int = 8080):
        self.port = port
        self.server: HTTPServer = None
        self.thread: threading.Thread = None
    
    def start(self):
        """Start the server in a background thread."""
        if self.server is not None:
            return
        
        HttpTestHandler.requests_log = []
        self.server = HTTPServer(('localhost', self.port), HttpTestHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
    
    def stop(self):
        """Stop the server."""
        if self.server is not None:
            self.server.shutdown()
            self.server = None
            self.thread = None
    
    def get_requests(self) -> list:
        """Get all logged requests."""
        return HttpTestHandler.requests_log.copy()
    
    def clear_requests(self):
        """Clear the request log."""
        HttpTestHandler.requests_log.clear()
    
    @property
    def url(self) -> str:
        """Get the server URL."""
        return f'http://localhost:{self.port}'


if __name__ == '__main__':
    print('Starting HTTP test server on http://localhost:8080')
    print('Press Ctrl+C to stop')
    
    server = HttpTestServer()
    server.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nStopping server...')
        server.stop()
        print('Server stopped')