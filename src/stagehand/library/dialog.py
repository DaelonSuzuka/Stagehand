"""Dialog for saving items to the library."""

from qtstrap import *


class SaveToLibraryDialog(QDialog):
    """Dialog for naming and saving an item to the library.
    
    Shows a preview of the data being saved and asks for a name.
    """
    
    def __init__(self, category: str, data: dict, parent=None):
        super().__init__(parent=parent)
        
        self.category = category
        self.data = data
        self.result_name = None
        
        category_names = {
            'triggers': 'Trigger',
            'filters': 'Filter',
            'outputs': 'Output',
            'actions': 'Action',
        }
        
        self.setWindowTitle(f'Save {category_names.get(category, "Item")} to Library')
        self.setMinimumWidth(400)
        
        # Name input
        self.name_edit = QLineEdit()
        self.name_edit.setText(data.get('name', ''))
        self.name_edit.setPlaceholderText('Enter a name for this item')
        self.name_edit.selectAll()
        
        # Preview
        self.preview = QTextEdit()
        self.preview.setReadOnly(True)
        self.preview.setMaximumHeight(200)
        self.preview.setFont(QFont('monospace'))
        
        # Format preview text
        import json
        preview_data = {k: v for k, v in data.items() if not k.startswith('_')}
        self.preview.setPlainText(json.dumps(preview_data, indent=2))
        
        # Buttons
        self.save_btn = QPushButton('Save', clicked=self.accept)
        self.cancel_btn = QPushButton('Cancel', clicked=self.reject)
        
        # Layout
        with CVBoxLayout(self) as layout:
            layout.add(QLabel('Name:'))
            layout.add(self.name_edit)
            layout.addSpacing(10)
            layout.add(QLabel('Preview:'))
            layout.add(self.preview, 1)
            layout.addSpacing(10)
            with layout.hbox(align='right'):
                layout.add(self.cancel_btn)
                layout.add(self.save_btn)
        
        # Enable save button only when name is not empty
        self.name_edit.textChanged.connect(self.validate)
        self.save_btn.setEnabled(bool(self.name_edit.text()))
        
        # Focus name edit
        self.name_edit.setFocus()
    
    def validate(self):
        """Enable save button only when name is not empty."""
        self.save_btn.setEnabled(bool(self.name_edit.text().strip()))
    
    def accept(self):
        """Store the name and close."""
        self.result_name = self.name_edit.text().strip()
        super().accept()
    
    def get_name(self) -> str | None:
        """Return the entered name, or None if cancelled."""
        return self.result_name