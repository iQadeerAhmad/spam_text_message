#!/usr/bin/env python3
import pyautogui
import time

time.sleep(3)
with open('baba.txt', 'r') as file:
    a = file.readlines()
    for lines in a:
        pyautogui.write(lines)
        pyautogui.press('enter')
        time.sleep(0.1)
