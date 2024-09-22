from pathlib import Path
from zipfile import PyZipFile
import os
import sys
import click
import subprocess


@click.group()
def main() -> None:
    pass


PLUGIN_FOLDER = 'src/stagehand/plugins/'


@main.command()
def install():
    plugins = [p for p in Path(PLUGIN_FOLDER).rglob('*') if Path(p / 'plugin.json').exists()]

    for plugin in plugins:
        req_file = plugin / 'requirements.txt'
        package_dir = plugin / 'packages'
        if req_file.exists():
            cmd = [sys.executable, '-m', 'pip', 'install', f'-r{req_file.as_posix()}', f'-t{package_dir.as_posix()}']
            subprocess.check_call(cmd)


@main.command()
def build():
    plugins = [p for p in Path(PLUGIN_FOLDER).rglob('*') if Path(p / 'plugin.json').exists()]

    for plugin in plugins:
        with PyZipFile(plugin.as_posix() + '.zip', mode='w') as zip_module:
            zip_module.writepy(plugin)


@main.command()
def clean():
    plugins = [p for p in Path(PLUGIN_FOLDER).rglob('*.zip')]

    for plugin in plugins:
        os.remove(plugin)


if __name__ == '__main__':
    main()
