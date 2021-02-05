import pyautogui
import pytesseract
import cv2
import keyboard
import time
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'D:\Programs\pytesseract\tesseract.exe'

#test
# img = pyautogui.screenshot(region=(1277,1003,52,43))
# img.save(r'D:\savedimg.png')
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(1280,1045)[0] == 123 and pyautogui.pixel(1280,1045)[1] == 48 and pyautogui.pixel(1280,1045)[2] == 44:
        if keyboard.is_pressed('1') == True:
            time.sleep(2.6)
        else:    
            time.sleep(0.6)
            keyboard.press_and_release('2')


# pyautogui.locateOnScreen()