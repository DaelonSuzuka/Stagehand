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
    binaries=[
        ('.venv/Scripts/AutoHotkey.exe', '.'),
    ],
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
    [],
    exclude_binaries=True,
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    icon=icon_file,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name=app_name,
)
