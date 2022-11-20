import cv2
import pyautogui
import time
import numpy as np
i=0

img_name = "megaman-7-shrunk.png"
img = cv2.imread(f'images/{img_name}')
img_height = img.shape[0]
img_width = img.shape[1]
set_of_colours = set([])
background_to_remove = tuple(img[0][0])

for i in range(img_width):
    for j in range(img_height):
        B = int(img[j][i][0])
        G = int(img[j][i][1])
        R = int(img[j][i][2])
        tup = (B, G, R)
        if tup != background_to_remove:
            set_of_colours.add(tup)


for unique in set_of_colours:
    i += 1
    red = unique[2]
    green = unique[1]
    blue = unique[0]

    bgr = [blue, green, red]

    y, x = np.where(np.all(img == bgr, axis=2))
    zipped = np.column_stack((x,y))

    pyautogui.click(1949, 175)
    pyautogui.click(1949, 175)

    time.sleep(0.5)
    pyautogui.hotkey('f')
    time.sleep(0.5)
    pyautogui.typewrite(f"{str(red)},{str(green)},{str(blue)}")
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)

    for item in range(len(zipped)):
        pyautogui.moveTo(x=zipped[item][0]+2110, y=zipped[item][1]+230)
        pyautogui.click()
        print(str(item) + " / " + str(len(zipped)))
        time.sleep(0.1)

    print(i)
    print(unique)

