from pynput import mouse, keyboard
import time

# List that will store the coordinates every time the user presses 'c'
coords = []


# Function to track where mouse is going (for debugging)
def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

# Function to track where mouse is clicking (for debugging)
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

# Function to identify which key is pressed and if 'c' is pressed, append.
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

    if key == keyboard.Key.esc:
        click_listener.stop()
        return False

    # Check if the pressed key is 'c'
    if key.char == 'c':
        # Append the current mouse coordinates to the coords list
        current_mouse_position = mouse.Controller().position
        coords.append(current_mouse_position)
        print(f"Coordinates appended: {coords}")

def on_release(key):
    print('{0} released'.format(key))

click_listener = mouse.Listener(on_move=on_move, on_click=on_click)
click_listener.start()

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print (coords)
'''
coords_time = []
for i in range(len(coords)):
    input_time = input(f"Enter time for coordinate {i + 1}: ")
'''