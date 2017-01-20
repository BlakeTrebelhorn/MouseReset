# Mouse Reset
## About
I made this for someone I know whom works with cognitively handicapped children. They have a problem where the child would move a mouse to a certain place, and continue to click on that spot, whether they were picking the right answer or not. This simply moves the mouse back to the middle of the screen, as to prevent that.

I used a lot of resources online to help me. They are listed below:
* http://stackoverflow.com/questions/165495/detecting-mouse-clicks-in-windows-using-python
* https://sourceforge.net/p/pyhook/wiki/PyHook_Tutorial/#mouse-hooks
* http://stackoverflow.com/questions/17244317/using-pyhook-to-get-mouse-coordinates-to-play-back-later
* http://www.dangibbs.co.uk/journal/python-wait-function-alternative-to-sleep-for-gtk

## Usage
You're gonna have to have a few things installed:
* Have [Python 3](https://www.python.org/downloads/) installed
* Install pyHook `pip install pyhook`
* Install pywin32 `pip install pywin32` or `pip install pypiwin32`

Just run the mouseReset.py. You should be able to close the program without too much trouble. If all else fails, `ctrl + shift + esc` will override the mouse reset on click, and will let you end task on the python script running.

### TODO
* Make for macOS