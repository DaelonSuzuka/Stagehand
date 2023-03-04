from qtstrap import *
from stagehand.sandbox import Sandbox, SandboxExtension
from cyber import *


class CyberExtension(SandboxExtension):
    name = 'cyber'

    def __init__(self):
        self.vm = CyberVM()

        with self.vm.module('core') as module:
            @module('print', 1)
            def _print(vm, args, nargs):
                s = cyValueToTempString(vm, args[0])
                Sandbox().tools.print(s.charz.decode())
                return 0

    def eval(self, string):
        self.vm.eval(string)
