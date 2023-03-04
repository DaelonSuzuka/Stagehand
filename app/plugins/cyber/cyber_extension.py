from qtstrap import *
from stagehand.sandbox import Sandbox, SandboxExtension
from cyber import *


class CyberExtension(SandboxExtension):
    name = 'cyber'

    def __init__(self):
        self.vm = CyberVM()

        with self.vm.module('core') as module:
            @module.function('print')
            def _print(string: str):
                Sandbox().tools.print(string)

    def eval(self, string):
        self.vm.eval(string)
