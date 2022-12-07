import cv2
import pyautogui
import time
import numpy as np
import requests
import experiment
from scipy.spatial import distance
LOT = 0.7
TOP_TOOLBAR = (2660, 15)
LAYER_TOP = (3783, 735)
LAYER_TOP_THUMBNAIL = (3604, 735)
LAYER_BOTTOM = (3783, 773)
LAYER_BOTTOM_THUMBNAIL = (3604, 773)
MERGE_VISIBLE = (3686, 806)
coordinatesToClick = []
filteredCoords = []

def rgb_to_hex(x):
    b, g, r = x
    url = f"https://www.thecolorapi.com/id?rgb=rgb({r},{g},{b})"
    r = requests.get(url)
    source = r.json()
    return source['hex']['clean']

def percentage(part, whole):
    Percentage = 100 * float(part)/float(whole)
    if Percentage < 10:
        return str(str(Percentage))[:3]
    else:
        return str(str(Percentage))[:4]

#443735
img_url = 'images/small_super_mario.png'
img = cv2.imread(img_url, cv2.IMREAD_UNCHANGED)
img = experiment.makeBorder(img)

img_height = img.shape[0]
img_width = img.shape[1]
set_of_colours = set()

# This goes through
for i in range(img_width):
    for j in range(img_height):
        B = int(img[j][i][0])
        G = int(img[j][i][1])
        R = int(img[j][i][2])
        tup = (B, G, R)
        set_of_colours.add(tup)

num = len(set_of_colours)

print("--creating new document--")
time.sleep(LOT)
pyautogui.click(TOP_TOOLBAR)
time.sleep(LOT)
pyautogui.hotkey('ctrl', 'n')
time.sleep(LOT)

for i in range(3):
    pyautogui.hotkey('tab')
    time.sleep(LOT)

print("--inputting width and height--")
pyautogui.typewrite(str(img_width+50))
time.sleep(LOT)

for i in range(2):
    pyautogui.hotkey('tab')
    time.sleep(LOT)

pyautogui.typewrite(str(img_height+50))
time.sleep(LOT)
pyautogui.hotkey('enter')

print("--setting up main Iterator--")
iterator = 0
brush_colour_index = 0

# Activate Pencil Tool
print('--activating pencil tool--')
time.sleep(LOT)
pyautogui.click(1941, 309)
time.sleep(LOT)

# Fill in background
print("--filling in background / creating fill layer--")
pyautogui.click(1933, 698)
pyautogui.typewrite("#" + str(rgb_to_hex(img[0, 0])))
time.sleep(LOT)
pyautogui.hotkey('enter')
time.sleep(LOT)
pyautogui.hotkey('alt', 'backspace')

# Setting up new empty layer
print("--creating empty layer--")
pyautogui.hotkey('shift', 'ctrl', 'n')
time.sleep(LOT)
pyautogui.hotkey('enter')
time.sleep(LOT)
it = 0


# Removing background from set_of_colours
set_of_colours.remove(tuple(img[0, 0]))

for set_colour in set_of_colours:
    it += 1
    img = experiment.givePaintPoints(img_url, set_colour)

    # Gathers all the coordinates of that single colour and places them all in an array
    y, x = np.where(np.all(img == (0, 0, 0), axis=2))
    zipped = list(zip(x, y))

    # Creating a new layer just in-case
    time.sleep(LOT)
    pyautogui.hotkey('shift', 'ctrl', 'n')
    time.sleep(LOT)
    pyautogui.hotkey('enter')

    # Reassure Pencil Tool
    print('--keeping pencil tool active--')
    time.sleep(LOT)
    pyautogui.hotkey('b')
    time.sleep(LOT)

    if len(zipped) > 0:
        pyautogui.click(1934, 694)
        time.sleep(LOT)
        pyautogui.typewrite("#" + str(rgb_to_hex(set_colour)))
        print(f"--changed colour to {set_colour}--")
        time.sleep(LOT)
        pyautogui.hotkey('enter')
        time.sleep(LOT)
    else:
        print("--no pixels to paint on this layer--")

    for item in range(len(zipped)):
        coordinatesToClick.append([zipped[item][0] + 2737-(img_width//2)+1, zipped[item][1] + 564-(img_height//2)])

    totalCoords = len(coordinatesToClick)
    for i in range(len(coordinatesToClick)):
        x, y = pyautogui.position()
        currentMousePos = [x, y]
        coordinatesToClick.sort(key=lambda x: (x[0] - currentMousePos[0]) ** 2 + (x[1] - currentMousePos[1]) ** 2)

        currentCoordinate = (coordinatesToClick[0][0], coordinatesToClick[0][1])

        pyautogui.click(currentCoordinate)

        coordinatesToClick.remove(coordinatesToClick[0])
        print(f"{percentage(i, totalCoords)} - {i} / {totalCoords}")

    time.sleep(LOT)

    pyautogui.hotkey('w')
    time.sleep(LOT)
    pyautogui.click(2737 - (img_width // 2) + 1, 564 - (img_height // 2))
    time.sleep(LOT)
    pyautogui.hotkey('shift', 'ctrl', 'i')
    time.sleep(LOT)
    pyautogui.hotkey('alt', 'backspace')

    time.sleep(LOT)
    pyautogui.hotkey('ctrl', 'd')

    print(f"{it} / {len(set_of_colours)}")

    if it > 1:
        with pyautogui.hold('ctrl'):
            pyautogui.click(LAYER_BOTTOM_THUMBNAIL)

        time.sleep(LOT)
        print(tuple(img[1, 1]))
        if set_colour == tuple(img[1, 1]):
            with pyautogui.hold('ctrl'):
                pyautogui.click(LAYER_TOP)
        else:
            with pyautogui.hold('ctrl'):
                with pyautogui.hold('alt'):
                    pyautogui.click(LAYER_TOP_THUMBNAIL)


        time.sleep(LOT)
        pyautogui.hotkey('delete')
        time.sleep(LOT)
        pyautogui.hotkey('ctrl', 'd')
        time.sleep(LOT)

        pyautogui.click(LAYER_TOP, button='right')
        time.sleep(LOT)
        pyautogui.click(MERGE_VISIBLE)
        time.sleep(LOT)

    print("--press any key to continue--")
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pyautogui.click(TOP_TOOLBAR)