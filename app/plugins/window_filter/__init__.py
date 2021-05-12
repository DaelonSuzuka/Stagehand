__version__ = "0.1"


from .active_window_filter import ActiveWindowFilter


def install_plugin(plugin_manager):
    plugin_manager.register.filter('active window', ActiveWindowFilter)