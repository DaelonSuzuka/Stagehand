__version__ = "0.1"


from .keyboard_extension import KeyboardExtension, MouseExtension
from .keyboard_action import KeyboardAction


def install_plugin(plugin_manager):
    plugin_manager.register_action_type('keyboard', KeyboardAction)

    keyboard = KeyboardExtension()
    plugin_manager.register_sandbox_extension('kb', keyboard)
    plugin_manager.register_sandbox_extension('keyboard', keyboard)

    mouse = MouseExtension()
    plugin_manager.register_sandbox_extension('mouse', mouse)