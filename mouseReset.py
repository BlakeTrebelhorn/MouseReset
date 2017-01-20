import win32api
import pyHook
import pythoncom
import time

# get screen size, and find middle
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
midWidth = (width + 1) / 2
midHeight = (height + 1) / 2


# move cursor to pixel x, y
def moveCursor(x, y):
    # time.sleep(0.2)
    print('Moving mouse')
    win32api.SetCursorPos((x, y))


# listen function for click event
def onclick(event):
    print(event.Position)
    moveCursor(int(midWidth), int(midHeight))  # call moveCursor to screen mid
    return True


# wait function - alternative to time.sleep()
def wait(time_lapse):
    time_start = time.time()
    time_end = (time_start + time_lapse)

    while time_end > time.time():
        pass


# function that checks if left or right control is pressed
# if so, it unhooks the mouse and keyboard for 10 secs, then rehooks
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
    hm.SubscribeMouseLeftUp(onclick)  # only watch left mouse button up
    hm.SubscribeKeyDown(checkCtrl)  # only watch keyboard button down
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()
except KeyboardInterrupt:
    hm.UnhookMouse()
    hm.UnhookKeyboard()
    print('\nDone.')
    exit()
