"""Keyboard and Mouse services for the Roadie engine.

These replace KeyboardExtension and MouseExtension as direct Service
subclasses, accessible from JS as stagehand.keyboard.tap('a'),
stagehand.mouse.click('left'), etc.

KeyboardService sends through one of two tiers:
    driver tier  — a uinput virtual device (Linux only). Events are
                   indistinguishable from hardware, so raw-input listeners
                   (games, TeamSpeak-style hotkey engines) receive them.
    session tier — pynput (SendInput / XTEST / CGEventPost). Portable
                   fallback; invisible to raw-input listeners.

Tier selection happens once at startup: uinput if the platform and
/dev/uinput permissions allow, pynput otherwise. type() always uses the
session tier — driver-tier scancodes can't express arbitrary unicode text.
"""

from __future__ import annotations

import logging
import os
import sys

from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

from stagehand import keys
from stagehand.roadie import Service

log = logging.getLogger(__name__)


UDEV_RULE_PATH = '/etc/udev/rules.d/70-stagehand-uinput.rules'
UDEV_RULE = 'KERNEL=="uinput", TAG+="uaccess", OPTIONS+="static_node=uinput"'

# uaccess grants an ACL to the active seat user the moment udev retriggers —
# no group membership, no re-login. Every step is idempotent (own rule file,
# never appending to anything shared), so rerunning is always safe.
ENABLE_SCRIPT = f"""set -e
printf '%s\\n' '{UDEV_RULE}' > {UDEV_RULE_PATH}
echo uinput > /etc/modules-load.d/stagehand-uinput.conf
modprobe uinput
udevadm control --reload-rules
udevadm trigger --name-match=uinput
"""

OFFERABLE = ('no_node', 'no_permission')


def diagnose_uinput() -> str:
    """Driver-tier availability: 'ok', 'unsupported', 'no_evdev', 'no_node', 'no_permission'.

    States in OFFERABLE are fixable by running ENABLE_SCRIPT as root.
    """
    if sys.platform != 'linux':
        return 'unsupported'
    try:
        import evdev  # noqa: F401
    except ImportError:
        return 'no_evdev'
    if not os.path.exists('/dev/uinput'):
        return 'no_node'
    if not os.access('/dev/uinput', os.W_OK):
        return 'no_permission'
    return 'ok'


class _PynputBackend:
    tier = 'session'

    def __init__(self, controller: KeyboardController):
        self.controller = controller

    def press(self, name: str) -> None:
        self.controller.press(self._resolve(name))

    def release(self, name: str) -> None:
        self.controller.release(self._resolve(name))

    def _resolve(self, name: str):
        key = keys.to_pynput(name)
        if key is None:
            raise ValueError(f'{name!r} requires the driver-tier (uinput) backend')
        return key


class _UinputBackend:
    tier = 'driver'

    def __init__(self):
        from evdev import UInput, ecodes

        self._ecodes = ecodes
        codes = [ecodes.ecodes[name] for name in set(keys.KEYS.values())]
        self.ui = UInput({ecodes.EV_KEY: codes}, name='stagehand-virtual-keyboard')

    def press(self, name: str) -> None:
        self._write(name, 1)

    def release(self, name: str) -> None:
        self._write(name, 0)

    def _write(self, name: str, value: int) -> None:
        evdev_name = keys.to_evdev(name)
        if evdev_name is None:
            log.warning(f'no physical key for {name!r}, skipping')
            return
        self.ui.write(self._ecodes.EV_KEY, self._ecodes.ecodes[evdev_name], value)
        self.ui.syn()


class KeyboardService(Service):
    """Provides keyboard simulation to JS action code.

    All key arguments accept canonical combo specs (see stagehand.keys):
        stagehand.keyboard.tap('a')
        stagehand.keyboard.tap('ctrl+shift+l')
        stagehand.keyboard.press('ctrl')
        stagehand.keyboard.release('ctrl')
        stagehand.keyboard.type('hello world')
    """

    name = ['keyboard', 'kb']

    def __init__(self):
        self.controller = KeyboardController()
        self.backend = _PynputBackend(self.controller)
        self.diagnosis = ''
        self.retry_backend()

    def retry_backend(self) -> bool:
        """(Re)attempt the driver-tier backend, hot-swapping on success.

        Callable at any time — the setup dialog uses it to activate the
        driver tier live after the udev rule is installed.
        """
        if self.backend.tier == 'driver':
            return True
        self.diagnosis = diagnose_uinput()
        if self.diagnosis == 'ok':
            try:
                self.backend = _UinputBackend()
                log.info('keyboard send: driver tier (uinput)')
                return True
            except Exception as e:
                self.diagnosis = f'uinput error: {e}'
        log.info(f'keyboard send: session tier (pynput) [{self.diagnosis}]')
        return False

    def tap(self, key: str) -> None:
        """Press and release a key or combo: mods down, key tapped, mods up."""
        parts = keys.parse_combo(key)
        for part in parts:
            self.backend.press(part)
        for part in reversed(parts):
            self.backend.release(part)

    def press(self, key: str) -> None:
        """Press and hold a key or combo."""
        for part in keys.parse_combo(key):
            self.backend.press(part)

    def release(self, key: str) -> None:
        """Release a held key or combo."""
        for part in reversed(keys.parse_combo(key)):
            self.backend.release(part)

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
