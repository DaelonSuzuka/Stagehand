"""Trigger registry: matches fire events to actions and executes tasks.

All trigger sources (keyboard, device, etc.) distill their events down to
a fire event dict and call registry.on_fire(event). The registry matches
against the loaded action config, checks filters, and executes the task
through the Roadie engine.
"""

from __future__ import annotations

import logging
from typing import Any, Callable

from stagehand.config import (
    ActionConfig,
    ActionsConfig,
    FilterConfig,
    TaskRef,
    TriggerConfig,
    load_actions_config,
)
from stagehand.roadie import Engine

log = logging.getLogger(__name__)


class TriggerRegistry:
    """Matches fire events to actions from the config and executes tasks.

    Usage:
        engine = Engine()
        # ... register services ...

        registry = TriggerRegistry(engine, load_actions_config())

        # Trigger sources call this:
        registry.on_fire({'type': 'keyboard', 'key': 'ctrl+shift+l'})
    """

    def __init__(self, engine: Engine, config: ActionsConfig):
        self.engine = engine
        self.config = config
        self._task_sources: dict[str, str] = {}  # task_id -> JS source
        self._filter_checkers: dict[str, Callable] = {}  # filter_type -> checker function
        self._on_action_callbacks: list[Callable] = []

    def register_filter_checker(self, filter_type: str, checker: Callable) -> None:
        """Register a filter checker function.

        Args:
            filter_type: The filter type name (e.g., 'active_window').
            checker: A callable(filter_params, fire_event) -> bool.
        """
        self._filter_checkers[filter_type] = checker

    def register_task_source(self, task_id: str, source: str) -> None:
        """Register a JS source for a task ID.

        This is used for task library files that define tasks via
        stagehand.register({id: "obs.switchScene", ...}).
        """
        self._task_sources[task_id] = source

    def on_action(self, callback: Callable[[ActionConfig], None]) -> None:
        """Register a callback invoked when an action is about to execute.

        Useful for UI feedback (highlighting the action, logging, etc.)
        """
        self._on_action_callbacks.append(callback)

    def reload_config(self) -> None:
        """Reload the actions config from disk."""
        self.config = load_actions_config()

    def on_fire(self, event: dict) -> None:
        """Match a fire event against all actions and execute matching tasks.

        Args:
            event: A fire event dict, e.g.,
                {'type': 'keyboard', 'key': 'ctrl+shift+l'}
                {'type': 'device', 'name': 'stomp4', 'pedal': 1}
                {'type': 'startup'}

        Any trigger in an action's trigger list matching the event
        (OR logic — any match fires the action) causes the action to
        execute, provided its filters pass (AND logic).
        """
        for page in self.config.pages.values():
            for action in page.actions:
                if not action.enabled:
                    continue
                if not action.triggers:
                    continue

                # OR logic: any trigger matching fires the action
                matched = any(t.matches(event) for t in action.triggers)
                if not matched:
                    continue

                # AND logic: all filters must pass
                if not self._check_filters(action.filters, event):
                    continue

                # Notify callbacks
                for cb in self._on_action_callbacks:
                    cb(action)

                # Execute the task
                self._execute_task(action.task, event)

    def _check_filters(self, filters: list[FilterConfig], event: dict) -> bool:
        """Check all filters (AND logic). Return True if all pass."""
        for f in filters:
            checker = self._filter_checkers.get(f.type)
            if checker is None:
                # No registered checker — log and skip (permissive default)
                log.debug(f"No filter checker registered for '{f.type}', skipping filter")
                continue
            if not checker(f.params, event):
                return False
        return True

    def _execute_task(self, task: TaskRef | None, event: dict) -> None:
        """Execute a task through the engine.

        For named tasks (e.g., obs.switchScene), look up the JS source
        from registered task files and evaluate it.

        For inline JS (stagehand.js), evaluate the body directly.
        """
        if task is None:
            log.warning("Action fired but no task defined")
            return

        if task.is_inline:
            # Inline JS — evaluate the body directly
            code = task.inline_code or ''
            if not code.strip():
                return
            result = self.engine.execute(code)
            if not result.ok:
                log.error(f"Inline task error: {result.error}")
            return

        # Named task — look up the source
        source = self._task_sources.get(task.task_id)
        if source is None:
            log.error(f"Unknown task: {task.task_id}")
            return

        # If the task has params, inject them as a variable and wrap the call
        if task.params:
            params_json = __import__('json').dumps(task.params)
            wrapped = f"var _params = {params_json};\n{source}"
        else:
            wrapped = source

        result = self.engine.execute(wrapped)
        if not result.ok:
            log.error(f"Task '{task.task_id}' error: {result.error}")