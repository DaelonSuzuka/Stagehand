from stagehand.sandbox import SandboxExtension
from ahk.daemon import AHK, AHKDaemon


class AutohotkeyExtension(SandboxExtension):
    name = ['autohotkey', 'ahk']

    def __init__(self):
        self._ahk = AHK()

        self._daemon = AHKDaemon()
        self._daemon.start()

    def __getattr__(self, name):
        if name in ['run_script']:
            return getattr(self._ahk, name)

        return getattr(self._daemon, name)
