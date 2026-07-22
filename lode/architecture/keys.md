# Key Vocabulary and Send Tiers

**Module**: `src/stagehand/keys.py` — pure data + adapters, no Qt imports.

## Canonical Form

Bare lowercase names joined with `+`, modifiers first: `ctrl+shift+f13`.
This is the single format used by the YAML config, fire events, trigger
matching, the key picker, and service send calls. `MODIFIERS` order
(`ctrl, shift, alt, super`) is the canonical combo order; `parse_combo()`
normalizes any input ordering and resolves aliases (`cmd`/`win`/`meta` →
`super`, `escape` → `esc`, etc.).

Single characters outside the table (e.g. `é`) are valid canonical names
but session-tier only — no physical key, no evdev code.

## Adapters (one per representation edge)

| Adapter | Direction | Consumer |
|---|---|---|
| `normalize_pynput()` | pynput event → canonical | `KeyboardFireSource` |
| `to_pynput()` | canonical → `Key`/char | session-tier sending |
| `to_evdev()` | canonical → `'KEY_*'` name | driver-tier sending |
| `to_hotkey_spec()` | canonical → `<ctrl>+l` | legacy `HotKey.parse` trigger path |
| `_event_key_name()` (in `key_picker.py`) | Qt event → canonical | key picker capture |

`to_pynput()` returning `None` marks a driver-tier-only key (f21–f24,
numpad `kp_*`) — pynput's `Key` enum stops at f20 and has no numpad names.

Known limitation: with Ctrl held, pynput delivers control characters
(`'\x0c'` for ctrl+l) as `KeyCode.char`; `normalize_pynput` passes them
through. See migration review M-2 — combo composition must solve this.

## Send Tiers (`services/keyboard_service.py`)

Injection depth determines which programs see synthetic input: a listener
sees only events that entered the stack *below* its listening point.

- **driver tier** — `_UinputBackend`, Linux only: a uinput virtual keyboard
  (`python-evdev`). Events are indistinguishable from hardware — reaches
  raw-input listeners (games, TeamSpeak-default-mode hotkeys) and native
  Wayland clients. Requires write access to `/dev/uinput` (udev rule).
- **session tier** — `_PynputBackend`: SendInput / XTEST / CGEventPost.
  Portable fallback. Invisible to raw-input listeners; on Wayland, XTEST
  reaches XWayland clients only. `type()` always uses this tier (arbitrary
  unicode has no scancode).

Selection happens once in `KeyboardService.__init__`: uinput attempted on
Linux, any failure logs and falls back to pynput. `tap`/`press`/`release`
all accept combo specs; `tap('ctrl+shift+l')` presses modifiers, taps the
key, releases in reverse.

Windows driver tier (Interception) and macOS (Karabiner DriverKit) are
future options — see kmonad for the portable-trio existence proof. Note
the anti-cheat asterisk: some anti-cheats detect the Interception driver
itself.

To enable the driver tier on Linux:

```
# /etc/udev/rules.d/70-stagehand-uinput.rules
KERNEL=="uinput", MODE="0660", GROUP="input", OPTIONS+="static_node=uinput"
```

plus membership in the `input` group.

## Key Picker (`src/stagehand/key_picker.py`)

`KeyPicker` — drop-in line edit surface (`text`/`setText`/`textChanged`)
plus a button opening `KeyPickerDialog`. Three entry paths, one
authoritative raw line: capture button (Qt-side `grabKeyboard`, works for
pedal-emitted keys when the box is focused), modifier checkboxes + key
list generated from `keys.names()`, and the raw line edit itself. Output
is always canonical. Used by `KeyboardTrigger`; built to be reused by the
config editors.

## Related

- [../config/fire-sources.md](../config/fire-sources.md) — input side
- [../config/services.md](../config/services.md) — service surface
- [../plans/migration-review-2026-07.md](../plans/migration-review-2026-07.md) — M-2 combo composition gap (still open)
