from qtstrap import *
from pathlib import Path
import json
import importlib
import sys
import os
import codex
import zipimport
import logging


plugin_folder = OPTIONS.APPLICATION_PATH / 'plugins'


@singleton
class Plugins():
    _plugins = {}

    def __init__(self):
        self.log = logging.getLogger(__name__)

        def is_plugin(p):
            return Path(Path(p) / 'plugin.json').exists()

        plugins = [Path(d[0]) for d in os.walk(plugin_folder) if is_plugin(d[0])]
        for plugin in plugins:
            self.load_loose_plugin(plugin)

        # for plugin in plugin_folder.rglob('*.zip'):
        #     self.load_zip_plugin(plugin)

    def __getattr__(self, name):
        return self._plugins['plugins.' + name]
    
    def __contains__(self, key):
        return key in self._plugins

    def load_zip_plugin(self, plugin):
        self.log.info(f'Attemping to load zip plugin: {plugin}')
        plugin_name = plugin.relative_to(OPTIONS.APPLICATION_PATH).as_posix()
        plugin_name = plugin_name.replace('/','.')
        plugin_name = plugin_name[:-len('.zip')]

        if plugin_name not in self._plugins:
            sys.path.append(plugin)
            
            try:
                module = importlib.import_module(plugin_name)
                self._plugins[plugin_name] = module
                self.log.debug(f'Successfully loaded plugin: {plugin_name}')
            except Exception as e:
                self.log.error(f'Failed loading plugin: {plugin_name}', exc_info=True)

    def load_loose_plugin(self, plugin):
        self.log.info(f'Attemping to load loose plugin: {plugin}')
        plugin_name = plugin.relative_to(OPTIONS.APPLICATION_PATH).as_posix()
        plugin_name = plugin_name.replace('/','.')

        if plugin_name not in self._plugins:
            if Path(plugin / 'packages').exists():
                sys.path.append(plugin / 'packages')
            try:
                module = importlib.import_module(plugin_name)
                self._plugins[plugin_name] = module
                self.log.debug(f'Successfully loaded plugin: {plugin_name}')
            except Exception as e:
                self.log.error(f'Failed loading plugin: {plugin_name}', exc_info=True)