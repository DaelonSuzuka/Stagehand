from qtstrap.extras.command_palette import Command
from stagehand.sandbox import SandboxExtension
from stagehand.main_window import MainWindow
from .saleae_connection import SaleaeConnection


class SaleaeExtension(SandboxExtension):
    name = 'saleae'

    def __init__(self):
        super().__init__()
        self.connection = SaleaeConnection()

        self.commands = [Command('Saleae: Open Settings', triggered=self._open_settings)]

    def _open_settings(self):
        MainWindow().tabs.create_page('Saleae Settings')
