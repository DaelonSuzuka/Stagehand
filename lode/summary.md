# Stagehand Summary

Stagehand is a Python/Qt desktop automation tool for streamers and content creators. It provides an event-driven action system with a config-centric architecture: human-editable YAML config defines triggers and task references, JS task files define what the system can do, and the Roadie QuickJS engine evaluates all action code.

**Core Architecture**: Actions combine a trigger, optional filters, and a task. The config file (`config/actions.yaml`) is the source of truth — widgets are editors for the config, not the routing layer. All trigger sources distill down to `fire` events, matched by a `TriggerRegistry` against the config. Tasks are JS code executed in isolated QuickJS contexts via the Roadie engine. Named tasks are defined in `config/tasks/*.js` and shared by reference. Inline JS uses `stagehand.js: {body: "..."}` or YAML block scalars.

**Config Format**: Everything follows the `type: {params}` pattern — triggers, tasks, and filters. Example: `- keyboard: {key: "ctrl+shift+l"}` (trigger), `obs.switchScene: {scene: "Live"}` (task). This makes the config human-readable, diffable, and editable by hand.

**Roadie Engine**: QuickJS evaluation engine at `src/stagehand/roadie/`. `Engine.execute()`/`evaluate()`/`validate()` for action code. `stagehand` JS Proxy routes `stagehand.service.method()` calls through FFI to Python `Service` methods. `ExtensionToServiceAdapter` wraps existing `SandboxExtension` subclasses — each will migrate to `Service` directly.

**Key Technology Stack**: Python 3.10+, PySide6, QuickJS (action evaluation), obs-websocket-py, pygame-ce, pynput.

**Active Plugins** (during transition): keyboard, web_server. All others (obs_core, shell, joystick, godot, etc.) temporarily disabled.

**Workspace Dependencies**: qtstrap (v0.7.1), codex-engine-pyqt (v0.3.1), monaco-qt (v0.2.0).

**Entry Point**: `stagehand.__main__:main()` creates the Application singleton and MainWindow.

**In Transition**: Replacing the old widget-centric architecture (actions.json Qt widget dump + Python sandbox) with config-centric architecture (YAML config + JS task library + fire events + Roadie engine). See `plans/config-format.md` for the full plan.