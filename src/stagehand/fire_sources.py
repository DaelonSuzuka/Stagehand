"""Fire sources bridge external events into the TriggerRegistry.

Each trigger type (keyboard, device, websocket, etc.) has a fire source
that listens to its external event stream and calls registry.on_fire()
with a distilled event dict.

Fire sources are the input side of the narrow waist. They don't know what
actions exist or what tasks run — they just emit typed events.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from qtstrap import *
from pynput.keyboard import Listener

from stagehand import keys

if TYPE_CHECKING:
    from stagehand.trigger_registry import TriggerRegistry

log = logging.getLogger(__name__)


@singleton
class KeyboardFireSource(QObject):
    """Bridges pynput keyboard events into fire events.

    Emits fire events like:
        {'type': 'keyboard', 'key': 'ctrl+shift+l', 'event': 'press'}
        {'type': 'keyboard', 'key': 'a', 'event': 'release'}
        {'type': 'keyboard', 'key': 'ctrl+shift+l', 'event': 'hotkey'}

    Connects to the TriggerRegistry via on_fire callback.
    """

    key_pressed = Signal(str)  # emits normalized key string
    key_released = Signal(str)

    def __init__(self):
        super().__init__()
        self._registry: TriggerRegistry | None = None
        self._pressed_keys: set = set()

        self.listener = Listener(
            on_press=self._on_press,
            on_release=self._on_release,
        )
        App().aboutToQuit.connect(self.listener.stop)
        self.listener.start()

    def connect_registry(self, registry: TriggerRegistry) -> None:
        """Connect this fire source to a trigger registry."""
        self._registry = registry

    def _on_press(self, key) -> None:
        """Called by pynput listener thread on key press."""
        if key in self._pressed_keys:
            return  # Debounce repeats
        self._pressed_keys.add(key)

        normalized = keys.normalize_pynput(key)

        # Emit Qt signal (for UI triggers that still use the old path)
        self.key_pressed.emit(normalized)

        # Emit fire event to registry
        if self._registry is not None:
            self._registry.on_fire({
                'type': 'keyboard',
                'key': normalized,
                'event': 'press',
            })

    def _on_release(self, key) -> None:
        """Called by pynput listener thread on key release."""
        if key in self._pressed_keys:
            self._pressed_keys.remove(key)

        normalized = keys.normalize_pynput(key)

        self.key_released.emit(normalized)

        if self._registry is not None:
            self._registry.on_fire({
                'type': 'keyboard',
                'key': normalized,
                'event': 'release',
            })

    def stop(self) -> None:
        """Stop the keyboard listener."""
        self.listener.stop()


class StartupFireSource:
    """Fires startup events with a delay.

    Emits fire events like:
        {'type': 'startup', 'delay': 2000}
    """

    def __init__(self, registry: TriggerRegistry, delay_ms: int = 0):
        self._registry = registry
        self._delay_ms = delay_ms
        if delay_ms > 0:
            call_later(delay_ms, self._fire)
        else:
            self._fire()

    def _fire(self) -> None:
        self._registry.on_fire({
            'type': 'startup',
            'delay': self._delay_ms,
        })