from qtstrap import *
from stagehand.sandbox import Sandbox, SandboxExtension
from .interface import requests
from .obs_socket import ObsSocket


class ObsExtension(SandboxExtension):
    name = 'obs'

    def __getattr__(self, name):
        return requests[name]

    def send(self, payload, cb=None):
        ObsSocket().send(payload, cb)
