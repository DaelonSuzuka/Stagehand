from qtstrap import *
import numpy as np
import sounddevice as sd
from time import time
import os
from stagehand.sandbox import Sandbox
from stagehand.components import StagehandWidget


class MicStream:
    def __init__(self, device=None):
        self.amplitude = 0
        self.volume = 0
        self.gain = 50
        self.beta = 0.2
        self.stream = None
        if device:
            self.device_id = device
            self.device = sd.query_devices(device)
            self.name = self.device['name']

    def set_gain(self, gain):
        try:
            self.gain = float(gain)
        except ValueError:
            pass

    def set_beta(self, beta):
        self.beta = float(beta)

    def start(self, device=None):
        if device is None:
            device = self.device_id
        self.stream = sd.InputStream(device=device)
        self.stream.start()

    def process_audio(self):
        buffer, _ = self.stream.read(self.stream.read_available)

        # sometimes buffer is empty
        if len(buffer) == 0:
            return

        # calculate RMS
        raw = np.sqrt(np.mean(np.power(buffer.flat, 2)))
        # IIR low pass filter
        self.amplitude = self.amplitude - (self.beta * self.amplitude - raw)
        # convert to integer
        self.volume = min(int(self.amplitude * self.gain), 30)
        return self.volume


class MicStreamWidget(QWidget):
    def __init__(self, device, parent=None):
        super().__init__(parent=parent)

        self.stream = MicStream(device)

        self.device = sd.query_devices(device)
        self.name = self.device['name']

        self.title = QLabel(self.name)
        self.title.setFixedWidth(250)
        self.title.setToolTip(self.name)
        self.enabled = PersistentCheckBox(f'mic_voter/{self.name}/enabled', changed=self.on_check)
        self.obs_name = PersistentLineEdit(f'mic_voter/{self.name}/obs_name')
        self.meter = QLabel()
        self.preferred = PersistentCheckBox(f'mic_voter/{self.name}/preferred')

        self.gain = PersistentLineEdit(f'mic_voter/{self.name}/gain', changed=self.stream.set_gain, default=str(self.stream.gain))
        self.gain.setFixedWidth(40)
        self.beta = PersistentLineEdit(f'mic_voter/{self.name}/beta', changed=self.stream.set_beta, default=str(self.stream.beta))
        self.beta.setFixedWidth(40)

        self.on_check()

    def on_check(self):
        if self.enabled.checkState() == Qt.Checked:
            self.title.setEnabled(True)
            self.stream.start()
        else:
            self.title.setEnabled(False)
            # self.stream.stop()
            self.meter.setText('')


class MicVoterWidget(StagehandWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, icon_name='fa5s.microphone', **kwargs)

        self.best_mic = QLabel()

        self.default_host_api = 0
        if os.name == 'nt':
            self.default_host_api = 3

        self.mics = {}

        self.enabled = PersistentCheckBox('mic_voter/enabled', changed=self.set_enabled)

        self.timer = QTimer()
        self.timer.timeout.connect(self.process_audio)
        # self.timer.start(20)

        self.last_changed_time = time()
        self.rate_limit = PersistentLineEdit('mic_voter/rate_limit', default='1')
        self.change_threshold = PersistentLineEdit('mic_voter/change_threshold', default='5')

        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Best Mic:'))
                layout.add(self.best_mic)
                layout.add(QLabel(), 1)
            layout.add(QLabel())
            with layout.hbox():
                layout.add(QLabel('Switch Threshold:'))
                layout.add(self.change_threshold)
                layout.add(QLabel('Rate Limit:'))
                layout.add(self.rate_limit)
                layout.add(QLabel(), 1)
                layout.add(QLabel('Voter Enabled:'))
                layout.add(self.enabled)
            layout.add(QLabel())

            with layout.grid() as layout:
                self.grid = layout._layout
                layout.setColumnStretch(1, 1)
                layout.add(QLabel('Title'), 0, 0)
                layout.add(QLabel('Meter'), 0, 1)
                layout.add(QLabel('Beta'), 0, 3)
                layout.add(QLabel('Gain'), 0, 4)
                layout.add(QLabel('OBS Name'), 0, 5)
                layout.add(QLabel('Enabled'), 0, 6)
                layout.add(HLine(), 1, 0, 1, 8)

                if self.enabled:
                    self.create_devices()
                
            layout.add(QLabel(), 1)

    def create_devices(self):
        for i, d in enumerate(sd.query_devices()):
            if d['hostapi'] == self.default_host_api and d['max_input_channels'] > 0:
                self.mics[i] = MicStreamWidget(i)

        for i, mic in enumerate(self.mics.values()):
            self.grid.add(mic.title, i + 2, 0)
            self.grid.add(mic.meter, i + 2, 1)
            self.grid.add(mic.beta, i + 2, 3)
            self.grid.add(mic.gain, i + 2, 4)
            self.grid.add(mic.obs_name, i + 2, 5)
            self.grid.add(mic.enabled, i + 2, 6)
    
        self.timer.start(20)

    def remove_devices(self):
        self.timer.stop()

        for i, mic in enumerate(self.mics.values()):
            self.grid.removeWidget(mic.title)
            mic.title.hide()
            self.grid.removeWidget(mic.meter)
            mic.meter.hide()
            self.grid.removeWidget(mic.beta)
            mic.beta.hide()
            self.grid.removeWidget(mic.gain)
            mic.gain.hide()
            self.grid.removeWidget(mic.obs_name)
            mic.obs_name.hide()
            self.grid.removeWidget(mic.enabled)
            mic.enabled.hide()
            mic.deleteLater()

        self.mics.clear()

    def set_enabled(self, value):
        if self.enabled:
            self.create_devices()
        else:
            self.remove_devices()

    def process_audio(self):
        volumes = {}
        for key, mic in self.mics.items():
            if mic.enabled.checkState() == Qt.Checked:
                volume = mic.stream.process_audio()
                if volume is None:
                    volume = 0
                volumes[key] = volume
                mic.meter.setText(str(volume) + ' ' + '|' * volume)

        sorted_keys = [k for k in reversed(sorted(volumes, key=volumes.get))]
        if len(sorted_keys) == 0:
            return
        best_mic = self.mics[sorted_keys[0]]
        
        need_to_change = False
        for _, vol in volumes.items():
            try:
                if vol > float(self.change_threshold.text()):
                    need_to_change = True
            except ValueError:
                return

        if not need_to_change:
            return

        if (rate_limit_period := self.rate_limit.text()) == '':
            rate_limit_period = 5
        if (time() - self.last_changed_time) < float(rate_limit_period):
            return
        self.last_changed_time = time()

        if best_mic.name != self.best_mic.text():
            mute = {}
            for key in sorted_keys:
                obs_name = self.mics[key].obs_name.text()
                if obs_name:
                    mute[obs_name] = True
                    
            obs_name = best_mic.obs_name.text()
            if obs_name:
                mute[obs_name] = False

            self.best_mic.setText(best_mic.name)

            for mic, state in mute.items():
                mute_request = {"request-type": "SetMute", "source": mic, "mute": state}
                Sandbox().obs.send(mute_request)