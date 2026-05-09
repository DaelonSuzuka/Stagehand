# New Config Format Plan

## Goal

Replace `actions.json` (Qt widget state dump) with a human-editable config system:
- `config/actions.yaml` — trigger wiring (data: when to do it)
- `config/tasks/*.js` — task library (code: what to do)
- `config/helpers/*.js` — helper functions (shared utilities)

## Terminology

- **Action** = trigger + filter + task (the whole unit)
- **Task** = what runs (was "output" / "ActionItem")
- **Fire** = the narrow-waist event all triggers distill to

## Config File Format

### `config/actions.yaml`

```yaml
pages:
  Streaming:
    actions:
      - name: Go Live
        triggers:
          - keyboard: {key: "ctrl+shift+l"}
          - device: {name: "stomp4", pedal: 1}
        task:
          obs.switchScene: {scene: "Live"}
        filters:
          - active_window: "OBS"

      - name: Toggle Mic
        triggers:
          - keyboard: {key: "ctrl+m"}
        task:
          obs.toggleMute: {source: "Mic/Aux"}

      - name: Send Alert
        triggers:
          - startup: {delay: 2000}
        task:
          stagehand.js: |
            var count = stagehand.load("alert_count") || 0
            count += 1
            stagehand.save("alert_count", count)
            stagehand.print("Alert #" + count)
```

**Key patterns:**
- Triggers use `type: {params}` — consistent across all trigger types
- Tasks use `task_id: {params}` — matches the same `type: {params}` pattern
- Inline JS uses `stagehand.js` with either `{body: "code"}` or YAML `|` block scalar
- Filters use `type: value` or `type: {params}` — same pattern
- Everything is data, not code (except `stagehand.js` inline tasks)

### `config/tasks/obs.js`

```js
stagehand.register({
  id: "obs.switchScene",
  run: (params) => stagehand.obs.switchScene(params.scene),
})

stagehand.register({
  id: "obs.toggleMute",
  run: (params) => stagehand.obs.toggleMute(params.source),
})

stagehand.register({
  id: "go-live",
  run: () => {
    stagehand.obs.switchScene("Live")
    stagehand.obs.startStreaming()
  }
})
```

### `config/helpers/utils.js`

```js
roadie.helpers.discordAlert = function(message) {
  stagehand.http.post("https://discord.example.com/webhook",
    { json: { content: message } })
}
```

## Architecture Change: Widget-Centric → Config-Centric

### Current (widget-centric)
```
TriggerItem (Qt widget)
  → self.triggered.connect(ActionWidget.run)
  → ActionWidget.run() calls Sandbox().run(code)
```
Config is a dump of widget state. The widget *is* the routing.

### New (config-centric)
```
External event source (keyboard, device, etc.)
  → emits fire event {type: 'keyboard', key: 'ctrl+shift+l'}
  → TriggerRegistry matches fire → resolves action → looks up task
  → engine.execute(task_code, params)
```
Config is the source of truth. Widgets are editors for the config, not the routing layer.

### Trigger Registry

A new `TriggerRegistry` replaces the direct widget-to-action wiring:

```python
class TriggerRegistry:
    """Matches fire events to task IDs using the action config."""

    def on_fire(self, event: dict):
        """Called by any trigger source with a distilled event dict.
        Looks up matching actions in the config, checks filters, executes tasks."""
        for action in self.matching_actions(event):
            if self.check_filters(action, event):
                self.engine.execute(action.task, action.params)
```

Each trigger source (keyboard listener, device manager, etc.) calls `registry.on_fire(event_dict)` instead of directly calling a widget's `run()`.

### Filter Evaluation

Filters also move from Qt widgets to data:

```python
def check_filters(self, action, event):
    for filter_def in action.filters:
        filter_type = list(filter_def.keys())[0]
        filter_params = filter_def[filter_type]
        if not self.filter_registry.check(filter_type, filter_params, event):
            return False
    return True
```

JS sandbox filters evaluate `stagehand.js: {body: "expression"}` as boolean expressions.

## Implementation Steps

### Phase 1: Config format + engine integration
1. Create `config/actions.yaml` schema and loader
2. Create `config/tasks/` directory and task loader
3. Create `config/helpers/` directory and helper loader
4. Build `TriggerRegistry` that matches fire events to tasks
5. Wire `TriggerRegistry` to `Engine.execute()`
6. Write migration for core trigger types (keyboard, startup, device)

### Phase 2: Active plugins
1. Migrate `keyboard` plugin: trigger source → fire event emitter, `KeyboardExtension` → `Service`
2. Migrate `obs_core` plugin: `ObsExtension` → `Service`, `ObsTrigger` → fire event
3. Migrate `shell` plugin: `ShellExtension` → `Service`
4. Disable all other plugins in loader

### Phase 3: UI rebuild
1. Replace `ActionWidget` serialization with config-centric load/save
2. Replace `MainTabWidget.save()` with YAML writer
3. Replace `MainTabWidget.load()` with YAML reader
4. Task editor: integrate with `config/tasks/` for named tasks
5. Inline JS editor: `stagehand.js` body field

### Phase 4: Migrate remaining plugins one by one
- Each plugin: `Extension` → `Service`, trigger → fire emitter, action → task/config

## Active Plugins During Transition

| Plugin | Status | Provides |
|--------|--------|----------|
| **keyboard** | Active | KeyboardTrigger → fire events + KeyboardService + MouseService |
| **web_server** | Active | WebTrigger → fire events (websocket) + WebInterfacePage (remote control UI) |
| All others | Disabled | Temporarily commented out in plugin loader (obs_core, shell, joystick, godot, autohotkey, cyber, saleae, microphone_voter, device filters) |

Core (non-plugin) triggers remain active: `StartupTrigger`, `DeviceTrigger`, `SandboxTrigger` (manual).

## Design Principles

- **Config is source of truth** — widgets edit the config, they don't hold state
- **Consistent `type: {params}` pattern** — triggers, tasks, and filters all use it
- **Tasks by reference** — `obs.switchScene` is defined once, referenced N times
- **Inline JS for simple cases** — `stagehand.js: {body: "..."}` for one-off actions
- **Human-editable first** — YAML reads naturally, diffs cleanly
- **No versioning needed yet** — add `version` field when format stabilizes