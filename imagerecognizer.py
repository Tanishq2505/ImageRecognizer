import os

os.system("pip install pywin32 --user")
os.system("pip install keyboard")
os.system("pip install pyautogui")
os.system("pip install opencv-python")
print("Yess")
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#left lane x:702 Y: 577
#second left x:793 Y: 577
#third x: 875 y:577
#fourth x:963 y:577
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def hold(x,y):
    win32api.SetCursorPos((x+20,y+20))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    if pyautogui.pixel(x-30,y-30)[0] == 51:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def start_clicking():
    while keyboard.is_pressed('q') == False: 
        if pyautogui.pixel(1010,642)[0] == 254:
            click(1010,642)
            time.sleep(0.1)
        elif pyautogui.pixel(664,620)[0] == 1:
            click(664,650)
            time.sleep(0.1)
        elif pyautogui.pixel(770,620)[0] == 1:
            click(770,650)
            time.sleep(0.1)
        elif pyautogui.pixel(868,620)[0] == 1:
            click(868,650)
            time.sleep(0.1)
        elif pyautogui.pixel(968,620)[0] == 1:
            click(968,650)
            time.sleep(0.1)
        elif pyautogui.pixel(664,699)[0] == 0 or pyautogui.pixel(664,699)[0] == 5 or pyautogui.pixel(664,699)[0] == 6:
            hold(664,670)
            time.sleep(0.1)
        elif pyautogui.pixel(770,688)[0] == 0 or pyautogui.pixel(770,688)[0] == 5 or pyautogui.pixel(770,688)[0] == 6:
            hold(770,670)
            time.sleep(0.1)
        elif pyautogui.pixel(868,688)[0] == 0 or pyautogui.pixel(868,688)[0] == 5 or pyautogui.pixel(868,688)[0] == 6:
            hold(868,670)
            time.sleep(0.1)
        elif pyautogui.pixel(968,688)[0] == 0 or pyautogui.pixel(968,688)[0] == 5 or pyautogui.pixel(968,688)[0] == 6:
            hold(968,670)
            time.sleep(0.1)


start_clicking()
