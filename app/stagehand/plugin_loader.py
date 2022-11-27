from qtstrap import *
from pathlib import Path
import json
import importlib
import sys
import os
import codex
import zipimport
from zipimport import zipimporter
import logging


plugin_folder = OPTIONS.APPLICATION_PATH / 'plugins'


@singleton
class Plugins:
    _plugins = {}

    def __init__(self):
        self.log = logging.getLogger(__name__)

        def is_plugin(p):
            return Path(Path(p) / 'plugin.json').exists()

        for plugin in plugin_folder.rglob('*.zip'):
            self.load_zip_plugin(plugin)

        plugins = [Path(d[0]) for d in os.walk(plugin_folder) if is_plugin(d[0])]
        for plugin in plugins:
            self.load_loose_plugin(plugin)

    def __getattr__(self, name):
        return self._plugins['plugins.' + name]

    def __contains__(self, key):
        return key in self._plugins

    def load_zip_plugin(self, plugin):
        plugin_name = plugin.relative_to(OPTIONS.APPLICATION_PATH).as_posix()
        plugin_name = plugin_name.replace('/', '.')
        plugin_name = plugin_name[: -len('.zip')]

        if plugin_name not in self._plugins:
            self.log.info(f'Attemping to load zip plugin: {plugin}')
            sys.path.insert(0, plugin)

            try:
                importer = zipimporter(plugin)
                module = importer.load_module(plugin_name)
                self._plugins[plugin_name] = module
                self.log.debug(f'Successfully loaded zip plugin: {plugin_name}')
            except Exception as e:
                self.log.error(f'Failed loading plugin: {plugin_name}', exc_info=True)

    def load_loose_plugin(self, plugin):
        plugin_name = plugin.relative_to(OPTIONS.APPLICATION_PATH).as_posix()
        plugin_name = plugin_name.replace('/', '.')

        if plugin_name not in self._plugins:
            self.log.info(f'Attemping to load loose plugin: {plugin}')
            try:
                package_dir = plugin / 'packages'
                if package_dir.exists():
                    self.log.info(f'Adding plugin package dir to path: {plugin}')
                    sys.path.insert(0, package_dir.as_posix())

                module = importlib.import_module(plugin_name)
                self._plugins[plugin_name] = module
                self.log.debug(f'Successfully loaded loose plugin: {plugin_name}')
            except Exception as e:
                self.log.error(f'Failed loading plugin: {plugin_name}', exc_info=True)
