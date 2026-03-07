# Terminology

| Term | Meaning |
|------|---------|
| **Action** | User-defined workflow combining trigger + filter + output. Saved as JSON, displayed as ActionWidget. |
| **Trigger** | Event source that activates an action. Types: keyboard, joystick, device, sandbox (manual), startup. |
| **Filter** | Conditional check that must pass for an action to execute. Multiple filters can be stacked (AND logic). |
| **Output** | The operation performed when action runs. Types: sandbox (Python), keyboard, shell, cyber, OBS commands. |
| **Sandbox** | Sandboxed Python execution environment with `save()`/`load()` persistence and extension injection. |
| **Page** | Tab in the main UI containing a collection of actions. Saved as `actions.json`. |
| **Plugin** | Module in `src/stagehand/plugins/` that registers triggers, filters, or outputs. |
| **Extension** | Object registered in Sandbox that injects functions/classes into sandbox namespace. |
| **Device** | Physical hardware (Stomp pedals, click switches) managed via codex DeviceManager. |
| **ActionWidgetGroup** | Container managing a list of actions with group-level filters. |
| **TriggerItem** | Base class for trigger widgets. Subclasses register via `name` class attribute. |
| **ActionItem** | Base class for output widgets. Subclasses register via `name` class attribute. |
| **FilterStackItem** | Base class for filter widgets. Must implement `check()` returning bool. |
| **StagehandPage** | Base class for tab pages. Pages register via `page_type` and `tags` ['singleton', 'user']. |