__version__ = '0.1'


import sys


# this filter only works on windows, sorry
if sys.platform == 'win32':
    from .active_window_filter import ActiveWindowFilter


from .program_running_filter import ProgramRunningFilter
