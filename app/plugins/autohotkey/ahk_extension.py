from stagehand.sandbox import SandboxExtension
from ahk.daemon import AHK, AHKDaemon

# for future vendored packages
# from .packages.ahk.daemon import AHK, AHKDaemon
# from pathlib import Path


class AutohotkeyExtension(SandboxExtension):
    name = ['autohotkey', 'ahk']

    def __init__(self):
        # for future vendored packages
        # exe_path = (Path(__file__).parent / 'packages/Scripts/AutoHotkey.exe').as_posix()
        # self._ahk = AHK(executable_path=exe_path)
        # self._daemon = AHKDaemon(executable_path=exe_path)

        self._ahk = AHK()
        self._daemon = AHKDaemon()
        self._daemon.start()

    def __getattr__(self, name):
        if name in ['run_script']:
            return getattr(self._ahk, name)

        return getattr(self._daemon, name)

    def close
