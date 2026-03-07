# Sandbox Architecture

## Overview

The Sandbox provides a constrained Python execution environment for action outputs. It allows users to write Python scripts without full system access.

**File**: `src/stagehand/sandbox/sandbox.py`

## Class: Sandbox

```python
@singleton
class Sandbox(QObject):
    extensions = {}  # Injected objects
    
    def __init__(self):
        self.tools_dock = SandboxToolsDockWidget()
        self.tools = self.tools_dock.tools
        self.reset_environment()
```

## Execution Methods

| Method | Purpose | Returns |
|--------|---------|---------|
| `run(text, error_cb)` | Execute Python code | None (exec) |
| `eval(text, error_cb)` | Evaluate expression | None (eval) |
| `compile(text, error_cb)` | Syntax check | None |

## Namespace

```python
self._globals = {
    'save': self._save,           # Persistence
    'load': self._load,           # Retrieval
    'data': self._data,           # Data dict
    'print': self.tools.print,     # Redirected output
    'this': self.this,             # Context object
    'source': self.source,         # Event source
    **self.extensions,              # Plugin extensions
}
```

## Extension Injection

Plugins extend the sandbox by subclassing `SandboxExtension`:

```python
class KeyboardExtension(SandboxExtension):
    name = 'keyboard'
    
    def press(self, key):
        # Available as: keyboard.press(key)
        pass
        
    def release(self, key):
        # Available as: keyboard.release(key)
        pass
```

Registration happens in `Sandbox.__init__()`:
```python
for ext in SandboxExtension.__subclasses__():
    e = ext()
    self.extensions[ext.name] = e
```

## Persistence

```python
# In sandbox code:
save('counter', 42)
counter = load('counter')  # Returns 42

# Or directly:
data['counter'] += 1
```

Data stored in `Sandbox._data` dict, persists across action executions within session.

## Context Variables

When an action runs:

```python
# Set context in ActionWidget.run()
Sandbox().this = self      # The ActionWidget instance
Sandbox().source = sender  # The QEvent/source object

# Available in sandbox:
# this - reference to action
# source - reference to event source
```

**Important**: Context cleared after execution:
```python
self._globals['this'] = None
self._globals['source'] = None
```

## Error Handling

```python
def run(self, text, error_cb=None):
    try:
        code = compile(text, '', 'exec')
        exec(code, self._globals, self._locals)
    except Exception as e:
        error = str(e)
        
    if error_cb:
        error_cb(error)
    else:
        self.tools.print(error)  # Show in tools panel
```

## SandboxTools

**File**: `src/stagehand/sandbox/sandbox_tools.py`

- Output panel showing `print()` output
- Error highlighting
- Clear button
- Docked in MainWindow