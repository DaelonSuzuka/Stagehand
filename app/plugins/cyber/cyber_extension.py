from stagehand.sandbox import Sandbox, SandboxExtension
from cyber import CyberVM


class CyberExtension(SandboxExtension):
    name = 'cyber'

    def __init__(self):
        self.vm = CyberVM()

        @self.vm.module('core')
        class Core:
            def print(self, string: str):
                Sandbox().tools.print(string)

        @self.vm.module
        class Stagehand:
            """Cyber module for Stagehand API"""
            pass


    def eval(self, string):
        self.vm.eval(string)
