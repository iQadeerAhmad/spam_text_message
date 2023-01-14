#!/usr/bin/env python3
import pyautogui
import time

def main():
    time.sleep(3)
    with open('spam_message_text.txt', 'r') as file:
        a = file.readlines()
        for lines in a:
            pyautogui.write(lines)
            pyautogui.press('enter')
            time.sleep(0.1)

main()