"""Application-level initialization for the config-centric action system.

Wires together:
  - Roadie Engine (QuickJS evaluation)
  - Services (keyboard, mouse, etc.)
  - Config loader (actions.yaml, tasks, helpers)
  - Trigger registry (fire event matching)
  - Fire sources (keyboard, startup, etc.)
"""

from __future__ import annotations

import logging

from qtstrap import singleton
from stagehand.config import (
    ActionsConfig,
    load_actions_config,
    load_helper_files,
    load_task_files,
    ensure_default_config,
)
from stagehand.fire_sources import KeyboardFireSource
from stagehand.roadie import Engine
from stagehand.services import KeyboardService, MouseService
from stagehand.trigger_registry import TriggerRegistry

log = logging.getLogger(__name__)


@singleton
class ActionPipeline:
    """The central wiring point for the config-centric action system.

    Created once at app startup. Owns the engine, registry, and fire sources.
    Connects everything together so that fire events flow through the registry
    to the engine for execution.
    """

    def __init__(self):
        # 1. Create the engine
        self.engine = Engine()
        self.engine.on_print(lambda msg: log.info(f"[stagehand] {msg}"))

        # 2. Register services
        self.keyboard_service = KeyboardService()
        self.mouse_service = MouseService()
        for svc in [self.keyboard_service, self.mouse_service]:
            self.engine.register_service(svc)

        # 3. Load config
        ensure_default_config()
        self.config = load_actions_config()

        # 4. Load task files and register in the trigger registry
        # Task JS sources are evaluated by the registry when executing named tasks.
        # They're also injected as helpers so their functions are available in every context.
        self._task_sources: dict[str, str] = {}
        for name, source in load_task_files().items():
            self._task_sources[name] = source
            # Inject task file source as a helper so functions are available in contexts
            self.engine.register_helper(source)

        # 5. Load helper files — inject into every QuickJS context
        for name, source in load_helper_files().items():
            self.engine.register_helper(source)

        # 6. Create trigger registry and register task sources
        self.registry = TriggerRegistry(self.engine, self.config)
        for task_id, source in self._task_sources.items():
            self.registry.register_task_source(task_id, source)

        # 7. Connect fire sources to the registry
        self.keyboard_source = KeyboardFireSource()
        self.keyboard_source.connect_registry(self.registry)

    def reload_config(self) -> None:
        """Reload the actions config from disk and update the registry."""
        self.config = load_actions_config()
        self.registry.config = self.config
        log.info("Reloaded actions config")

    def reload_tasks(self) -> None:
        """Reload task files from disk and register them with the registry."""
        for name, source in load_task_files().items():
            self._task_sources[name] = source
            self.registry.register_task_source(name, source)
        log.info("Reloaded task files")

    def reload_helpers(self) -> None:
        """Reload helper files from disk. Note: helpers are injected at context
        creation time, so changes take effect on the next execution."""
        # Clear existing helpers and re-register
        self.engine._helpers.clear()
        for name, source in load_helper_files().items():
            self.engine.register_helper(source)
        # Re-inject task sources as helpers too
        for name, source in self._task_sources.items():
            self.engine.register_helper(source)
        log.info("Reloaded helper files")

    def reload_all(self) -> None:
        """Reload config, tasks, and helpers."""
        self.reload_config()
        self.reload_tasks()
        self.reload_helpers()