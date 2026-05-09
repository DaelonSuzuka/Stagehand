# Action Pipeline

**File**: `src/stagehand/action_pipeline.py`

The `ActionPipeline` singleton wires together the entire config-centric action system at app startup.

## Initialization Order

```mermaid
sequenceDiagram
    participant App as Application
    participant AP as ActionPipeline
    participant E as Engine
    participant Reg as TriggerRegistry
    participant KF as KeyboardFireSource

    App->>AP: ActionPipeline() (singleton)
    AP->>E: Engine()
    AP->>E: register_service(KeyboardService)
    AP->>E: register_service(MouseService)
    AP->>AP: ensure_default_config()
    AP->>AP: load_actions_config()
    AP->>E: register_helper(task JS sources)
    AP->>E: register_helper(helper JS sources)
    AP->>Reg: TriggerRegistry(engine, config)
    AP->>Reg: register_task_source(task_id, source)
    AP->>KF: KeyboardFireSource() (singleton)
    AP->>KF: connect_registry(registry)
```

## Services Registered

| Service | JS name | Methods |
|---------|---------|---------|
| `KeyboardService` | `stagehand.keyboard`, `stagehand.kb` | `tap(key)`, `press(key)`, `release(key)`, `type(string)` |
| `MouseService` | `stagehand.mouse` | `click(button, times)`, `press(button)`, `release(button)`, `position(x,y)`, `move(dx,dy)`, `scroll(dir,steps)` |

## Fire Sources Connected

| Fire Source | Event Type | Example Event |
|-------------|------------|---------------|
| `KeyboardFireSource` | `keyboard` | `{'type': 'keyboard', 'key': 'ctrl+shift+l', 'event': 'press'}` |
| `StartupFireSource` | `startup` | `{'type': 'startup', 'delay': 2000}` |

## Hot Reload

- `reload_config()` — reload actions.yaml from disk
- `reload_tasks()` — reload config/tasks/*.js and re-register with registry
- `reload_helpers()` — reload config/helpers/*.js and re-inject into engine
- `reload_all()` — all of the above

## Related

- [config/config-module.md](config/config-module.md) — Config data models and I/O
- [config/trigger-registry.md](config/trigger-registry.md) — Fire event matching
- [architecture/new-config-format.md](architecture/new-config-format.md) — Architecture doc