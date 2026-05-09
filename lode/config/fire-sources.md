# Fire Sources

**File**: `src/stagehand/fire_sources.py`

Fire sources bridge external events (keyboard, device, websocket, etc.) into `TriggerRegistry.on_fire()`. They are the input side of the narrow waist — they don't know what actions exist, they just emit typed event dicts.

## KeyboardFireSource

A `@singleton` QObject that owns a `pynput.keyboard.Listener` thread and emits fire events for every key press/release.

```python
KeyboardFireSource()  # always returns same instance

# Connects to trigger registry:
keyboard_source.connect_registry(registry)

# Emits fire events:
# {'type': 'keyboard', 'key': 'ctrl+shift+l', 'event': 'press'}
# {'type': 'keyboard', 'key': 'a', 'event': 'release'}
```

Key normalization:
- `KeyCode(char='a')` → `'a'`
- `Key.space` → `'space'`
- `Key.ctrl_l` → `'ctrl'` (strips _l/_r/_gr variants)

Also emits Qt signals `key_pressed(str)` and `key_released(str)` for any remaining widget-based triggers.

## StartupFireSource

Simple fire source that emits a startup event after a configurable delay.

```python
StartupFireSource(registry, delay_ms=2000)
# Emits: {'type': 'startup', 'delay': 2000}
```

## Migrating from Widget-Based Triggers

The old architecture had `KeyboardTrigger` widgets directly connected to `ActionWidget.run()` via Qt signals. The new architecture has `KeyboardFireSource` emitting typed events into `TriggerRegistry`.

| Old | New |
|-----|-----|
| `ListenerObject` (singleton) | `KeyboardFireSource` (singleton) |
| `KeyboardTrigger.triggered` signal | `registry.on_fire(event_dict)` |
| `ActionWidget.run()` direct call | Engine task execution |

## Related

- [config/trigger-registry.md](trigger-registry.md) — Where fire events are matched
- [config/action-pipeline.md](action-pipeline.md) — Wiring it all together