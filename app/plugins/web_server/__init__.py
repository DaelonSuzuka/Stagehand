from .web_interface import WebInterfaceManager


def install_plugin(plugin_manager):
    widget = WebInterfaceManager()
    plugin_manager.register.widget('Web Actions', widget)
    plugin_manager.register.sidebar_widget('Web Actions', widget.sidebar_widget)