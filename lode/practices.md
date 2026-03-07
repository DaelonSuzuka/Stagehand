# Practices

## Plugin Development

**Location**: `src/stagehand/plugins/<plugin_name>/`

**Required Files**:
- `__init__.py` - imports and exports plugin components
- Extension classes (register into SandboxExtension subclass)
- TriggerItem/ActionItem/FilterStackItem subclasses

**Registration Pattern**:
```python
# In __init__.py
from .keyboard_trigger import KeyboardTrigger
from .keyboard_action import KeyboardAction
from .keyboard_extension import KeyboardExtension
```

**Item Registration**:
```python
class MyTrigger(TriggerItem):
    name = 'my_trigger'  # Display name in UI
    
    def get_data(self) -> dict:
        return {'key': self.input.text()}  # Serialize
    
    def set_data(self, data: dict):
        self.input.setText(data.get('key', ''))
    
    def reset(self):
        self.input.clear()
```

**Extension Pattern**:
```python
class MyExtension(SandboxExtension):
    name = 'my_extension'
    def my_function(self, arg):
        # Available in sandbox as: my_extension.my_function(arg)
        pass
```

## Action Widget Pattern

All actions follow this lifecycle:
1. `ActionWidget.__init__()` - creates trigger, filter, and output widgets
2. `set_data()` - loads from JSON
3. `get_data()` - serializes to JSON
4. `run()` - executes output if filters pass
5. `remove()` - cleans up and deletes

## Sandbox Execution

```python
# In action code
Sandbox().this = self  # Set context
Sandbox().source = self.sender()  # Event source
Sandbox().run(text, error_cb=callback)  # Execute
```

## Testing HTTP Actions

Use the HTTP test server for testing HTTP actions locally:

```bash
# Run standalone
make http-server
# or
uv run python tools/http_test_server.py
```

```python
from tools.http_test_server import HttpTestServer

# Start server on port 8080 (default)
server = HttpTestServer()
server.start()

# Available endpoints:
# GET  /              - Help message
# GET  /echo          - Echo request details
# POST /echo          - Echo POST body
# PUT  /echo          - Echo PUT body
# GET  /status/{code} - Return custom status code
# GET  /slow          - Slow response (1s delay)
# GET  /json          - Return sample JSON
# GET  /requests      - Get all logged requests
# DELETE /requests    - Clear request log

# Make test requests
import httpx
response = httpx.post(f'{server.url}/echo', json={'test': 'data'})

server.stop()
```

**Available in sandbox namespace**:
- `save(name, value)` / `load(name)` - persistence
- `data` - dict of saved values
- `print()` - redirected to tools panel
- Extensions from `SandboxExtension.__subclasses__()`

## Data Persistence

Config stored in `OPTIONS.config_dir / 'actions.json'`:
```json
{
  "current_tab": 0,
  "pages": {
    "Page 1": {
      "page_type": "Generic Actions",
      "name": "Page 1",
      "enabled": true,
      "actions": [...],
      "filter": {"enabled": true, "filters": [...]}
    }
  }
}
```

## Naming Conventions

- **Files**: `snake_case.py`
- **Classes**: `PascalCase`
- **UI Widgets**: `ActionWidget`, `TriggerItem`, `FilterStack`
- **Singletons**: `@singleton` decorator from `qtstrap`
- **Pages**: `StagehandPage` subclass with `page_type` and `tags`

## Qt Patterns

- Use `CHBoxLayout`, `CVBoxLayout` from qtstrap for layouts
- `PersistentCheckableAction` for menu items with saved state
- `Signal`/`Slot` for inter-widget communication
- `changed` signal pattern for dirty tracking

**IMPORTANT: Signal Declaration**

Signals MUST be declared at the class level, never in `__init__()`:

```python
# CORRECT - Signal at class level
class MyTrigger(TriggerItem):
    name = 'my_trigger'
    triggered = Signal()  # Class-level signal
    
    def __init__(self, changed, run, owner=None):
        super().__init__()
        self.triggered.connect(run)
        # ...

# WRONG - Signal in __init__ will fail
class MyTrigger(TriggerItem):
    name = 'my_trigger'
    
    def __init__(self, changed, run, owner=None):
        super().__init__()
        self.triggered = Signal()  # ERROR: AttributeError
        self.triggered.connect(run)
```

This applies to all `QObject` subclasses including `TriggerItem`, `ActionItem`, `StagehandPage`, and custom widgets.