import cv2
import pyautogui
import time
import numpy as np
i = 0

img_name = "selfport.png"
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
    red = unique[2]
    green = unique[1]
    blue = unique[0]

    bgr = [blue, green, red]

    y, x = np.where(np.all(img == bgr, axis=2))
    zipped = np.column_stack((x,y))

    time.sleep(0.2)
    print("Before clicking Edit Colours")
    if i == 0:
        pyautogui.click(2916, 84)

    pyautogui.click(2916, 84)
    time.sleep(0.2)
    print("Clicked Edit Colours")
    # Modify Blue Field
    pyautogui.click(3074, 639)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    pyautogui.press('backspace')
    time.sleep(0.2)
    pyautogui.typewrite(str(blue))
    # Modify Green Field
    time.sleep(0.2)
    pyautogui.click(3074, 615)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    pyautogui.press('backspace')
    time.sleep(0.2)
    pyautogui.typewrite(str(green))
    # Modify Red Field
    time.sleep(0.2)
    pyautogui.click(3074, 596)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    pyautogui.press('backspace')
    time.sleep(0.2)
    pyautogui.typewrite(str(red))
    # Exit Dialog
    time.sleep(0.2)
    pyautogui.hotkey('enter')
    # Reassure Pencil Tool
    time.sleep(0.2)
    pyautogui.click(2164, 69)
    time.sleep(0.2)

    for item in range(len(zipped)):
        pyautogui.click(x=zipped[item][0]+2110, y=zipped[item][1]+230)
        print(str(item) + " / " + str(len(zipped)) + "\t" + str(i))

    i += 1
    print(unique)

