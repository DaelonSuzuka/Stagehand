from qtstrap import *
from stagehand.components import SingletonPageMixin, StagehandPage
from .http_trigger import HttpServerManager


class HttpServerSettingsPage(SingletonPageMixin, StagehandPage):
    """Settings page for the HTTP trigger server."""
    
    page_type = 'HTTP Server Settings'
    
    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name
        
        if data is not None:
            self.set_data(data)
        
        self.manager = HttpServerManager()
        
        # Port setting
        self.port = QSpinBox()
        self.port.setRange(1, 65535)
        self.port.setValue(self.manager.settings.port)
        self.port.valueChanged.connect(self._on_port_changed)
        
        # Start/Stop buttons
        self.start_btn = QPushButton('Start', clicked=self._start_server)
        self.stop_btn = QPushButton('Stop', clicked=self._stop_server)
        self.stop_btn.setEnabled(False)
        
        # Status
        self.status_label = QLabel('Stopped')
        
        # Test endpoint info
        self.test_info = QLabel()
        self.test_info.setWordWrap(True)
        self.test_info.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        # Connect status updates
        self.manager.status_changed.connect(self._update_status)
        self._update_ui()
        
        with CVBoxLayout(self) as layout:
            with layout.form() as form:
                form.addRow('Port:', self.port)
                form.addRow('Status:', self.status_label)
                form.addRow('', self.start_btn)
                form.addRow('', self.stop_btn)
            
            layout.add(QLabel('Test Endpoint:'))
            layout.add(self.test_info)
            
            layout.add(QLabel())
            layout.add(QLabel('Usage:'), 0)
            info_text = '''
<p>Configure an action with an <b>HTTP trigger</b> to respond to HTTP requests.</p>
<p><b>Example trigger settings:</b></p>
<ul>
  <li>Method: POST</li>
  <li>Path: /webhook</li>
</ul>
<p>Then send a request to: <code>http://localhost:{port}/webhook</code></p>
'''
            layout.add(QLabel(info_text.format(port=self.port.value())))
    
    def _on_port_changed(self, value):
        """Handle port change."""
        self.manager.settings.port = value
        if self.manager.is_running:
            # Restart with new port
            self.manager.stop()
            self.manager.start()
        self._update_test_info()
    
    def _start_server(self):
        """Start the HTTP server."""
        self.manager.start(self.port.value())
    
    def _stop_server(self):
        """Stop the HTTP server."""
        self.manager.stop()
    
    def _update_status(self, status: str):
        """Update status display."""
        if status == 'active':
            self.status_label.setText(f'Running on port {self.manager.settings.port}')
            self.status_label.setStyleSheet('color: green;')
        elif status == 'inactive':
            self.status_label.setText('Stopped')
            self.status_label.setStyleSheet('color: gray;')
        elif status == 'error':
            self.status_label.setText('Error (port may be in use)')
            self.status_label.setStyleSheet('color: red;')
        self._update_ui()
    
    def _update_ui(self):
        """Update button states."""
        running = self.manager.is_running
        self.start_btn.setEnabled(not running)
        self.stop_btn.setEnabled(running)
        self.port.setEnabled(not running)
        self._update_test_info()
    
    def _update_test_info(self):
        """Update test endpoint info."""
        port = self.port.value()
        self.test_info.setText(f'<code>http://localhost:{port}/</code>')