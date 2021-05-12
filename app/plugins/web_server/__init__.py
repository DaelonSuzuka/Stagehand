from .web_interface import WebInterfaceManager



def install_plugin(plugin_manager):
    plugin_manager.register.widget('Web Actions', WebInterfaceManager())