from qtstrap import *
from pathlib import Path
import json
import importlib
import sys
from codex import SerialDevice
import codex


plugin_folder = OPTIONS.APPLICATION_PATH / 'plugins'


class PluginLoader:
    def __init__(self):
        for plugin in plugin_folder.glob('*'):
            if not plugin.is_dir():
                continue

            if plugin.suffix == '.zip':
                load_zip_plugin(plugin)
            if Path(plugin / 'plugin.json').exists():
                load_loose_plugin(plugin)

    def load_zip_plugin(self, plugin):
        pass

    def load_loose_plugin(self, plugin):
        relative = plugin.relative_to(OPTIONS.APPLICATION_PATH).as_posix()
        relative = relative.replace('/','.')

        module = importlib.import_module(relative)
        setattr(sys.modules[__name__], module.__name__, module)