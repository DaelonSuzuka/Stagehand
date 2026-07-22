"""Reusable key combo picker.

KeyPicker is a drop-in line edit (text/setText/textChanged) with a button
that opens KeyPickerDialog. The dialog offers three entry paths that all
write to one authoritative raw line:

    capture — click the box, press the combo (works for pedal-emitted keys:
              focus the box and stomp the pedal)
    manual  — modifier checkboxes + searchable key list, for keys you can't
              physically press (F13-F24, numpad on a TKL, media keys)
    raw     — the line edit itself, validated against stagehand.keys

Output is always a canonical combo spec ('ctrl+shift+f13').
"""

from qtstrap import *

from stagehand import keys


_QT_MODIFIER_KEYS = {
    Qt.Key_Control,
    Qt.Key_Shift,
    Qt.Key_Alt,
    Qt.Key_AltGr,
    Qt.Key_Meta,
    Qt.Key_Super_L,
    Qt.Key_Super_R,
}

_QT_MODIFIER_FLAGS = [
    (Qt.ControlModifier, 'ctrl'),
    (Qt.ShiftModifier, 'shift'),
    (Qt.AltModifier, 'alt'),
    (Qt.MetaModifier, 'super'),
]

_QT_NAMED = {
    Qt.Key_Escape: 'esc',
    Qt.Key_Return: 'enter',
    Qt.Key_Enter: 'kp_enter',
    Qt.Key_Tab: 'tab',
    Qt.Key_Backtab: 'tab',
    Qt.Key_Space: 'space',
    Qt.Key_Backspace: 'backspace',
    Qt.Key_Delete: 'delete',
    Qt.Key_Insert: 'insert',
    Qt.Key_Home: 'home',
    Qt.Key_End: 'end',
    Qt.Key_PageUp: 'page_up',
    Qt.Key_PageDown: 'page_down',
    Qt.Key_Up: 'up',
    Qt.Key_Down: 'down',
    Qt.Key_Left: 'left',
    Qt.Key_Right: 'right',
    Qt.Key_CapsLock: 'caps_lock',
    Qt.Key_NumLock: 'num_lock',
    Qt.Key_ScrollLock: 'scroll_lock',
    Qt.Key_Print: 'print_screen',
    Qt.Key_Pause: 'pause',
    Qt.Key_Menu: 'menu',
    Qt.Key_MediaTogglePlayPause: 'media_play_pause',
    Qt.Key_MediaPlay: 'media_play_pause',
    Qt.Key_MediaNext: 'media_next',
    Qt.Key_MediaPrevious: 'media_previous',
    Qt.Key_VolumeUp: 'media_volume_up',
    Qt.Key_VolumeDown: 'media_volume_down',
    Qt.Key_VolumeMute: 'media_volume_mute',
}


def _event_modifiers(event) -> list[str]:
    return [name for flag, name in _QT_MODIFIER_FLAGS if event.modifiers() & flag]


def _event_key_name(event) -> str | None:
    """Qt key event -> canonical key name, or None if unmappable."""
    key = event.key()
    if key in _QT_NAMED:
        return _QT_NAMED[key]
    if Qt.Key_F1 <= key <= Qt.Key_F35:
        return f'f{int(key) - int(Qt.Key_F1) + 1}'
    if 0x20 <= key <= 0x7E:
        return chr(key).lower()
    text = event.text()
    if text and text.isprintable():
        return text.lower()
    return None


class KeyCaptureButton(QPushButton):
    captured = Signal(str)

    idle_text = 'Click to capture...'

    def __init__(self, parent=None):
        super().__init__(self.idle_text, parent=parent)
        self.setCheckable(True)
        self.toggled.connect(self._on_toggled)

    def _on_toggled(self, checked):
        if checked:
            self.setText('Press a key combo...')
            self.grabKeyboard()
        else:
            self.releaseKeyboard()
            self.setText(self.idle_text)

    def _preview(self, event):
        mods = _event_modifiers(event)
        self.setText('+'.join(mods + ['...']) if mods else 'Press a key combo...')

    def keyPressEvent(self, event):
        if not self.isChecked():
            return super().keyPressEvent(event)
        if event.isAutoRepeat():
            return
        if event.key() in _QT_MODIFIER_KEYS:
            self._preview(event)
            return
        name = _event_key_name(event)
        if name is None:
            return
        combo = keys.format_combo(_event_modifiers(event) + [name])
        self.setChecked(False)
        self.captured.emit(combo)

    def keyReleaseEvent(self, event):
        if not self.isChecked():
            return super().keyReleaseEvent(event)
        if event.key() in _QT_MODIFIER_KEYS:
            self._preview(event)

    def focusOutEvent(self, event):
        self.setChecked(False)
        super().focusOutEvent(event)


class KeyPickerDialog(QDialog):
    def __init__(self, key: str = '', parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle('Select Key')

        self._syncing = False

        self.capture = KeyCaptureButton()
        self.capture.captured.connect(self.set_key)

        self.mod_checks = {m: QCheckBox(m) for m in keys.MODIFIERS}
        for check in self.mod_checks.values():
            check.toggled.connect(self._manual_changed)

        self.key_combo = QComboBox()
        self.key_combo.setEditable(True)
        self.key_combo.setInsertPolicy(QComboBox.NoInsert)
        self.key_combo.addItem('')
        self.key_combo.addItems(keys.names())
        self.key_combo.currentTextChanged.connect(self._manual_changed)

        self.raw = QLineEdit()
        self.raw.textChanged.connect(self._raw_changed)

        with CVBoxLayout(self) as layout:
            layout.add(self.capture)
            with layout.hbox() as layout:
                for check in self.mod_checks.values():
                    layout.add(check)
                layout.add(QLabel(), 1)
            with layout.form() as layout:
                layout.add('Key:', self.key_combo)
                layout.add('Raw:', self.raw)
            with layout.hbox() as layout:
                layout.add(QLabel(), 1)
                layout.add(QPushButton('Ok', clicked=self.accept, default=True))
                layout.add(QPushButton('Cancel', clicked=self.reject))

        self.set_key(key)

    def key(self) -> str:
        return self.raw.text()

    def set_key(self, combo: str):
        self.raw.setText(combo)

    def _manual_changed(self, *_):
        if self._syncing:
            return
        parts = [m for m, check in self.mod_checks.items() if check.isChecked()]
        name = keys.resolve(self.key_combo.currentText())
        if name and name not in keys.MODIFIERS:
            parts.append(name)
        self._syncing = True
        self.raw.setText(keys.format_combo(parts))
        self._syncing = False

    def _raw_changed(self, text):
        if self._syncing:
            return
        try:
            parts = keys.parse_combo(text)
        except ValueError:
            return
        self._syncing = True
        for mod, check in self.mod_checks.items():
            check.setChecked(mod in parts)
        rest = [p for p in parts if p not in keys.MODIFIERS]
        self.key_combo.setCurrentText(rest[0] if rest else '')
        self._syncing = False

    @classmethod
    def pick(cls, key: str = '', parent=None) -> str | None:
        """Open the dialog modally. Returns the combo, or None on cancel."""
        dialog = cls(key, parent)
        if dialog.exec():
            return dialog.key()
        return None


class KeyPicker(QWidget):
    """Line edit + picker button. Drop-in for a QLineEdit holding a key spec."""

    textChanged = Signal(str)

    def __init__(self, text: str = '', parent=None):
        super().__init__(parent=parent)

        self._dialog_open = False

        self.edit = QLineEdit(text)
        self.edit.textChanged.connect(self.textChanged)

        self.button = QToolButton(text='…', clicked=self._pick)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.edit, 1)
            layout.add(self.button)

    def text(self) -> str:
        return self.edit.text()

    def setText(self, text: str):
        self.edit.setText(text)

    def hasFocus(self) -> bool:
        return self.edit.hasFocus() or self._dialog_open

    def _pick(self):
        self._dialog_open = True
        try:
            result = KeyPickerDialog.pick(self.edit.text(), self)
        finally:
            self._dialog_open = False
        if result is not None:
            self.edit.setText(result)
