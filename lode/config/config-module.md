# Config Module

**File**: `src/stagehand/config.py`

The config module provides data models and I/O for the human-editable action configuration system.

## File Layout

```
config/
  actions.yaml          ← trigger wiring (YAML)
  tasks/                ← JS task library
    obs.js
    streaming.js
  helpers/              ← shared utility functions
    utils.js
```

## Data Models

All follow the `type: {params}` pattern for consistent parsing:

| Model | Purpose | Parse from |
|-------|---------|------------|
| `TriggerConfig` | Trigger definition (type + params) | `{'keyboard': {'key': 'ctrl+l'}}` |
| `FilterConfig` | Filter definition (type + params/value) | `{'active_window': 'OBS'}` |
| `TaskRef` | Task reference (named ID or inline JS) | `{'obs.switchScene': {'scene': 'Live'}}` or `{'stagehand.js': {'body': 'code'}}` |
| `ActionConfig` | Full action: name + triggers + task + filters | |
| `PageConfig` | Named group of actions | |
| `ActionsConfig` | Top-level: pages dict | |

## TriggerConfig.matches()

Each trigger has a `matches(fire_event)` method that checks type and params:

```python
trigger = TriggerConfig(type='keyboard', params={'key': 'ctrl+shift+l'})
trigger.matches({'type': 'keyboard', 'key': 'ctrl+shift+l'})  # True
trigger.matches({'type': 'keyboard', 'key': 'ctrl+k'})         # False
trigger.matches({'type': 'device', 'key': 'ctrl+shift+l'})     # False
```

Fire events can have extra fields — the trigger only checks its own params.

## TaskRef Inline vs Named

- **Named**: `TaskRef(task_id='obs.switchScene', params={'scene': 'Live'})` — looked up from task library
- **Inline**: `TaskRef(task_id='stagehand.js', params={'body': 'code'})` — evaluated directly

## I/O Functions

- `load_actions_config(path)` — Parse `actions.yaml`, returns `ActionsConfig`. Accepts optional path for testing.
- `save_actions_config(config, path)` — Serialize to YAML. Auto-creates parent dirs.
- `load_task_files(path)` — Load all `*.js` from `tasks/` directory.
- `load_helper_files(path)` — Load all `*.js` from `helpers/` directory.
- `ensure_default_config()` — Create seed `actions.yaml` if none exists.

All I/O functions accept optional `Path` parameters to avoid dependency on `OPTIONS.config_dir` in tests.

## YAML Format

```yaml
pages:
  Streaming:
    actions:
      - name: Go Live
        enabled: true
        triggers:
          - keyboard: {key: "ctrl+shift+l"}
          - device: {name: "stomp4", pedal: 1}
        task:
          obs.switchScene: {scene: "Live"}
        filters:
          - active_window: "OBS"
```

## Related

- [trigger_registry.md](trigger-registry.md) — Matches fire events to actions
- [plans/config-format.md](../plans/config-format.md) — Design plan
- [architecture/new-config-format.md](../architecture/new-config-format.md) — Architecture doc