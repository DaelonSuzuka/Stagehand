from qtstrap import *
from qtstrap.extras.code_editor import CodeLine
import qtawesome as qta
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionItem
import json


class HttpAction(ActionItem):
    name = 'http'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.changed = changed

        self.method = QComboBox()
        self.method.addItems(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
        self.method.currentIndexChanged.connect(changed)

        self.url = QLineEdit()
        self.url.setPlaceholderText('https://api.example.com/endpoint')
        self.url.textChanged.connect(changed)

        self.body = QLineEdit()
        self.body.setPlaceholderText('{"key": "value"}')
        self.body.textChanged.connect(changed)
        self.body.setVisible(False)

        self.method.currentTextChanged.connect(self._update_body_visibility)
        self._update_body_visibility(self.method.currentText())

        self.edit_btn = QPushButton('', clicked=self._open_editor, icon=qta.icon('fa5.edit'))
        self.edit_btn.setIconSize(QSize(22, 22))

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.method)
            layout.add(self.url, 1)
            layout.add(self.body, 1)
            layout.add(self.edit_btn)

    def _update_body_visibility(self, method: str):
        """Show body field for methods that support request body."""
        self.body.setVisible(method in ('POST', 'PUT', 'PATCH'))

    def _open_editor(self):
        """Open the multiline editor dialog."""
        from .http_action_editor import HttpActionEditorDialog

        self.data['method'] = self.method.currentText()
        self.data['url'] = self.url.text()
        self.data['body'] = self.body.text()
        self.data['name'] = self.owner.name if self.owner else 'HTTP Action'

        self.editor = HttpActionEditorDialog(self.data, self.owner)
        self.editor.accepted.connect(self._on_accept)
        self.editor.open()

    def _on_accept(self):
        """Handle editor dialog acceptance."""
        self.method.setCurrentText(self.editor.method.currentText())
        self.url.setText(self.editor.url.text())
        self.body.setText(self.editor.body.toPlainText())
        if self.owner:
            self.owner.label.setText(self.editor.label.text())
        self.changed()

    def set_data(self, data: dict):
        self.data = data
        self.method.setCurrentText(data.get('method', 'GET'))
        self.url.setText(data.get('url', ''))
        self.body.setText(data.get('body', ''))
        self._update_body_visibility(self.method.currentText())

    def get_data(self) -> dict:
        return {
            'method': self.method.currentText(),
            'url': self.url.text(),
            'body': self.body.text(),
        }

    def reset(self):
        self.method.setCurrentText('GET')
        self.url.clear()
        self.body.clear()

    def run(self):
        """Execute the HTTP request."""
        method = self.method.currentText().lower()
        url = self.url.text()
        body_text = self.body.text()

        if not url:
            Sandbox().tools.print('HTTP Action: No URL specified')
            return

        # Build the sandbox code to execute
        # We inject print statements to show the result
        code = f'''
response = http.{method}("{url}"'''

        # Add body for methods that support it
        if body_text and method in ('post', 'put', 'patch'):
            try:
                # Validate JSON
                parsed = json.loads(body_text)
                # Use json= parameter for proper serialization
                code += f', json={repr(parsed)}'
            except json.JSONDecodeError:
                # Fall back to raw string if not valid JSON
                Sandbox().tools.print(f'HTTP Action: Invalid JSON body: {body_text}')
                return

        code += f''')
print(f"HTTP {method.upper()} {url}")
print(f"Status: {{response.status_code}}")
print(f"Response: {{response.text[:1000]}}")
'''

        Sandbox().run(code)