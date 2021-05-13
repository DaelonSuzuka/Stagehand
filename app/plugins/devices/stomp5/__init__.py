from .stomp_5_profile import Stomp5
from .stomp_5_widget import Stomp5Widget
from .stomp_5_trigger import Stomp5Trigger



def install_plugin(plugin_manager):
    plugin_manager.register.trigger('stomp5', Stomp5Trigger)