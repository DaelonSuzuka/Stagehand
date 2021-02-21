from qt import *
import numpy as np
import sounddevice as sd
from time import time


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
        self.gain = float(gain)

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
        self.volume = min(int(self.amplitude * self.gain), 50)
        return self.volume


class MicStreamWidget(QWidget):
    def __init__(self, device, parent=None):
        super().__init__(parent=parent)

        self.stream = MicStream(device)

        self.device = sd.query_devices(device)
        self.name = self.device['name']
        self.title = QLabel(self.name)
        self.enabled = PersistentCheckBox(f'enabled:{self.name}', changed=self.on_check)
        self.obs_name = PersistentLineEdit(f'obs_name:{self.name}')
        self.meter = QLabel()

        self.gain = PersistentLineEdit(f'gain:{self.name}', changed=self.stream.set_gain)
        if self.gain.text() == '':
            self.gain.setText(str(self.stream.gain))
        self.gain.setFixedWidth(40)
        self.beta = PersistentLineEdit(f'beta:{self.name}', changed=self.stream.set_beta)
        if self.beta.text() == '':
            self.beta.setText(str(self.stream.beta))
        self.beta.setFixedWidth(40)

        self.on_check()
        
        # disabled until we can create a more structured widget layout
        # with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
        #     layout.add(self.title)
        #     layout.add(self.meter)
        #     layout.add(QLabel(), 1)
        #     layout.add(self.beta)
        #     layout.add(self.gain)
        #     layout.add(self.enabled)
        #     layout.add(self.obs_name)

    def on_check(self):
        if self.enabled.checkState() == Qt.Checked:
            self.title.setEnabled(True)
            self.stream.start()
        else:
            self.title.setEnabled(False)
            # self.stream.stop()
            self.meter.setText('')


class MicVoterWidget(QWidget):
    def __init__(self, parent=None, obs=None):
        super().__init__(parent=parent)

        self.best_mic = QLabel()
        self.obs = obs
        self.obs.message_received.connect(self.rx_msg)

        self.mics = {}
        for i, d in enumerate(sd.query_devices()):
            if d['hostapi'] == 3 and d['max_input_channels'] > 0:
                self.mics[i] = MicStreamWidget(i)

        self.timer = QTimer()
        self.timer.timeout.connect(self.process_audio)
        self.timer.start(50)
        self.last_changed_time = time()
        self.rate_limit = PersistentLineEdit('rate_limit', default='1')

        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Best Mic:'))
                layout.add(self.best_mic)
                layout.add(QLabel(), 1)
                layout.add(QLabel('Rate Limit:'))
                layout.add(self.rate_limit)

            layout.add(QLabel())

            with layout.hbox() as layout:
                layout.add(QLabel('title'), 6)
                layout.add(QLabel('meter'), 5)
                layout.add(QLabel('beta'), 1)
                layout.add(QLabel('gain'), 1)
                layout.add(QLabel('obs_name'), 1)
                layout.add(QLabel('enabled'), 1)

            layout.add(HLine())
            with layout.hbox() as layout:
                with layout.vbox() as layout:
                    for key, mic in self.mics.items():
                        layout.add(mic.title)
                layout.add(VLine())
                with layout.vbox(1) as layout:
                    for key, mic in self.mics.items():
                        layout.add(mic.meter)
                layout.add(VLine())
                with layout.vbox() as layout:
                    for key, mic in self.mics.items():
                        with layout.hbox() as layout:
                            layout.add(mic.beta)
                            layout.add(mic.gain)
                            layout.add(mic.obs_name)
                            layout.add(mic.enabled)
                
            layout.add(QLabel(), 1)

    def rx_msg(self, message):
        if 'sources' in message:
            print('got it')

    def process_audio(self):
        volumes = {}
        for key, mic in self.mics.items():
            if mic.enabled.checkState() == Qt.Checked:
                volume = mic.stream.process_audio()
                volumes[key] = volume
                mic.meter.setText(str(volume) + ' ' + '|' * volume)

        sorted_keys = [k for k in reversed(sorted(volumes, key=volumes.get))]
        best_mic = self.mics[sorted_keys[0]]
            
        if (time() - self.last_changed_time) < float(self.rate_limit.text()):
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
                mute_request = {"request-type": "SetMute", 'source': mic, 'mute': state}
                self.obs.send(mute_request)