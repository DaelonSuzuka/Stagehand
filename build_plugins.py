from pathlib import Path
from zipfile import ZipFile
import shutil


def build_plugins():
    plugins = [p for p in Path('app/plugins/').glob('*') if Path(p / 'plugin.json').exists()]

    for plugin in plugins:
        shutil.make_archive(plugin.as_posix(), 'zip', plugin)


if __name__ == "__main__":
    build_plugins()