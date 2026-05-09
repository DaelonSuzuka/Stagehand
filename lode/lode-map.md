# Lode Map

## Core Documentation
- [summary.md](summary.md) - Project overview and tech stack
- [terminology.md](terminology.md) - Domain vocabulary (updated for Task/Action/Fire model)
- [practices.md](practices.md) - Development patterns and conventions

## Architecture
- [architecture/entry-points.md](architecture/entry-points.md) - Application bootstrap and initialization
- [architecture/actions-system.md](architecture/actions-system.md) - Action/Trigger/Filter/Output architecture (legacy — being replaced)
- [architecture/new-config-format.md](architecture/new-config-format.md) - Config-centric architecture: YAML actions + JS tasks + fire events
- [architecture/sandbox.md](architecture/sandbox.md) - Python sandbox execution model (legacy — being replaced by Roadie engine)
- [architecture/plugins.md](architecture/plugins.md) - Plugin discovery and loading
- [architecture/dependencies.md](architecture/dependencies.md) - External workspace dependencies (qtstrap, codex, monaco-qt)
- [architecture/contribution-points.md](architecture/contribution-points.md) - Plugin extension points and registration
- [architecture/logging.md](architecture/logging.md) - LogMonitor performance issues and mitigation
- [architecture/sidebar.md](architecture/sidebar.md) - Sidebar system architecture

## Components
- [actions/action-widget.md](actions/action-widget.md) - ActionWidget and ActionWidgetGroup (being replaced by config editors)
- [actions/triggers.md](actions/triggers.md) - Trigger system (being replaced by fire events)
- [actions/filters.md](actions/filters.md) - Filter system (being replaced by data filters)
- [sandbox/runtime.md](sandbox/runtime.md) - QuickJS sandbox execution via Roadie engine
- [library/library.md](library/library.md) - Library system (being replaced by task library)

## Config System
- [config/config-module.md](config/config-module.md) - YAML config data models, I/O, and default seed
- [config/trigger-registry.md](config/trigger-registry.md) - Fire event matching and task execution

## Roadie Engine
- [roadie/engine.md](../src/stagehand/roadie/engine.py) - QuickJS evaluation engine: Proxy, autoUnwrap, Service, execution modes
- [roadie/adapter.md](../src/stagehand/roadie/adapter.py) - ExtensionToServiceAdapter: wraps SandboxExtension as Service

## Plugins
- [plugins/builtin.md](plugins/builtin.md) - Built-in plugins overview
- [plugins/keyboard.md](plugins/keyboard.md) - Keyboard trigger and action
- [plugins/obs-core.md](plugins/obs-core.md) - OBS websocket integration

## Architecture (qtstrap)
- [architecture/devtools.md](architecture/devtools.md) - Qt live devtools: Scene Tree, Inspector, Style Editor, REPL

## Plans
- [plans/library-system.md](plans/library-system.md) - Reusable definition library (legacy — replaced by task library)
- [plans/config-format.md](plans/config-format.md) - New config format: YAML actions + JS tasks + fire events

## Scratch
- [tmp/](tmp/) - Session scraps (git-ignored)