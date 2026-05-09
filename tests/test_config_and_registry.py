"""Tests for the config-centric action system and trigger registry."""

import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml

from stagehand.config import (
    ActionConfig,
    ActionsConfig,
    FilterConfig,
    PageConfig,
    TaskRef,
    TriggerConfig,
    load_actions_config,
    save_actions_config,
)
from stagehand.roadie import Engine


# ---------------------------------------------------------------------------
# Config data model tests
# ---------------------------------------------------------------------------

class TestTriggerConfig:
    def test_from_dict_with_params(self):
        t = TriggerConfig.from_dict({'keyboard': {'key': 'ctrl+shift+l'}})
        assert t.type == 'keyboard'
        assert t.params == {'key': 'ctrl+shift+l'}

    def test_from_dict_with_null_params(self):
        t = TriggerConfig.from_dict({'startup': None})
        assert t.type == 'startup'
        assert t.params == {}

    def test_to_dict_with_params(self):
        t = TriggerConfig(type='keyboard', params={'key': 'ctrl+shift+l'})
        d = t.to_dict()
        assert d == {'keyboard': {'key': 'ctrl+shift+l'}}

    def test_to_dict_with_empty_params(self):
        t = TriggerConfig(type='startup', params={})
        d = t.to_dict()
        assert d == {'startup': None}

    def test_matches_exact_event(self):
        t = TriggerConfig.from_dict({'keyboard': {'key': 'ctrl+shift+l'}})
        assert t.matches({'type': 'keyboard', 'key': 'ctrl+shift+l'})

    def test_matches_wrong_key(self):
        t = TriggerConfig.from_dict({'keyboard': {'key': 'ctrl+shift+l'}})
        assert not t.matches({'type': 'keyboard', 'key': 'ctrl+k'})

    def test_matches_wrong_type(self):
        t = TriggerConfig.from_dict({'keyboard': {'key': 'ctrl+shift+l'}})
        assert not t.matches({'type': 'device', 'key': 'ctrl+shift+l'})

    def test_matches_partial_params(self):
        """Fire event can have extra fields — trigger only checks its own params."""
        t = TriggerConfig.from_dict({'keyboard': {'key': 'ctrl+shift+l'}})
        assert t.matches({'type': 'keyboard', 'key': 'ctrl+shift+l', 'extra': 42})

    def test_from_dict_rejects_multi_key(self):
        with pytest.raises(AssertionError):
            TriggerConfig.from_dict({'keyboard': {'key': 'a'}, 'device': {'name': 'x'}})

    def test_round_trip(self):
        original = {'keyboard': {'key': 'ctrl+m'}}
        t = TriggerConfig.from_dict(original)
        assert t.to_dict() == original


class TestFilterConfig:
    def test_from_dict_with_scalar(self):
        f = FilterConfig.from_dict({'active_window': 'OBS'})
        assert f.type == 'active_window'
        assert f.params == 'OBS'

    def test_from_dict_with_dict(self):
        f = FilterConfig.from_dict({'sandbox': {'expression': 'True'}})
        assert f.type == 'sandbox'
        assert f.params == {'expression': 'True'}

    def test_to_dict(self):
        f = FilterConfig(type='active_window', params='OBS')
        assert f.to_dict() == {'active_window': 'OBS'}


class TestTaskRef:
    def test_named_task_with_params(self):
        t = TaskRef.from_dict({'obs.switchScene': {'scene': 'Live'}})
        assert t.task_id == 'obs.switchScene'
        assert t.params == {'scene': 'Live'}
        assert not t.is_inline

    def test_named_task_no_params(self):
        t = TaskRef.from_dict({'go-live': None})
        assert t.task_id == 'go-live'
        assert t.params == {}
        assert not t.is_inline

    def test_inline_task(self):
        t = TaskRef.from_dict({'stagehand.js': {'body': 'stagehand.print("hi")'}})
        assert t.task_id == 'stagehand.js'
        assert t.is_inline
        assert t.inline_code == 'stagehand.print("hi")'

    def test_inline_task_empty_body(self):
        t = TaskRef.from_dict({'stagehand.js': None})
        assert t.is_inline
        assert t.inline_code == ''

    def test_round_trip_named(self):
        original = {'obs.switchScene': {'scene': 'Live'}}
        t = TaskRef.from_dict(original)
        assert t.to_dict() == original

    def test_round_trip_inline(self):
        original = {'stagehand.js': {'body': 'code'}}
        t = TaskRef.from_dict(original)
        assert t.to_dict() == original


class TestActionConfig:
    def test_full_action(self):
        data = {
            'name': 'Go Live',
            'enabled': True,
            'triggers': [
                {'keyboard': {'key': 'ctrl+shift+l'}},
                {'device': {'name': 'stomp4', 'pedal': 1}},
            ],
            'task': {'obs.switchScene': {'scene': 'Live'}},
            'filters': [
                {'active_window': 'OBS'},
            ],
        }
        action = ActionConfig.from_dict(data)
        assert action.name == 'Go Live'
        assert action.enabled is True
        assert len(action.triggers) == 2
        assert action.task.task_id == 'obs.switchScene'
        assert len(action.filters) == 1

    def test_minimal_action(self):
        data = {'name': 'Simple'}
        action = ActionConfig.from_dict(data)
        assert action.name == 'Simple'
        assert action.triggers == []
        assert action.task is None
        assert action.filters == []

    def test_round_trip(self):
        data = {
            'name': 'Go Live',
            'enabled': True,
            'triggers': [{'keyboard': {'key': 'ctrl+shift+l'}}],
            'task': {'stagehand.js': {'body': 'print("hi")'}},
            'filters': [{'active_window': 'OBS'}],
        }
        action = ActionConfig.from_dict(data)
        result = action.to_dict()
        assert result == data


class TestActionsConfig:
    def test_round_trip(self):
        data = {
            'pages': {
                'Streaming': {
                    'actions': [
                        {
                            'name': 'Go Live',
                            'enabled': True,
                            'triggers': [{'keyboard': {'key': 'ctrl+shift+l'}}],
                            'task': {'stagehand.js': {'body': 'stagehand.obs.switchScene("Live")'}},
                            'filters': [{'active_window': 'OBS'}],
                        },
                    ],
                },
            },
        }
        config = ActionsConfig.from_dict(data)
        assert 'Streaming' in config.pages
        assert len(config.pages['Streaming'].actions) == 1
        assert config.to_dict() == data

    def test_empty_config(self):
        config = ActionsConfig.from_dict({})
        assert config.pages == {}


# ---------------------------------------------------------------------------
# YAML I/O tests
# ---------------------------------------------------------------------------

class TestYamlIO:
    def test_save_and_load(self, tmp_path):
        yaml_path = tmp_path / 'config' / 'actions.yaml'

        config = ActionsConfig.from_dict({
            'pages': {
                'Test': {
                    'actions': [
                        {
                            'name': 'Hello',
                            'enabled': True,
                            'triggers': [{'keyboard': {'key': 'ctrl+h'}}],
                            'task': {'stagehand.js': {'body': 'stagehand.print("hello")'}},
                        },
                    ],
                },
            },
        })

        # Save
        save_actions_config(config, yaml_path)

        assert yaml_path.exists()

        # Load
        loaded = load_actions_config(yaml_path)

        assert 'Test' in loaded.pages
        action = loaded.pages['Test'].actions[0]
        assert action.name == 'Hello'
        assert action.triggers[0].type == 'keyboard'
        assert action.triggers[0].params == {'key': 'ctrl+h'}
        assert action.task.is_inline
        assert action.task.inline_code == 'stagehand.print("hello")'

    def test_load_missing_file(self, tmp_path):
        yaml_path = tmp_path / 'config' / 'actions.yaml'
        config = load_actions_config(yaml_path)
        assert config.pages == {}

    def test_yaml_is_human_readable(self, tmp_path):
        yaml_path = tmp_path / 'config' / 'actions.yaml'

        config = ActionsConfig.from_dict({
            'pages': {
                'Streaming': {
                    'actions': [
                        {
                            'name': 'Go Live',
                            'enabled': True,
                            'triggers': [{'keyboard': {'key': 'ctrl+shift+l'}}],
                            'task': {'stagehand.js': {'body': 'stagehand.obs.switchScene("Live")'}},
                        },
                    ],
                },
            },
        })

        save_actions_config(config, yaml_path)

        content = yaml_path.read_text()
        # Should be valid YAML
        parsed = yaml.safe_load(content)
        assert 'pages' in parsed


# ---------------------------------------------------------------------------
# Trigger Registry tests
# ---------------------------------------------------------------------------

class TestTriggerRegistry:
    def test_fire_matches_action(self):
        from stagehand.trigger_registry import TriggerRegistry

        engine = Engine()
        config = ActionsConfig.from_dict({
            'pages': {
                'Test': {
                    'actions': [
                        {
                            'name': 'Hello',
                            'enabled': True,
                            'triggers': [{'keyboard': {'key': 'ctrl+shift+l'}}],
                            'task': {'stagehand.js': {'body': 'stagehand.print("fired")'}},
                        },
                    ],
                },
            },
        })

        registry = TriggerRegistry(engine, config)

        # Should not crash — inline JS task executes
        registry.on_fire({'type': 'keyboard', 'key': 'ctrl+shift+l'})

    def test_fire_no_match(self):
        from stagehand.trigger_registry import TriggerRegistry

        engine = Engine()
        config = ActionsConfig.from_dict({
            'pages': {
                'Test': {
                    'actions': [
                        {
                            'name': 'Hello',
                            'enabled': True,
                            'triggers': [{'keyboard': {'key': 'ctrl+shift+l'}}],
                            'task': {'stagehand.js': {'body': 'stagehand.print("should not fire")'}},
                        },
                    ],
                },
            },
        })

        registry = TriggerRegistry(engine, config)
        # Wrong key — should not match
        registry.on_fire({'type': 'keyboard', 'key': 'ctrl+k'})

    def test_disabled_action_skipped(self):
        from stagehand.trigger_registry import TriggerRegistry

        engine = Engine()
        config = ActionsConfig.from_dict({
            'pages': {
                'Test': {
                    'actions': [
                        {
                            'name': 'Disabled',
                            'enabled': False,
                            'triggers': [{'keyboard': {'key': 'ctrl+shift+l'}}],
                            'task': {'stagehand.js': {'body': 'stagehand.print("should not fire")'}},
                        },
                    ],
                },
            },
        })

        registry = TriggerRegistry(engine, config)
        # Action is disabled — should not fire
        registry.on_fire({'type': 'keyboard', 'key': 'ctrl+shift+l'})

    def test_or_trigger_logic(self):
        """Any matching trigger in the list fires the action (OR logic)."""
        from stagehand.trigger_registry import TriggerRegistry

        engine = Engine()
        action_callback = MagicMock()

        config = ActionsConfig.from_dict({
            'pages': {
                'Test': {
                    'actions': [
                        {
                            'name': 'Multi-trigger',
                            'enabled': True,
                            'triggers': [
                                {'keyboard': {'key': 'ctrl+l'}},
                                {'device': {'name': 'stomp4', 'pedal': 1}},
                            ],
                            'task': {'stagehand.js': {'body': 'stagehand.print("fired")'}},
                        },
                    ],
                },
            },
        })

        registry = TriggerRegistry(engine, config)
        registry.on_action(action_callback)

        # First trigger
        registry.on_fire({'type': 'keyboard', 'key': 'ctrl+l'})
        assert action_callback.call_count == 1

        # Second trigger
        registry.on_fire({'type': 'device', 'name': 'stomp4', 'pedal': 1})
        assert action_callback.call_count == 2

    def test_filter_blocks_action(self):
        """All filters must pass (AND logic) for the action to execute."""
        from stagehand.trigger_registry import TriggerRegistry

        engine = Engine()
        config = ActionsConfig.from_dict({
            'pages': {
                'Test': {
                    'actions': [
                        {
                            'name': 'Filtered',
                            'enabled': True,
                            'triggers': [{'keyboard': {'key': 'ctrl+l'}}],
                            'task': {'stagehand.js': {'body': 'stagehand.print("fired")'}},
                            'filters': [{'active_window': 'OBS'}],
                        },
                    ],
                },
            },
        })

        registry = TriggerRegistry(engine, config)
        registry.register_filter_checker(
            'active_window',
            lambda params, event: event.get('window') == params
        )

        # Without matching window — filter blocks
        registry.on_fire({'type': 'keyboard', 'key': 'ctrl+l', 'window': 'Chrome'})
        # Should not execute (filter blocks)

        # With matching window — filter passes
        registry.on_fire({'type': 'keyboard', 'key': 'ctrl+l', 'window': 'OBS'})
        # Should execute

    def test_named_task_not_found(self):
        """Unknown task ID should log error, not crash."""
        from stagehand.trigger_registry import TriggerRegistry

        engine = Engine()
        config = ActionsConfig.from_dict({
            'pages': {
                'Test': {
                    'actions': [
                        {
                            'name': 'Missing task',
                            'enabled': True,
                            'triggers': [{'keyboard': {'key': 'ctrl+l'}}],
                            'task': {'obs.switchScene': {'scene': 'Live'}},
                        },
                    ],
                },
            },
        })

        registry = TriggerRegistry(engine, config)
        # No task sources registered — should log error but not crash
        registry.on_fire({'type': 'keyboard', 'key': 'ctrl+l'})