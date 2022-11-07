from pathlib import Path
from zipfile import PyZipFile
import os
import click


@click.group()
def main() -> None:
    pass


PLUGIN_FOLDER = 'app/plugins/'


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