import pyautogui
import time
import os
#move mouse
while True:
    x,y=pyautogui.position()
    print(x,y)

pyautogui.hotkey('win')
time.sleep(3)
pyautogui.write('termina')
#time.sleep(3)
#pyautogui.hotkey('enter')
#print(__file__)
mypath=os.path.dirname(os.path.realpath(__file__))+"/terminal.png"
isfind=None
while isfind is None:
    isfind=pyautogui.locateOnScreen(mypath,confidence=0.7)

print("I got the image")


