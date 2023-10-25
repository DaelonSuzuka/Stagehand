import sys

if sys.platform == 'win32':
    from .shell_extension import CmdExtension, PowershellExtension
else:
    from .shell_extension import ShellExtension

from .shell_action import ShellAction
