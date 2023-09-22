from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener, Key

coords = []
terminate = False

def onClick(x, y, button, pressed): #onClick accepts parameters such as x, y, button, pressed
    global terminate
    if pressed and not terminate:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        coords.append((x,y))
        print (terminate)

def onKeyboardPress(key): #Accepts parameter key which is escape.
    global terminate
    if key == Key.esc:
        print('Exiting...')
        terminate = True
        return False

# Create a keyboard listener
keyboard_listener = KeyboardListener(on_press=onKeyboardPress)

# Start the keyboard listener in a separate thread
keyboard_listener.start()

    
with Listener(on_click=onClick) as listener:
    listener.join()


