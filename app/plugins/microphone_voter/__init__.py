from .voter import MicVoterWidget


def install_plugin(plugin_manager):
    widget = MicVoterWidget()
    plugin_manager.register.widget('Mic Voter', widget)
    plugin_manager.register.sidebar_widget('Mic Voter', widget.sidebar_widget)