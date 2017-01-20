import win32api
import pyHook
import pythoncom
import time


width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = (width + 1) / 2
midHeight = (height + 1) / 2


def moveCursor(x, y):
    # time.sleep(0.2)
    print('Moving mouse')
    win32api.SetCursorPos((x, y))


def onclick(event):
    print(event.Position)
    moveCursor(int(midWidth), int(midHeight))
    return True


def wait(time_lapse):
    time_start = time.time()
    time_end = (time_start + time_lapse)

    while time_end > time.time():
        pass


def checkCtrl(event):
    if event.Key in ('Lcontrol', 'Rcontrol'):
        print('Pausing for 10 Seconds')
        hm.UnhookKeyboard()
        hm.UnhookMouse()
        wait(10)
        hm.HookKeyboard()
        hm.HookMouse()
    return True


try:
    hm = pyHook.HookManager()
    hm.SubscribeMouseLeftUp(onclick)
    hm.SubscribeKeyDown(checkCtrl)
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()
except KeyboardInterrupt:
    hm.UnhookMouse()
    hm.UnhookKeyboard()
    print('\nDone.')
    exit()
