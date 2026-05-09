"""Config-centric action system.

The config files are the source of truth:
  config/actions.yaml  — trigger wiring (data: when to do it)
  config/tasks/*.js     — task library (code: what to do)
  config/helpers/*.js   — helper functions (shared utilities)

Everything follows the type: {params} pattern — triggers, tasks, and filters.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from qtstrap import OPTIONS


def config_dir() -> Path:
    """Return the config directory, creating it if needed."""
    d = OPTIONS.config_dir / 'config'
    d.mkdir(parents=True, exist_ok=True)
    return d


def tasks_dir() -> Path:
    """Return the tasks directory, creating it if needed."""
    d = config_dir() / 'tasks'
    d.mkdir(parents=True, exist_ok=True)
    return d


def helpers_dir() -> Path:
    """Return the helpers directory, creating it if needed."""
    d = config_dir() / 'helpers'
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class TriggerConfig:
    """A trigger definition: type + params.

    Examples:
        TriggerConfig(type='keyboard', params={'key': 'ctrl+shift+l'})
        TriggerConfig(type='device', params={'name': 'stomp4', 'pedal': 1})
        TriggerConfig(type='startup', params={'delay': 2000})
    """

    type: str
    params: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> TriggerConfig:
        """Parse a type: {params} dict into a TriggerConfig.

        Handles both formats:
            {'keyboard': {'key': 'ctrl+shift+l'}}  -> type='keyboard', params={...}
            {'keyboard': None}                      -> type='keyboard', params={}
        """
        assert len(data) == 1, f"Trigger must have exactly one key, got: {data}"
        trigger_type, params = next(iter(data.items()))
        if params is None:
            params = {}
        return cls(type=trigger_type, params=params)

    def to_dict(self) -> dict:
        """Serialize back to type: {params} format."""
        if self.params:
            return {self.type: self.params}
        return {self.type: None}

    def matches(self, fire_event: dict) -> bool:
        """Check if this trigger matches a fire event.

        A trigger matches if its type matches and all params are present
        and equal in the fire event.
        """
        if self.type != fire_event.get('type'):
            return False
        for key, value in self.params.items():
            if fire_event.get(key) != value:
                return False
        return True


@dataclass
class FilterConfig:
    """A filter definition: type + params (or type + scalar value).

    Examples:
        FilterConfig(type='active_window', params={'window': 'OBS'})
        FilterConfig(type='active_window', params='OBS')  # scalar shorthand
    """

    type: str
    params: Any = None  # dict or scalar

    @classmethod
    def from_dict(cls, data) -> FilterConfig:
        """Parse a filter definition.

        Handles formats:
            {'active_window': 'OBS'}     -> type='active_window', params='OBS'
            {'active_window': {'window': 'OBS'}}  -> type='active_window', params={...}
        """
        if isinstance(data, str):
            # Bare string filter like 'active_window: OBS' in YAML becomes just a string
            return cls(type=data, params=None)

        assert len(data) == 1, f"Filter must have exactly one key, got: {data}"
        filter_type, params = next(iter(data.items()))
        return cls(type=filter_type, params=params)

    def to_dict(self) -> dict:
        """Serialize back."""
        return {self.type: self.params}


@dataclass
class TaskRef:
    """A task reference: either a named task ID + params, or inline JS.

    Examples:
        TaskRef(task_id='obs.switchScene', params={'scene': 'Live'})
        TaskRef(task_id='stagehand.js', params={'body': 'stagehand.print("hi")'})
    """

    task_id: str
    params: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> TaskRef:
        """Parse a task: {task_id: params} dict.

        Handles:
            {'obs.switchScene': {'scene': 'Live'}}  -> task_id='obs.switchScene', params={...}
            {'obs.switchScene': None}                -> task_id='obs.switchScene', params={}
        """
        assert len(data) == 1, f"Task must have exactly one key, got: {data}"
        task_id, params = next(iter(data.items()))
        if params is None:
            params = {}
        return cls(task_id=task_id, params=params)

    def to_dict(self) -> dict:
        """Serialize back to {task_id: params} format."""
        if self.params:
            return {self.task_id: self.params}
        return {self.task_id: None}

    @property
    def is_inline(self) -> bool:
        """True if this is an inline JS task (not a named task reference)."""
        return self.task_id == 'stagehand.js'

    @property
    def inline_code(self) -> str | None:
        """Return the inline JS code if this is an inline task, else None."""
        if not self.is_inline:
            return None
        return self.params.get('body', '')


@dataclass
class ActionConfig:
    """A complete action: name + triggers + task + filters.

    This is the unit that the TriggerRegistry matches against fire events.
    """

    name: str = ''
    enabled: bool = True
    triggers: list[TriggerConfig] = field(default_factory=list)
    task: TaskRef | None = None
    filters: list[FilterConfig] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> ActionConfig:
        """Parse an action from YAML dict."""
        triggers = [
            TriggerConfig.from_dict(t) for t in data.get('triggers', [])
        ]
        filters = [
            FilterConfig.from_dict(f) for f in data.get('filters', [])
        ]
        task = None
        if 'task' in data:
            task = TaskRef.from_dict(data['task'])
        return cls(
            name=data.get('name', ''),
            enabled=data.get('enabled', True),
            triggers=triggers,
            task=task,
            filters=filters,
        )

    def to_dict(self) -> dict:
        """Serialize back to YAML-compatible dict."""
        result = {'name': self.name, 'enabled': self.enabled}
        if self.triggers:
            result['triggers'] = [t.to_dict() for t in self.triggers]
        if self.task:
            result['task'] = self.task.to_dict()
        if self.filters:
            result['filters'] = [f.to_dict() for f in self.filters]
        return result


@dataclass
class PageConfig:
    """A page of actions."""

    name: str = ''
    actions: list[ActionConfig] = field(default_factory=list)

    @classmethod
    def from_dict(cls, name: str, data: dict) -> PageConfig:
        """Parse a page from YAML dict."""
        actions = [
            ActionConfig.from_dict(a) for a in data.get('actions', [])
        ]
        return cls(name=name, actions=actions)

    def to_dict(self) -> dict:
        """Serialize back."""
        return {'actions': [a.to_dict() for a in self.actions]}


@dataclass
class ActionsConfig:
    """Top-level config: pages of actions."""

    pages: dict[str, PageConfig] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> ActionsConfig:
        """Parse from the full YAML structure."""
        pages = {}
        for name, page_data in data.get('pages', {}).items():
            pages[name] = PageConfig.from_dict(name, page_data)
        return cls(pages=pages)

    def to_dict(self) -> dict:
        """Serialize back."""
        return {'pages': {name: page.to_dict() for name, page in self.pages.items()}}


# ---------------------------------------------------------------------------
# Config file I/O
# ---------------------------------------------------------------------------

ACTIONS_FILE = 'actions.yaml'


def load_actions_config(config_path: Path | None = None) -> ActionsConfig:
    """Load actions from config/actions.yaml. Returns empty config if file doesn't exist."""
    if config_path is None:
        config_path = config_dir() / ACTIONS_FILE

    if not config_path.exists():
        return ActionsConfig()

    with open(config_path, 'r') as f:
        data = yaml.safe_load(f)

    if not data:
        return ActionsConfig()

    return ActionsConfig.from_dict(data)


def save_actions_config(config: ActionsConfig, config_path: Path | None = None) -> None:
    """Save actions config to config/actions.yaml."""
    if config_path is None:
        config_path = config_dir() / ACTIONS_FILE

    config_path.parent.mkdir(parents=True, exist_ok=True)

    data = config.to_dict()

    with open(config_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def load_task_files(tasks_path: Path | None = None) -> dict[str, str]:
    """Load all JS task files from config/tasks/. Returns {task_id: source_code}."""
    tasks = {}
    if tasks_path is None:
        tasks_path = tasks_dir()
    if not tasks_path.exists():
        return tasks
    for path in sorted(tasks_path.glob('*.js')):
        source = path.read_text()
        # The task_id comes from stagehand.register() calls in the file.
        # We return filename -> source for the engine to evaluate.
        tasks[path.stem] = source
    return tasks


def load_helper_files(helpers_path: Path | None = None) -> dict[str, str]:
    """Load all JS helper files from config/helpers/. Returns {name: source_code}."""
    helpers = {}
    if helpers_path is None:
        helpers_path = helpers_dir()
    if not helpers_path.exists():
        return helpers
    for path in sorted(helpers_path.glob('*.js')):
        source = path.read_text()
        helpers[path.stem] = source
    return helpers


# ---------------------------------------------------------------------------
# Default config seed
# ---------------------------------------------------------------------------

DEFAULT_CONFIG = {
    'pages': {
        'Page 1': {
            'actions': [
                {
                    'name': 'Hello World',
                    'enabled': True,
                    'triggers': [
                        {'keyboard': {'key': 'ctrl+shift+h'}},
                    ],
                    'task': {'stagehand.js': {'body': 'stagehand.print("Hello, world!")'}},
                },
            ],
        },
    },
}


def ensure_default_config() -> None:
    """Create a default actions.yaml if none exists."""
    path = config_dir() / ACTIONS_FILE
    if not path.exists():
        save_actions_config(ActionsConfig.from_dict(DEFAULT_CONFIG))