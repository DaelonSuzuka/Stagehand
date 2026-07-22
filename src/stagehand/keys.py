"""Canonical key vocabulary and representation adapters.

Canonical form is bare lowercase names ('a', 'f13', 'page_up') joined with '+'
for combos, modifiers first: 'ctrl+shift+l'. This is the format used by the
YAML config, fire events, and trigger matching.

Everything else is an adapter at an edge:
    pynput event -> canonical    normalize_pynput()  (fire sources, capture)
    canonical    -> pynput       to_pynput()         (session-tier sending)
    canonical    -> evdev name   to_evdev()          (driver-tier sending)
    canonical    -> HotKey spec  to_hotkey_spec()    (legacy trigger path)

Qt -> canonical lives in key_picker.py, the only Qt consumer.

Single characters outside the table (e.g. 'é') are valid canonical names but
session-tier only — they have no physical key / evdev code.
"""

from __future__ import annotations

from pynput.keyboard import Key, KeyCode


MODIFIERS = ('ctrl', 'shift', 'alt', 'super')

ALIASES = {
    'cmd': 'super',
    'win': 'super',
    'windows': 'super',
    'meta': 'super',
    'control': 'ctrl',
    'escape': 'esc',
    'return': 'enter',
    'del': 'delete',
    'pgup': 'page_up',
    'pgdn': 'page_down',
}

_PUNCTUATION = {
    '`': 'KEY_GRAVE',
    '-': 'KEY_MINUS',
    '=': 'KEY_EQUAL',
    '[': 'KEY_LEFTBRACE',
    ']': 'KEY_RIGHTBRACE',
    '\\': 'KEY_BACKSLASH',
    ';': 'KEY_SEMICOLON',
    "'": 'KEY_APOSTROPHE',
    ',': 'KEY_COMMA',
    '.': 'KEY_DOT',
    '/': 'KEY_SLASH',
}

# canonical name -> evdev key name; dict order is display order in pickers
KEYS: dict[str, str] = {
    **{c: f'KEY_{c.upper()}' for c in 'abcdefghijklmnopqrstuvwxyz'},
    **{d: f'KEY_{d}' for d in '1234567890'},
    **{f'f{n}': f'KEY_F{n}' for n in range(1, 25)},
    'ctrl': 'KEY_LEFTCTRL',
    'shift': 'KEY_LEFTSHIFT',
    'alt': 'KEY_LEFTALT',
    'super': 'KEY_LEFTMETA',
    'space': 'KEY_SPACE',
    'enter': 'KEY_ENTER',
    'tab': 'KEY_TAB',
    'esc': 'KEY_ESC',
    'backspace': 'KEY_BACKSPACE',
    'delete': 'KEY_DELETE',
    'insert': 'KEY_INSERT',
    'home': 'KEY_HOME',
    'end': 'KEY_END',
    'page_up': 'KEY_PAGEUP',
    'page_down': 'KEY_PAGEDOWN',
    'up': 'KEY_UP',
    'down': 'KEY_DOWN',
    'left': 'KEY_LEFT',
    'right': 'KEY_RIGHT',
    'caps_lock': 'KEY_CAPSLOCK',
    'num_lock': 'KEY_NUMLOCK',
    'scroll_lock': 'KEY_SCROLLLOCK',
    'print_screen': 'KEY_SYSRQ',
    'pause': 'KEY_PAUSE',
    'menu': 'KEY_COMPOSE',
    **_PUNCTUATION,
    'media_play_pause': 'KEY_PLAYPAUSE',
    'media_next': 'KEY_NEXTSONG',
    'media_previous': 'KEY_PREVIOUSSONG',
    'media_volume_up': 'KEY_VOLUMEUP',
    'media_volume_down': 'KEY_VOLUMEDOWN',
    'media_volume_mute': 'KEY_MUTE',
    **{f'kp_{d}': f'KEY_KP{d}' for d in '0123456789'},
    'kp_enter': 'KEY_KPENTER',
    'kp_plus': 'KEY_KPPLUS',
    'kp_minus': 'KEY_KPMINUS',
    'kp_multiply': 'KEY_KPASTERISK',
    'kp_divide': 'KEY_KPSLASH',
    'kp_dot': 'KEY_KPDOT',
}


def resolve(name: str) -> str | None:
    """Resolve a name or alias to its canonical form, or None if unknown."""
    name = name.strip().lower()
    name = ALIASES.get(name, name)
    if name in KEYS or len(name) == 1:
        return name
    return None


def is_modifier(name: str) -> bool:
    return resolve(name) in MODIFIERS


def parse_combo(spec: str) -> list[str]:
    """Parse a combo spec into canonical parts, modifiers first.

    Raises ValueError on unknown key names.
    """
    parts = [p for p in spec.strip().lower().split('+') if p]
    resolved = []
    for part in parts:
        canonical = resolve(part)
        if canonical is None:
            raise ValueError(f'unknown key: {part!r}')
        if canonical not in resolved:
            resolved.append(canonical)
    mods = [m for m in MODIFIERS if m in resolved]
    rest = [r for r in resolved if r not in MODIFIERS]
    return mods + rest


def format_combo(parts: list[str]) -> str:
    return '+'.join(parts)


def normalize_combo(spec: str) -> str:
    return format_combo(parse_combo(spec))


def names() -> list[str]:
    """All canonical key names, in display order."""
    return list(KEYS)


def normalize_pynput(key) -> str:
    """Convert a pynput Key or KeyCode to a canonical name.

    Examples:
        KeyCode(char='a') -> 'a'
        Key.space -> 'space'
        Key.ctrl_l -> 'ctrl'
        Key.cmd -> 'super'
    """
    if isinstance(key, KeyCode):
        if key.char:
            return key.char
        return str(key)
    if isinstance(key, Key):
        name = key.name
        for variant in ('_l', '_r', '_gr'):
            if name.endswith(variant):
                name = name[: -len(variant)]
                break
        return 'super' if name == 'cmd' else name
    return str(key)


def to_pynput(name: str):
    """Canonical name -> pynput Key or char, or None if session tier can't send it.

    None means driver-tier only (f21-f24, numpad, unknown names).
    """
    canonical = resolve(name)
    if canonical is None:
        return None
    if canonical == 'super':
        return Key.cmd
    if hasattr(Key, canonical):
        return Key[canonical]
    if len(canonical) == 1:
        return canonical
    return None


def to_evdev(name: str) -> str | None:
    """Canonical name -> evdev key name ('KEY_A'), or None if no physical key."""
    canonical = resolve(name)
    if canonical is None:
        return None
    return KEYS.get(canonical)


def to_hotkey_spec(spec: str) -> str:
    """Canonical combo -> pynput HotKey.parse() syntax: 'ctrl+l' -> '<ctrl>+l'.

    Raises ValueError if any part is unknown or session-tier unsendable.
    """
    parts = []
    for part in parse_combo(spec):
        key = to_pynput(part)
        if key is None:
            raise ValueError(f'no pynput representation for {part!r}')
        parts.append(f'<{key.name}>' if isinstance(key, Key) else key)
    return '+'.join(parts)
