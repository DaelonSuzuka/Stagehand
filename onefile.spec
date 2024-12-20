# -*- mode: python ; coding: utf-8 -*-

import configparser


APP_DIR = 'src/stagehand'

# load app info
with open(f'{APP_DIR}/app_info.py') as f:
    file_content = '[dummy_section]\n' + f.read()

config = configparser.ConfigParser()
config.read_string(file_content)

section = config['dummy_section']

app_name = section['AppName'].replace('"', '')
icon_file = APP_DIR + '/' + str(section['AppIconPath'] + '/' + section['AppIconName']).replace('"', '')


a = Analysis(
    [f'{APP_DIR}/__main__.py'],
    pathex=[APP_DIR],
    binaries=[],
    datas=[
        (f'{APP_DIR}/resources', 'resources'),
        (f'{APP_DIR}/plugins/*.zip', 'plugins'),
        (f'{APP_DIR}/plugins/devices/*.zip', 'plugins/devices'),
    ],
    hiddenimports=[
        'pygame',
        'pynput',
        'ahk',
        'numpy',
        'sounddevice',
        'qtpy.QtWebSockets',
        'qtpy.shiboken',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=None,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name=app_name,
    icon=icon_file,
    debug=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=False,
)
