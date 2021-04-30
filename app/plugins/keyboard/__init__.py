__version__ = "0.1"


from stagehand.sandbox import  _Sandbox
from stagehand.actions import ActionStack

from .keyboard_extension import KeyboardExtension
from .keyboard_action import KeyboardAction


def install_plugin():
    ActionStack.actions['keyboard'] = KeyboardAction

    keyboard = KeyboardExtension()
    _Sandbox.extensions['kb'] = keyboard
    _Sandbox.extensions['keyboard'] = keyboard


install_plugin()