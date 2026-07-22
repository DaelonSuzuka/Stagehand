"""Tests for the canonical key vocabulary and its adapters."""

import sys

import pytest
from pynput.keyboard import Key, KeyCode

from stagehand import keys


class TestResolve:
    def test_canonical_names_resolve_to_themselves(self):
        for name in keys.names():
            assert keys.resolve(name) == name

    def test_aliases(self):
        assert keys.resolve('cmd') == 'super'
        assert keys.resolve('win') == 'super'
        assert keys.resolve('escape') == 'esc'
        assert keys.resolve('return') == 'enter'
        assert keys.resolve('Ctrl') == 'ctrl'

    def test_bare_chars_are_valid(self):
        assert keys.resolve('é') == 'é'

    def test_unknown_names_are_none(self):
        assert keys.resolve('flux_capacitor') is None


class TestCombos:
    def test_parse_orders_modifiers_first(self):
        assert keys.parse_combo('l+shift+ctrl') == ['ctrl', 'shift', 'l']

    def test_parse_single_key(self):
        assert keys.parse_combo('f13') == ['f13']

    def test_parse_resolves_aliases(self):
        assert keys.parse_combo('cmd+return') == ['super', 'enter']

    def test_parse_dedupes(self):
        assert keys.parse_combo('ctrl+ctrl+a') == ['ctrl', 'a']

    def test_parse_rejects_unknown(self):
        with pytest.raises(ValueError):
            keys.parse_combo('ctrl+flux_capacitor')

    def test_normalize_round_trip(self):
        assert keys.normalize_combo('SHIFT+Ctrl+L') == 'ctrl+shift+l'


class TestPynputAdapters:
    def test_named_keys(self):
        assert keys.to_pynput('ctrl') is Key.ctrl
        assert keys.to_pynput('space') is Key.space
        assert keys.to_pynput('f13') is Key.f13

    def test_super_maps_to_cmd(self):
        assert keys.to_pynput('super') is Key.cmd

    def test_chars_pass_through(self):
        assert keys.to_pynput('a') == 'a'

    def test_driver_tier_only_keys_are_none(self):
        assert keys.to_pynput('f21') is None
        assert keys.to_pynput('kp_5') is None

    def test_normalize_strips_variants(self):
        assert keys.normalize_pynput(Key.ctrl_l) == 'ctrl'
        assert keys.normalize_pynput(Key.shift_r) == 'shift'
        assert keys.normalize_pynput(Key.alt_gr) == 'alt'

    def test_normalize_cmd_is_super(self):
        assert keys.normalize_pynput(Key.cmd) == 'super'
        assert keys.normalize_pynput(Key.cmd_l) == 'super'

    def test_normalize_keycode(self):
        assert keys.normalize_pynput(KeyCode.from_char('a')) == 'a'

    def test_normalize_round_trips_through_canonical(self):
        # every canonical name pynput can send must normalize back to itself
        for name in keys.names():
            key = keys.to_pynput(name)
            if key is not None:
                assert keys.normalize_pynput(key if isinstance(key, Key) else KeyCode.from_char(key)) == name


class TestEvdevAdapter:
    def test_every_table_entry_has_evdev_name(self):
        for name in keys.names():
            assert keys.to_evdev(name) is not None

    def test_untabled_chars_have_no_evdev(self):
        assert keys.to_evdev('é') is None

    @pytest.mark.skipif(sys.platform != 'linux', reason='evdev is linux-only')
    def test_evdev_names_are_real(self):
        from evdev import ecodes

        for name, evdev_name in keys.KEYS.items():
            assert evdev_name in ecodes.ecodes, f'{name} -> {evdev_name} not in ecodes'


class TestHotkeySpec:
    def test_named_keys_get_brackets(self):
        assert keys.to_hotkey_spec('ctrl+shift+l') == '<ctrl>+<shift>+l'

    def test_super_uses_pynput_name(self):
        assert keys.to_hotkey_spec('super+x') == '<cmd>+x'

    def test_driver_only_keys_raise(self):
        with pytest.raises(ValueError):
            keys.to_hotkey_spec('ctrl+f21')
