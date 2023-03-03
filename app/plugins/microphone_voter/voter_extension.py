from qtstrap import *
from qtstrap.extras.command_palette import Command
from stagehand.sandbox import SandboxExtension
from stagehand.main_window import MainWindow


class MicVoterExtension(SandboxExtension):
    name = 'voter'

    def __init__(self) -> None:
        super().__init__()

        self.commands = [
            Command('Open Microphone Voter', triggered=lambda: MainWindow().tabs.create_page('Microphone Voter'))
            #
        ]
