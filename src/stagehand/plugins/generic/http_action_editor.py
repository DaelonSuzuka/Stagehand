from qtstrap import *
from qtstrap.extras.code_editor import CodeEditor
import qtawesome as qta


class HttpActionEditorDialog(QDialog):
    """Editor dialog for HTTP actions with multiline JSON body support."""
    
    def __init__(self, data, owner=None):
        super().__init__()

        self.owner = owner
        self.data = data
        self.setWindowTitle('HTTP Action Editor')

        size: int = QSettings().value('font_size', 12)
        set_font_options(self, {'setPointSize': int(size)})

        self.geometry_setting = 'plugins/http/http_action_editor/geometry'

        geometry = QSettings().value(self.geometry_setting)
        if isinstance(geometry, QByteArray):
            self.restoreGeometry(geometry)

        self.finished.connect(lambda _: QSettings().setValue(self.geometry_setting, self.saveGeometry()))

        # Method selector
        self.method = QComboBox()
        self.method.addItems(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
        self.method.setCurrentText(data.get('method', 'GET'))
        self.method.currentTextChanged.connect(self._update_body_visibility)

        # URL input
        self.url = QLineEdit()
        self.url.setText(data.get('url', ''))
        self.url.setPlaceholderText('https://api.example.com/endpoint')

        # Request body editor (for POST/PUT/PATCH)
        self.body = CodeEditor()
        self.body.setPlainText(data.get('body', ''))
        self.body.setPlaceholderText('{"key": "value"}')

        self._update_body_visibility(self.method.currentText())

        # Name and label
        name = data.get('name', 'HTTP Action')
        label_text = owner.label.text() if owner else name

        self.label = QLineEdit(label_text)

        # Buttons
        self.reset_btn = QPushButton('Reset', clicked=self._on_reset)
        self.cancel_btn = QPushButton('Cancel', clicked=self.reject)
        self.ok_btn = QPushButton('Ok', clicked=self.accept)
        self.run_btn = QPushButton('', clicked=self._run)
        self.run_btn.setIcon(qta.icon('mdi.play-circle-outline'))

        # Layout
        with CVBoxLayout(self) as layout:
            with layout.hbox() as h:
                h.add(QLabel('Name:'))
                h.add(QLabel(name))
                h.add(QLabel(), 1)
                h.add(self.reset_btn)

            with layout.hbox(align='left') as h:
                h.add(QLabel('Label:'))
                h.add(self.label)
                h.add(QLabel(), 1)
                h.add(self.run_btn)

            with layout.hbox(align='left') as h:
                h.add(QLabel('Method:'))
                h.add(self.method)

            with layout.hbox(align='left') as h:
                h.add(QLabel('URL:'))
                h.add(self.url, 1)

            with layout.hbox(align='left') as h:
                h.add(QLabel('Body:'))

            layout.add(self.body)

            with layout.hbox(align='right') as h:
                h.add(self.cancel_btn)
                h.add(self.ok_btn)

    def _update_body_visibility(self, method: str):
        """Show/hide body field based on HTTP method."""
        self.body.setVisible(method in ('POST', 'PUT', 'PATCH'))

    def _run(self):
        """Test the HTTP request."""
        import httpx
        import json

        method = self.method.currentText().lower()
        url = self.url.text()
        body_text = self.body.toPlainText()

        if not url:
            return

        kwargs = {}
        if body_text and method in ('post', 'put', 'patch'):
            try:
                kwargs['json'] = json.loads(body_text)
            except json.JSONDecodeError:
                return

        try:
            with httpx.Client() as client:
                response = client.request(method.upper(), url, **kwargs)
                Sandbox().tools.print(f'HTTP {method.upper()} {url}')
                Sandbox().tools.print(f'Status: {response.status_code}')
                Sandbox().tools.print(f'Response: {response.text[:500]}')
        except Exception as e:
            Sandbox().tools.print(f'HTTP request failed: {e}')

    def _on_reset(self):
        """Reset the form."""
        self.url.clear()
        self.body.setPlainText('')
        self.method.setCurrentText('GET')
        self.label.setText(self.data.get('name', 'HTTP Action'))