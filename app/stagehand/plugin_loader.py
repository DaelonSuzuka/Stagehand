from qtstrap import *
from pathlib import Path
import json
import importlib
import sys
import os
import codex
import zipimport

from stagehand.sandbox import _Sandbox
from stagehand.actions import ActionStack


plugin_folder = OPTIONS.APPLICATION_PATH / 'plugins'


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Plugins():
    _plugins = {}

    def __init__(self):        
        self.plugin_widgets = {}
        self.sidebar_widgets = {}
        self.statusbar_widgets = {}

        def is_plugin(p):
            return Path(Path(p) / 'plugin.json').exists() or Path(Path(p) / '__init__.py').exists()

        plugins = [Path(d[0]) for d in os.walk(plugin_folder) if is_plugin(d[0])]
        for plugin in plugins:
            self.load_loose_plugin(plugin)

        for plugin in plugin_folder.rglob('*.zip'):
            self.load_zip_plugin(plugin)

    def list_all(self):
        return self._plugins

    def register_sandbox_extension(self, name, extension):
        _Sandbox.extensions[name] = extension

    def register_action_type(self, name, action):
        ActionStack.actions[name] = action

    def register_widget(self, name, widget):
        self.plugin_widgets[name] = widget

    def register_sidebar_widget(self, name, widget):
        self.sidebar_widgets[name] = widget

    def register_statusbar_widget(self, name, widget):
        self.statusbar_widgets[name] = widget

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
            module = importlib.import_module(plugin_name)
            self._plugins[plugin_name] = module

            if hasattr(module, 'install_plugin'):
                module.install_plugin(self)


# plugins = None


# def Plugins():
#     global plugins
#     if plugins is None:
#         print('making new plugins')
#         plugins = _Plugins()
#     return plugins


# Plugins()