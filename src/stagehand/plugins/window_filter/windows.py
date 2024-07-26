import psutil
from ctypes import wintypes, windll, create_unicode_buffer, byref
import ctypes


EnumWindows = windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = windll.user32.GetWindowTextW
GetWindowTextLength = windll.user32.GetWindowTextLengthW
IsWindowVisible = windll.user32.IsWindowVisible


def get_window_title(window_handle):
    pid = wintypes.DWORD()
    windll.user32.GetWindowThreadProcessId(window_handle, byref(pid))
    info = psutil.Process(pid.value)

    length = windll.user32.GetWindowTextLengthW(window_handle)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(window_handle, buf, length + 1)

    if buf.value:
        return f'[{info.name()}] "{buf.value}"'
    else:
        return None


def getAllWindowTitles():
    titles = []

    def foreach_window(window_handle, lParam):
        if IsWindowVisible(window_handle):
            title = get_window_title(window_handle)
            if title:
                titles.append(title)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)

    return titles


def getForegroundWindowTitle():
    window_handle = windll.user32.GetForegroundWindow()
    return get_window_title(window_handle)
