from qtstrap import *
from stagehand.components import StagehandPage, SingletonPageMixin


class SaleaeSettingsPage(SingletonPageMixin, StagehandPage):
    page_type = 'Saleae Settings'

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name

        if data is not None:
            self.set_data(data)

        self.serial_number = QLineEdit()
        self.port = QLineEdit()
        
        with CVBoxLayout(self) as layout:
            with layout.form():
                layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
                layout.addRow('Serial Number:', self.serial_number)
                layout.addRow('Port:', self.port)
