"""Keyboard and Mouse services for the Roadie engine.

These replace KeyboardExtension and MouseExtension as direct Service
subclasses, accessible from JS as stagehand.keyboard.tap('a'),
stagehand.mouse.click('left'), etc.
"""

from __future__ import annotations

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

from stagehand.roadie import Service


class KeyboardService(Service):
    """Provides keyboard simulation to JS action code.

    JS usage:
        stagehand.keyboard.tap('a')
        stagehand.keyboard.press('ctrl')
        stagehand.keyboard.release('ctrl')
        stagehand.keyboard.type('hello world')
    """

    name = ['keyboard', 'kb']

    def __init__(self):
        self.controller = KeyboardController()

    def tap(self, key: str) -> None:
        """Press and release a key."""
        self.controller.press(key)
        self.controller.release(key)

    def press(self, key: str) -> None:
        """Press a key down (hold)."""
        self.controller.press(key)

    def release(self, key: str) -> None:
        """Release a held key."""
        self.controller.release(key)

    def type(self, string: str) -> None:
        """Type a string character by character."""
        self.controller.type(string)


class MouseService(Service):
    """Provides mouse simulation to JS action code.

    JS usage:
        stagehand.mouse.click('left')
        stagehand.mouse.position(100, 200)
        stagehand.mouse.move(10, -5)
        stagehand.mouse.scroll('down', 3)
    """

    name = 'mouse'

    def __init__(self):
        self.controller = MouseController()

    def position(self, x: int, y: int) -> None:
        """Move mouse to absolute position."""
        self.controller.position = (x, y)

    def move(self, dx: int, dy: int) -> None:
        """Move mouse by relative offset."""
        self.controller.move(dx, dy)

    def scroll(self, direction: str, steps: int) -> None:
        """Scroll the mouse wheel."""
        self.controller.scroll(int(direction) if direction.lstrip('-').isdigit() else 0, int(steps))

    def click(self, button: str, times: int = 1) -> None:
        """Click a mouse button."""
        btn = self._resolve_button(button)
        self.controller.click(btn, int(times))

    def press(self, button: str) -> None:
        """Press (hold) a mouse button."""
        self.controller.press(self._resolve_button(button))

    def release(self, button: str) -> None:
        """Release a held mouse button."""
        self.controller.release(self._resolve_button(button))

    def _resolve_button(self, button: str):
        """Resolve a button name string to a pynput Button enum value."""
        button_map = {
            'left': Button.left,
            'right': Button.right,
            'middle': Button.middle,
        }
        return button_map.get(button, Button.left)