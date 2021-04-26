from qtstrap import *
from pathlib import Path


plugin_path = OPTIONS.APPLICATION_PATH / 'plugins'


def load_plugins():
    print('loading plugins')

    for f in plugin_path.glob('*'):
        if not f.is_dir():
            continue
        if f.suffix == '.zip':
            print('zip plugin:', f)
        if Path(f / 'plugin.json').exists():
            print('loose plugin:', f)