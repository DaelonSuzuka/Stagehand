# -*- mode: python ; coding: utf-8 -*-

import configparser


# load app info
with open('app/app_info.py') as f:
    file_content = '[dummy_section]\n' + f.read()

config = configparser.ConfigParser()
config.read_string(file_content)

app_name = config['dummy_section']['AppName'].replace('"', '')
icon_file = config['dummy_section']['AppIconName'].replace('"', '')


a = Analysis(
    ['app/main.py'],
    pathex=['./app'],
    binaries=[],
    datas=[
        ('app/resources', 'resources'),
        ('app/sandbox', 'sandbox'),
        ('app/web_pages', 'web_pages'),
        ('app/plugins', 'plugins'),
    ],
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name=app_name,
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    icon=icon_file,
    console=False 
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name=app_name
)
