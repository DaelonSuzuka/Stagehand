# Services

**Directory**: `src/stagehand/services/`

Service classes are direct `Service` subclasses that inject Python callables into QuickJS contexts. They replace `SandboxExtension` subclasses — no adapter needed.

## Current Services

### KeyboardService (`services/keyboard_service.py`)

```python
class KeyboardService(Service):
    name = ['keyboard', 'kb']
    
    def tap(key: str) -> None      # Press + release
    def press(key: str) -> None    # Press down
    def release(key: str) -> None  # Release
    def type(string: str) -> None  # Type a string
```

JS usage: `stagehand.keyboard.tap('a')`, `stagehand.kb.type('hello')`

### MouseService (`services/keyboard_service.py`)

```python
class MouseService(Service):
    name = 'mouse'
    
    def position(x: int, y: int) -> None    # Move to absolute position
    def move(dx: int, dy: int) -> None      # Move by offset
    def scroll(direction: str, steps: int)  # Scroll wheel
    def click(button: str, times: int = 1) # Click (resolves 'left'/'right'/'middle')
    def press(button: str) -> None          # Hold button
    def release(button: str) -> None        # Release button
```

JS usage: `stagehand.mouse.click('left')`, `stagehand.mouse.position(100, 200)`

## Migration from SandboxExtension

Old pattern:
```python
class KeyboardExtension(SandboxExtension):
    name = ['keyboard', 'kb']
    def tap(self, key): ...
```

New pattern:
```python
class KeyboardService(Service):
    name = ['keyboard', 'kb']
    def tap(self, key: str) -> None: ...
```

Differences:
- Parent class: `Service` instead of `SandboxExtension`
- No `__getattr__` proxying — methods are explicit
- No `Sandbox().tools.print()` calls — services should return values, not print
- Button names resolved inside the service (`'left'` → `Button.left`)
- Type hints on all methods

## Related

- [sandbox/runtime.md](../sandbox/runtime.md) — Roadie engine and Service base class
- [config/action-pipeline.md](../config/action-pipeline.md) — Where services are registered