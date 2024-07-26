from stagehand.sandbox import SandboxExtension
from pathlib import Path
import sys

import ahk
from ahk import AHK
from ahk.window import Window


class AutohotkeyExtension(SandboxExtension):
    name = ['autohotkey', 'ahk']

    def __init__(self):
        # for future vendored packages
        # exe_path = (Path(ahk.__file__).parent / 'packages/Scripts/AutoHotkey.exe').as_posix()
        # self._ahk = AHK(executable_path=exe_path)

        exe_path = (Path(sys.executable).parent / 'AutoHotkey.exe').as_posix()
        self._ahk = AHK(executable_path=exe_path)

        self._namespace = {
            'Window': Window,
        }

    def __getattr__(self, name):
        if name in self._namespace:
            return self._namespace[name]

        if hasattr(ahk, name):
            return getattr(ahk, name)

        return getattr(self._ahk, name)
