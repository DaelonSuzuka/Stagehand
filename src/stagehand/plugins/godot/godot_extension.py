from qtstrap import *
from stagehand.sandbox import Sandbox, SandboxExtension

# from .requests import requests
from .godot_socket import GodotSocket


class GodotExtension(SandboxExtension):
    name = 'godot'

    def eval(self, string, cb=None):
        payload = {
            'request-type': 'Eval',
            'eval-string': string,
        }
        GodotSocket().send(payload, cb)

    def send(self, payload, cb=None):
        GodotSocket().send(payload, cb)
