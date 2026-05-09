# Terminology

| Term | Meaning |
|------|---------|
| **Action** | User-defined unit combining trigger + filter + task. The full routing unit. |
| **Task** | What runs when an action fires. Was "Output" / "ActionItem". Either a named task ID from the library (`obs.switchScene`) or inline JS (`stagehand.js`). |
| **Trigger** | Event source that activates an action. Distilled to a `fire` event for the engine. |
| **Filter** | Conditional check on a `fire` event. Must pass for the task to execute. `type: {params}` format. |
| **Fire** | The narrow-waist event. All trigger sources distill down to `fire` → engine matches → task execution. |
| **Task Library** | JS files in `config/tasks/` defining named, composable tasks via `stagehand.register()`. Shared by reference, not copy. |
| **Helpers** | JS utility functions in `config/helpers/`, injected as `roadie.helpers.*` into every context. |
| **Action Config** | YAML file (`config/actions.yaml`) defining pages, actions, triggers, filters, and task references. Human-editable. |
| **Page** | Named group of actions in the config. Displayed as a tab in the UI. |
| **Service** | Python class injected into JS contexts via `stagehand.service.method()`. Replaces `SandboxExtension`. |
| **stagehand Proxy** | Nested JS Proxy routing `stagehand.service.method()` calls to `__service_method` FFI callables, with auto-unwrap for dict/list returns. |
| **Roadie** | QuickJS engine module at `src/stagehand/roadie/`. Provides `Engine`, `Service`, `ExecutionResult`, `ValidationResult`, `ExtensionToServiceAdapter`. |
| **ExtensionToServiceAdapter** | Adapter wrapping any `SandboxExtension` as a `Service`. Transitional — each extension will migrate to `Service` directly. |
| **Device** | Physical hardware (Stomp pedals, click switches) managed via codex DeviceManager. |
| **Plugin** | Module in `src/stagehand/plugins/` that registers services, triggers, filters, or pages. |

## Deprecated Terms (being replaced)

| Old Term | New Term | Notes |
|----------|----------|-------|
| Output | Task | "Output" was the old name for what runs. Now "Task". |
| ActionItem | TaskItem | Widget base class for task selectors. |
| SandboxExtension | Service | Python callables injected into JS. Each ext migrates to `Service` parent class. |
| Sandbox | Engine | The execution environment. `Sandbox` class delegates to Roadie `Engine`. |
| actions.json | actions.yaml | Widget state dump → human-editable config. |
| Library (copy-on-use) | Task Library (by reference) | Library copied templates → task library shared by name reference. |