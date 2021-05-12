from .voter import MicVoterWidget


def install_plugin(plugin_manager):
    plugin_manager.register.widget('Mic Voter', MicVoterWidget())