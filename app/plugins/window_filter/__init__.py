import psutil
from ctypes import wintypes, windll, create_unicode_buffer, byref


def getForegroundWindowTitle():
    hWnd = windll.user32.GetForegroundWindow()

    id = wintypes.DWORD()
    windll.user32.GetWindowThreadProcessId(hWnd, byref(id))
    info = psutil.Process(id.value)

    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    
    if buf.value:
        return f'[{info.name()}] "{buf.value}"'
    else:
        return None