import pyautogui
import random
import time

while True:
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr, sep ='\n')
    time.sleep(2)
    