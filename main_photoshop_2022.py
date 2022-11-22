import cv2
import pyautogui
import time
import numpy as np
import requests
lot = 0.5
coordinatesToClick = []

def rgb_to_hex(r, g, b):
    url = "https://www.thecolorapi.com/id?rgb=rgb({},{},{})".format(r, g, b)
    r = requests.get(url)
    source = r.json()
    return source['hex']['clean']


img_name = "blaze.png"
img = cv2.imread(f'images/{img_name}', cv2.IMREAD_COLOR)



img_height = img.shape[0]
img_width = img.shape[1]
set_of_colours = set([])
background_to_remove = tuple(img[1][1])

for i in range(img_width):
    for j in range(img_height):
        B = int(img[j][i][0])
        G = int(img[j][i][1])
        R = int(img[j][i][2])
        tup = (B, G, R)
        if tup != background_to_remove:
            set_of_colours.add(tup)

num = len(set_of_colours)

time.sleep(lot)
print("Before clicking Edit Colours")
pyautogui.click(2660, 15)
time.sleep(lot)
pyautogui.hotkey('ctrl', 'n')
time.sleep(lot)

for i in range(3):
    pyautogui.hotkey('tab')
    time.sleep(lot)

pyautogui.typewrite(str(img_width))
time.sleep(lot)

for i in range(2):
    pyautogui.hotkey('tab')
    time.sleep(lot)

pyautogui.typewrite(str(img_height))
time.sleep(lot)
pyautogui.hotkey('enter')

for unique in set_of_colours:
    print('--start of loop--')
    # Format RGB values as BGR and placing them in an array
    red = unique[2]
    green = unique[1]
    blue = unique[0]
    bgr = (blue, green, red)

    # Gathers all the coordinates in an image and places them all in a single array
    y, x = np.where(np.all(img == bgr, axis=2))
    zipped = np.column_stack((x, y))

    print('reassuring pencil tool')
    # Reassure Pencil Tool
    time.sleep(lot)
    pyautogui.click(1941, 311)
    time.sleep(lot)
    print("Pencil tool assured")

    pyautogui.click(1934, 694)
    time.sleep(lot)
    pyautogui.typewrite("#" + str(rgb_to_hex(red, green, blue)))
    time.sleep(lot)
    pyautogui.hotkey('enter')
    time.sleep(lot)

    for item in range(len(zipped)):
        coordinatesToClick.append([zipped[item][0] + 2688-(img_width//2)+1, zipped[item][1] + 488-(img_height//2)])

    for i in range(len(coordinatesToClick)-1):

        x, y = pyautogui.position()
        currentMousePos = [x, y]
        coordinatesToClick.sort(key=lambda x: (x[0] - currentMousePos[0]) ** 2 + (x[1] - currentMousePos[1]) ** 2)

        currentCoordinate = (coordinatesToClick[0][0], coordinatesToClick[0][1])

        pyautogui.click(currentCoordinate)
        coordinatesToClick.remove(coordinatesToClick[0])
        print(str(i) + " / " + str(len(zipped)) + " / " + str(num))

    pyautogui.click(coordinatesToClick[0])
    num = num - 1
    print("--end of loop--")


