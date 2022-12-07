import sys


# this plugin only works on windows, sorry
if sys.platform == 'win32':
    from .ahk_action import AutohotkeyAction
    from .ahk_extension import AutohotkeyExtension