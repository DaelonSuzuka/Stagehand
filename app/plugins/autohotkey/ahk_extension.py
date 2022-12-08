from stagehand.sandbox import SandboxExtension
from ahk.daemon import AHK
from pathlib import Path
import sys


class AutohotkeyExtension(SandboxExtension):
    name = ['autohotkey', 'ahk']

    def __init__(self):
        # for future vendored packages
        # exe_path = (Path(ahk.__file__).parent / 'packages/Scripts/AutoHotkey.exe').as_posix()
        # self._ahk = AHK(executable_path=exe_path)

        exe_path = (Path(sys.executable).parent / 'AutoHotkey.exe').as_posix()
        self._ahk = AHK(executable_path=exe_path)

    def __getattr__(self, name):
        return getattr(self._ahk, name)
