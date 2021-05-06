from .voter import MicVoterWidget


def install_plugin(plugin_manager):
    plugin_manager.register_widget('Mic Voter', MicVoterWidget())