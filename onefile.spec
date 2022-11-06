# -*- mode: python ; coding: utf-8 -*-

import configparser


# load app info
with open('app/app_info.py') as f:
    file_content = '[dummy_section]\n' + f.read()

config = configparser.ConfigParser()
config.read_string(file_content)

section = config['dummy_section']

app_name = section['AppName'].replace('"', '')
icon_file = str(section['AppIconPath'] + '/' + section['AppIconName']).replace('"', '')


a = Analysis(
    ['app/main.py'],
    pathex=['./app'],
    binaries=[],
    datas=[
        ('app/resources', 'resources'),
        ('app/plugins/*.zip', 'plugins'),
        ('app/plugins/devices/*.zip', 'plugins/devices'),
    ],
    hiddenimports=[
        'numpy',
        'sounddevice',
        'flask',
        'qtpy.QtWebSockets',
        'qtpy.shiboken',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)

pyz = PYZ(
    a.pure, 
    a.zipped_data,
    cipher=None
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
    console=False
)
