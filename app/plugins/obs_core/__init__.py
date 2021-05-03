from stagehand.sandbox import  _Sandbox
from stagehand.actions import ActionStack

from .obs_action import ObsActionWidget
from .obs_extension import ObsExtension
from .obs_manager import ObsManager


def install_plugin():
    ActionStack.actions['obs'] = ObsActionWidget
    _Sandbox.extensions['obs'] = ObsExtension()


install_plugin()