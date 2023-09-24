from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener, Key
import pyautogui as pag
import time

coords = []
terminate = False
seconds = []

def click(coords):
    for i in range (len(coords)):
        pag.click(coords[i])
        time.sleep(seconds[i])
        print ("Moved to: ", coords[i], "for: ", seconds[i], "seconds")


def timeCheck(coords):
    global seconds
    for i in range(len(coords)):
        time_input = input(f"Enter time for coordinate {i + 1}: ")
        try:
            seconds.append(float(time_input))
        except ValueError:
            print("Invalid input. Please enter a numeric value for time.")

    print("Times entered: ", seconds)
    click(coords)

def onClick(x, y, button, pressed): #onClick accepts parameters such as x, y, button, pressed
    global terminate
    if pressed and not terminate:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        coords.append((x,y))

def onKeyboardPress(key): #Accepts parameter key which is escape.
    global terminate
    if key == Key.esc:
        print('Exiting...')
        terminate = True
        print (coords)
        timeCheck(coords)
        quit()

# Create a keyboard listener
keyboard_listener = KeyboardListener(on_press=onKeyboardPress)

# Start the keyboard listener in a separate thread
keyboard_listener.start()
    
with Listener(on_click=onClick) as listener:
    listener.join()