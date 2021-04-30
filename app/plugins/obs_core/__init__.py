from qtstrap import *
from stagehand.sandbox import Sandbox, _Sandbox
from stagehand.actions import ActionStack
from stagehand.obs import requests

from .obs_action import ObsActionWidget
from .obs_extension import ObsExtension


def install_plugin():
    ActionStack.actions['obs'] = ObsActionWidget
    _Sandbox.extensions['obs'] = ObsExtension()


install_plugin()