from qtstrap import *
from stagehand.sandbox import Sandbox
from .requests import requests


class ObsExtension:
    def __getattr__(self, name):
        return requests[name]

    def send(self, payload, cb=None):
        ObsSocket().send(payload, cb)