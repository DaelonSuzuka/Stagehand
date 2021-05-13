from .obs_action import ObsActionWidget
from .obs_extension import ObsExtension
from .obs_manager import ObsManager


def install_plugin(plugin_manager):
    plugin_manager.register.action('obs', ObsActionWidget)
    plugin_manager.register.sandbox_extension('obs', ObsExtension())

    widget = ObsManager()
    plugin_manager.register.widget('OBS Manager', widget)
    plugin_manager.register.sidebar_widget('OBS', widget.sidebar_widget)
    plugin_manager.register.statusbar_widget('OBS', widget.status_widget)