import os.path
import sys

from setuptools import find_packages, setup


def recursive_files(directory):
    paths = []
    for path, _, filenames in os.walk(directory):
        for filename in filenames:
            if not filename.endswith('.pyc') and filename != 'registered.json':
                paths.append(os.path.join('..', path, filename))
    return paths


if sys.version_info < (3, 9):
    raise RuntimeError('Stagehand requires Python 3.9 or later')

setupdir = os.path.dirname(__file__)

# with open(os.path.join(setupdir, "thonny", "VERSION"), encoding="ASCII") as f:
#     version = f.read().strip()
version = '0.1'

requirements = []
for line in open(os.path.join(setupdir, 'requirements.txt'), encoding='ASCII'):
    if line.strip() and not line.startswith('#'):
        requirements.append(line)

requirements = [
    'ahk==0.14.2',
    'ahk-binary==1.1.33.9',
    'appdirs',
    'click',
    'codex-engine-pyqt',
    'cyberlang',
    'inquirerpy',
    'monaco-qt',
    'numpy',
    'pygame-ce',
    'psutil',
    'pydantic==1.10.8',
    'pynput',
    'pyserial',
    'PySide6==6.7.2',
    'QtAwesome',
    'QtPy',
    'qtstrap',
    'sounddevice',
    'superqt',
]

setup(
    name='Stagehand',
    version=version,
    description='An event-based desktop automation tool for Windows, Linux, and macOS.',
    long_description='',
    url='https://github.com/DaelonSuzuka/Stagehand',
    author='David Kincaid',
    author_email='dlkincaid0@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: Freeware',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Education',
        'Topic :: Software Development',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Text Editors',
    ],
    keywords='',
    project_urls={
        'Source code': 'https://github.com/DaelonSuzuka/Stagehand',
        'Bug tracker': 'https://github.com/DaelonSuzuka/Stagehand/issues',
    },
    platforms=[
        'Windows',
        'macOS',
        'Linux',
    ],
    install_requires=requirements,
    python_requires='>=3.9',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': [
            'app/resources/*',
        ]
    },
    entry_points={
        'gui_scripts': ['stagehand = stagehand.main:main'],
    },
)
