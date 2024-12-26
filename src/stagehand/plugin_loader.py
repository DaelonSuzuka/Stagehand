import importlib
import logging
import sys
from pathlib import Path
from zipimport import zipimporter

import codex
from qtstrap import *


def flush_logs():
    if len(logging.getLogger().handlers) > 0:
        logging.getLogger().handlers[0].flush()


@singleton
class Plugins:
    _plugins = {}

    def __init__(self):
        self.log = logging.getLogger(__name__)

        plugin_folder = OPTIONS.BASE_PATH / 'plugins'

        for plugin in plugin_folder.rglob('*.zip'):
            self.load_zip_plugin(plugin)

        for plugin in plugin_folder.rglob('plugin.json'):
            self.load_loose_plugin(plugin.parent)

    def __getattr__(self, name):
        return self._plugins['plugins.' + name]

    def __contains__(self, key):
        return key in self._plugins

    def load_zip_plugin(self, plugin: Path):
        plugin_name = plugin.relative_to(OPTIONS.BASE_PATH).as_posix()
        plugin_name = plugin_name.replace('/', '.')
        plugin_name = plugin_name[: -len('.zip')]

        if plugin_name not in self._plugins:
            self.log.debug(f'Attemping to load zip plugin: {plugin}')
            flush_logs()
            sys.path.insert(0, plugin)

            try:
                importer = zipimporter(plugin.as_posix())
                module = importer.load_module(plugin_name)
                self._plugins[plugin_name] = module
                self.log.debug(f'Successfully loaded zip plugin: {plugin_name}')
                flush_logs()
            except Exception as e:
                self.log.error(f'Failed loading plugin: {plugin_name}', exc_info=e)
                flush_logs()

    def load_loose_plugin(self, plugin: Path):
        plugin_name = plugin.relative_to(OPTIONS.BASE_PATH).as_posix()
        plugin_name = plugin_name.replace('/', '.')
        plugin_name = 'stagehand.' + plugin_name

        if plugin_name not in self._plugins:
            self.log.info(f'Attemping to load loose plugin: {plugin_name}')
            flush_logs()

            try:
                package_dir = plugin / 'packages'
                if package_dir.exists():
                    self.log.info(f'Adding plugin package dir to path: {package_dir}')
                    flush_logs()
                    sys.path.insert(0, package_dir.as_posix())

                module = importlib.import_module(plugin_name)
                self._plugins[plugin_name] = module
                self.log.debug(f'Successfully loaded loose plugin: {plugin_name}')
                flush_logs()
            except Exception as e:
                self.log.error(f'Failed loading plugin: {plugin_name}', exc_info=e)
                flush_logs()
