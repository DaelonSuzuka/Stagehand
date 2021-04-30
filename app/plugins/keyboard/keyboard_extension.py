from pynput.keyboard import Key, Controller


class KeyboardExtension:
    def __init__(self):
        self.controller = Controller()

    def __getattr__(self, name):
        return getattr(Key, name)

    def key(self, k):
        self.controller.press(k)
        self.controller.release(k)

    def press(self, key):
        self.controller.press(key)

    def release(self, key):
        self.controller.release(key)