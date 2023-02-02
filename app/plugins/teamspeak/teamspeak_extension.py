from stagehand.sandbox import SandboxExtension
from .teamspeak_socket import TeamSpeakSocket


class TeamSpeakExtension(SandboxExtension):
    name = 'teamspeak'

    def __init__(self):
        pass

    def send_key_press(self, key, state):
        payload = {
            "type": "keyPress",
                "payload": {
                    "button": key,
                    "state": state
                }
        }
        TeamSpeakSocket().send(payload)

    def send(self, payload):
        TeamSpeakSocket().send(payload)