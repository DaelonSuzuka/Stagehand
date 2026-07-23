"""Offer and perform driver-tier keyboard output setup (Linux/uinput).

The dialog is reachable three ways: an automatic one-time offer at startup
(when the diagnosis says setup would fix things), a settings menu entry,
and the command palette. Setup runs ENABLE_SCRIPT via pkexec (polkit GUI
auth) — every step is idempotent, so manual reruns are always safe.

Works without a live KeyboardService (the action pipeline isn't wired into
the app yet); pass one to get live backend hot-swap after setup succeeds.
"""

from qtstrap import *

from stagehand.services.keyboard_service import ENABLE_SCRIPT, OFFERABLE, diagnose_uinput


EXPLANATION = (
    'Keyboard output is running in compatibility mode. Keys sent by Stagehand '
    'are invisible to programs that read input at the hardware level — games, '
    "TeamSpeak's default hotkey mode, and most native Wayland apps.\n\n"
    'Full-fidelity output uses a virtual keyboard device (uinput), which needs '
    'a one-time system change: a udev rule granting you access to /dev/uinput. '
    'Stagehand can install it now — your admin password will be requested once.'
)

STATUS = {
    'ok': 'Driver-tier output is available.',
    'unsupported': 'Not applicable on this platform.',
    'no_evdev': "python-evdev isn't installed — reinstall dependencies.",
    'no_node': '/dev/uinput does not exist — the uinput kernel module is not loaded.',
    'no_permission': 'No permission on /dev/uinput — the udev rule is not installed.',
}


class UinputSetupDialog(QDialog):
    def __init__(self, service=None, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle('Keyboard Output Setup')

        self.service = service
        self.proc = None

        explanation = QLabel(EXPLANATION)
        explanation.setWordWrap(True)

        self.status = QLabel()
        self.enable_btn = QPushButton('Enable', clicked=self.run_enable)
        self.dont_ask_btn = QPushButton("Don't ask again", clicked=self.dont_ask)

        with CVBoxLayout(self) as layout:
            layout.add(explanation)
            layout.add(self.status)
            with layout.hbox() as layout:
                layout.add(QLabel(), 1)
                layout.add(self.enable_btn)
                layout.add(QPushButton('Not now', clicked=self.reject))
                layout.add(self.dont_ask_btn)

        self.setMinimumWidth(450)
        self.refresh()

    def refresh(self):
        if self.service is not None and self.service.backend.tier == 'driver':
            diagnosis = 'ok'
        else:
            diagnosis = diagnose_uinput()
        self.status.setText(STATUS.get(diagnosis, diagnosis))
        self.enable_btn.setEnabled(diagnosis in OFFERABLE)

    def open_manual(self):
        """Open from the menu / command palette: no nag-suppression button."""
        self.dont_ask_btn.hide()
        self.refresh()
        self.open()

    def maybe_offer(self):
        """One-time startup offer, gated by diagnosis and settings."""
        if QSettings().value('uinput_setup/dont_ask', False, type=bool):
            return
        if diagnose_uinput() not in OFFERABLE:
            return
        self.dont_ask_btn.show()
        self.refresh()
        self.open()

    def dont_ask(self):
        QSettings().setValue('uinput_setup/dont_ask', True)
        self.reject()

    def run_enable(self):
        self.enable_btn.setEnabled(False)
        self.status.setText('Waiting for authorization...')

        self.proc = QProcess(self)
        self.proc.finished.connect(self.on_finished)
        self.proc.errorOccurred.connect(self.on_error)
        self.proc.start('pkexec', ['sh', '-c', ENABLE_SCRIPT])

    def on_finished(self, code, _status):
        if code == 0:
            if self.service is not None:
                active = self.service.retry_backend()
            else:
                active = diagnose_uinput() == 'ok'
            if active:
                self.status.setText('Driver-tier output enabled.')
            else:
                self.refresh()
        elif code in (126, 127):  # pkexec: dialog dismissed / not authorized
            self.status.setText('Authorization cancelled.')
            self.enable_btn.setEnabled(True)
        else:
            stderr = bytes(self.proc.readAllStandardError()).decode(errors='replace').strip()
            self.status.setText(f'Setup failed (exit {code}): {stderr}')
            self.enable_btn.setEnabled(True)

    def on_error(self, error):
        if error == QProcess.FailedToStart:
            self.status.setText('pkexec not found — install polkit or run the setup manually.')
            self.enable_btn.setEnabled(True)
