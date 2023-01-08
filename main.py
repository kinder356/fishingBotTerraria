import cv2
import numpy as np
import keyboard
import mss
import pyautogui
from time import sleep


sct = mss.mss()
go_fishing = False

def click():
    pyautogui.mouseDown()
    sleep(0.01)
    pyautogui.mouseUp()

def doScreenshot(sct, mon):
    img = sct.grab(mon)  # Делаю скриншот
    img = mss.tools.to_png(img.rgb, img.size)  # Кодирую в байты
    img = np.frombuffer(img, np.uint8)  # Преобразую байты в numpy-массив
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img


def check():


    cur = pyautogui.position()
    mon = {"top": cur[1] - 85, "left": cur[0] - 60, "width": 120, "height": 100}

    img = doScreenshot(sct, mon)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_red = (0,50,50)
    high_red = (10,255,255)
    mask0 = cv2.inRange(hsv, low_red, high_red)



    hasRed = np.sum(mask0)


    # 80_000, 150_000
    if hasRed > 70_000:
        print(f"красный есть (жду рыбу): {hasRed}")
        pass
    else:
        print(f"красного нету (вытаскиваю): {hasRed}")
        click()
        sleep(1)
        click()
        sleep(2)




    # cv2.imshow('picture', img)
    # cv2.waitKey(0)
    # cv2.imshow('picture', mask0)
    # cv2.waitKey(0)


def setGoFishing():
    global go_fishing
    go_fishing = not go_fishing



keyboard.add_hotkey("o", setGoFishing)

while True:
    if go_fishing:
        check()

    sleep(0.05)
