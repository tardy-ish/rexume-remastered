from win32gui import GetForegroundWindow, GetWindowText
from win32process import GetWindowThreadProcessId

def getInfo():
    win = GetForegroundWindow()
    return GetWindowThreadProcessId(win)[1], GetWindowText(win)