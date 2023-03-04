import pyautogui
import pyautogui as pag
import time

coords = []

while True:
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr, sep ='\n')
    
    coords.append((x,y))
    #coords.append((positionStr))
    print ("")
    print (*coords)
    time.sleep(2)


    #Make a loop that loops through coords when done
    #Loop subjected to change holy fuck
    
    for i in range(len(coords)):
        pag.moveTo(coords[i])
        print(coords[i])
    #another big problem is to convert the coordiante into one list, hence 1 string since append only accepts one argument.
    
