__version__ = "0.1"


from .keyboard_extension import KeyboardExtension, MouseExtension
from .keyboard_action import KeyboardAction
from .keyboard_trigger import KeyboardTrigger


def install_plugin(plugin_manager):
    plugin_manager.register.action('keyboard', KeyboardAction)
    plugin_manager.register.trigger('keyboard', KeyboardTrigger)

    keyboard = KeyboardExtension()
    plugin_manager.register.sandbox_extension('kb', keyboard)
    plugin_manager.register.sandbox_extension('keyboard', keyboard)

    mouse = MouseExtension()
    plugin_manager.register.sandbox_extension('mouse', mouse)