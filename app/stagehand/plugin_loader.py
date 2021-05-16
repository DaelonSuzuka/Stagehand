from qtstrap import *
from pathlib import Path
import json
import importlib
import sys
import os
import codex
import zipimport

from stagehand.sandbox import _Sandbox


plugin_folder = OPTIONS.APPLICATION_PATH / 'plugins'


class Registrar:
    def __init__(self, plugins):
        self.plugins = plugins
    
    def sandbox_extension(self, name, extension):
        _Sandbox.extensions[name] = extension

    def widget(self, name, widget):
        self.plugins.plugin_widgets[name] = widget

    def sidebar_widget(self, name, widget):
        self.plugins.sidebar_widgets[name] = widget

    def statusbar_widget(self, name, widget):
        self.plugins.statusbar_widgets[name] = widget


@singleton
class Plugins():
    _plugins = {}

    def __init__(self):
        self.plugin_widgets = {}
        self.sidebar_widgets = {}
        self.statusbar_widgets = {}

        self.register = Registrar(self)

        def is_plugin(p):
            return Path(Path(p) / 'plugin.json').exists()

        plugins = [Path(d[0]) for d in os.walk(plugin_folder) if is_plugin(d[0])]
        for plugin in plugins:
            self.load_loose_plugin(plugin)

        for plugin in plugin_folder.rglob('*.zip'):
            self.load_zip_plugin(plugin)

    def __getattr__(self, name):
        return self._plugins['plugins.' + name]
    
    def __contains__(self, key):
        return key in self._plugins

    def load_zip_plugin(self, plugin):
        plugin_name = plugin.relative_to(OPTIONS.APPLICATION_PATH).as_posix()
        plugin_name = plugin_name.replace('/','.')
        plugin_name = plugin_name[:-len('.zip')]

        if plugin_name not in self._plugins:
            sys.path.append(plugin)
            
            module = importlib.import_module(plugin_name)
            self._plugins[plugin_name] = module

    def load_loose_plugin(self, plugin):
        plugin_name = plugin.relative_to(OPTIONS.APPLICATION_PATH).as_posix()
        plugin_name = plugin_name.replace('/','.')

        if plugin_name not in self._plugins:
            if Path(plugin / 'packages').exists():
                sys.path.append(plugin / 'packages')

            module = importlib.import_module(plugin_name)
            self._plugins[plugin_name] = module

            if hasattr(module, 'install_plugin'):
                module.install_plugin(self)