import time
import pyautogui
import random
from PIL import Image
from collections import OrderedDict

i = 0

def MouseWiggle(sleepFor):
    time.sleep(sleepFor)
    current_pos = pyautogui.position()

    for x in range(3):
        randomX = random.randint(2000, 3700)
        randomY = random.randint(0, 1600)
        pyautogui.moveTo(randomX, randomY, 0.25)

    pyautogui.moveTo(current_pos)
    time.sleep(default_time)

time.sleep(0.05)

picture = Image.open("mar"
                     "io.jpg")
width, height = picture.size

startingPosX = 2362+2
startingPosY = 380+2

pyautogui.moveTo(startingPosX, startingPosY)
pyautogui.click()
default_time = 0.4

for pixelH in range(height):
    for pixelW in range(width):
        i += 1
        r, g, b = picture.getpixel((pixelW, pixelH))
        print(f"{str(i / (width*height))[2:4]}%")
        pyautogui.hotkey("f")
        time.sleep(default_time)
        pyautogui.typewrite("{0},{1},{2}".format(r, g, b))
        time.sleep(default_time)
        pyautogui.hotkey("enter")
        time.sleep(default_time)
        pyautogui.click()
        time.sleep(default_time)
        pyautogui.moveRel(1, 0)
        if i % 5 == 0:
            MouseWiggle(default_time)
    pyautogui.moveRel(-(width*1), 1)
    time.sleep(default_time)