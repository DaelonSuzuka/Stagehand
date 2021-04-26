from qtstrap import *
from pathlib import Path
import json
import importlib
import sys
from codex import SerialDevice
import codex
import zipimport


plugin_folder = OPTIONS.APPLICATION_PATH / 'plugins'


class _Plugins:
    _plugins = {}

    def __init__(self):
        for plugin in plugin_folder.glob('*'):
            # if not plugin.is_dir():
                # continue

            if plugin.suffix == '.zip':
                self.load_zip_plugin(plugin)

            # if plugin.is_dir() and Path(plugin / 'plugin.json').exists():
            #     self.load_loose_plugin(plugin)

    def list_all(self):
        return self._plugins

    def __getattr__(self, name):
        return self._plugins[name]
    
    def __contains__(self, key):
        return key in self._plugins

    def load_zip_plugin(self, plugin):
        relative = plugin.relative_to(OPTIONS.APPLICATION_PATH)
        # relative = relative.replace('/','.')

        print('loading zip plugin', relative)
        zip = zipimport.zipimporter(relative.as_posix())
        module = zip.load_module(relative.name.split('.')[0])
        self._plugins[module.__name__.split('.')[-1]] = module
        setattr(sys.modules[__name__], module.__name__, module)

    def load_loose_plugin(self, plugin):
        relative = plugin.relative_to(OPTIONS.APPLICATION_PATH).as_posix()
        relative = relative.replace('/','.')

        module = importlib.import_module(relative)
        self._plugins[module.__name__.split('.')[-1]] = module
        setattr(sys.modules[__name__], module.__name__, module)


plugins = None


def Plugins():
    global plugins
    if plugins is None:
        plugins = _Plugins()
    return plugins


Plugins()