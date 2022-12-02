import cv2
import pyautogui
import time
import numpy as np
import requests
brushes = [24, 22, 20, 18, 16, 14, 6, 4, 2, 1]

LOT = 0.7
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
        return str(str(Percentage) + "%")[:3]
    else:
        return str(str(Percentage) + "%")[:4]


img_url = 'images/goku.png'
img = cv2.imread(img_url, cv2.IMREAD_UNCHANGED)

img_height = img.shape[0]
img_width = img.shape[1]
set_of_colours = set()

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
pyautogui.click(2660, 15)
time.sleep(LOT)
pyautogui.hotkey('ctrl', 'n')
time.sleep(LOT)

for i in range(3):
    pyautogui.hotkey('tab')
    time.sleep(LOT)

print("--inputting width and height--")
pyautogui.typewrite(str(img_width))
time.sleep(LOT)

for i in range(2):
    pyautogui.hotkey('tab')
    time.sleep(LOT)

pyautogui.typewrite(str(img_height))
time.sleep(LOT)
pyautogui.hotkey('enter')

print("--setting up main Iterator--")
totalLength = len(brushes) * len(set_of_colours)
iterator = 0

set_of_colours = list(set_of_colours)

for brush in brushes:
    print('--start of loop--')
    pyautogui.click(2063, 43)
    time.sleep(LOT)
    pyautogui.click(2071, 188)
    time.sleep(LOT)
    pyautogui.typewrite(f"Hard Square {brush} ")
    time.sleep(LOT)
    pyautogui.click(2068, 331)
    time.sleep(LOT)
    pyautogui.hotkey('enter')
    time.sleep(LOT)

    for set_colour in set_of_colours:
        iterator += 1

        # Creating a new layer just in-case
        time.sleep(LOT)
        pyautogui.hotkey('shift', 'ctrl', 'n')
        time.sleep(LOT)
        pyautogui.typewrite(f"{percentage(iterator, totalLength)}%")
        pyautogui.hotkey('enter')

        # Gathers all the coordinates of that single colour and places them all in an array
        if brush == 1:
            y, x = np.where(np.all(img == set_colour, axis=2))
            zipped = np.column_stack((x, y))
        else:
            zipped = []
            for X in range(img_width):
                for Y in range(img_height):

                    channels = img.shape[2]

                    n = np.zeros((brush, brush, channels))
                    new_img = np.full_like(n, set_colour)

                    brush_stroke = img[Y-brush//2:Y+brush//2, X-brush//2:X+brush//2]

                    if brush_stroke.shape == new_img.shape:
                        if np.all(brush_stroke == set_colour) and np.all(brush_stroke == set_colour):
                            zipped.append([X, Y])
                            img[Y-brush//2:Y+brush//2, X-brush//2:X+brush//2] = (0, 0, 0)

        print('reassuring pencil tool')
        # Reassure Pencil Tool
        time.sleep(LOT)
        pyautogui.click(1941, 310)
        time.sleep(LOT)
        print("Pencil tool assured")

        if len(zipped) > 0:
            pyautogui.click(1934, 694)
            time.sleep(LOT)
            pyautogui.typewrite("#" + str(rgb_to_hex(set_colour)))
            time.sleep(LOT)
            pyautogui.hotkey('enter')
            time.sleep(LOT)
        else:
            print("--no pixels to paint on this layer--")

        for item in range(len(zipped)):
            coordinatesToClick.append([zipped[item][0] + 2688-(img_width//2)+1, zipped[item][1] + 488-(img_height//2)])
        for i in range(len(coordinatesToClick)):
            x, y = pyautogui.position()
            currentMousePos = [x, y]
            coordinatesToClick.sort(key=lambda x: (x[0] - currentMousePos[0]) ** 2 + (x[1] - currentMousePos[1]) ** 2)

            currentCoordinate = (coordinatesToClick[0][0], coordinatesToClick[0][1])


            pyautogui.click(currentCoordinate)
            coordinatesToClick.remove(coordinatesToClick[0])
            print(f"{percentage(i, len(zipped))}")
            print("100%")

        time.sleep(LOT)
        print(f"Colours: {iterator} / {len(set_of_colours)}")
        print("--end of loop--")
