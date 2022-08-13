from pathlib import Path
from zipfile import ZipFile, PyZipFile
import shutil


plugin_folder = 'app/plugins/'


def build_plugins():
    plugins = [p for p in Path(plugin_folder).rglob('*') if Path(p / 'plugin.json').exists()]

    for plugin in plugins:
        with PyZipFile(plugin.as_posix() + '.zip', mode='w') as zip_module:
            zip_module.writepy(plugin)
        # shutil.make_archive(plugin, 'zip', plugin)
        # shutil.make_archive(f'app/plugins/{plugin.name}', 'zip', plugin)


if __name__ == "__main__":
    build_plugins()