import sys
from pathlib import Path

sys.path.append(Path(__file__).parent)

from .packages.pynput.keyboard import Key, Controller
from .packages.pynput import mouse


class KeyboardExtension:
    def __init__(self):
        self.controller = Controller()

    def __getattr__(self, name):
        return getattr(Key, name)

    def tap(self, key):
        self.controller.press(key)
        self.controller.release(key)

    def press(self, key):
        self.controller.press(key)

    def release(self, key):
        self.controller.release(key)


class MouseExtension:
    def __init__(self):
        self.controller = mouse.Controller()

    def __getattr__(self, name):
        return getattr(mouse.Button, name)

    def position(self, x, y):
        self.controller.position(x, y)

    def move(self, x, y):
        self.controller.move(x, y)

    def scroll(self, direction, steps):
        self.controller.scroll(direction, steps)

    def click(self, button, times=1):
        self.controller.click(button, times)

    def press(self, button):
        self.controller.press(button)

    def release(self, button):
        self.controller.release(button)
