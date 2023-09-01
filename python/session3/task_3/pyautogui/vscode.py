import pyautogui
import time
import os
#open vscode
pyautogui.hotkey('win')
time.sleep(2)
pyautogui.write('vs')
time.sleep(2)
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.hotkey('Ctrl','Shift','x')
time.sleep(2)
#install clangd
pyautogui.write('clangd')
clangdpath = os.path.dirname(os.path.realpath(__file__))+ "/clangd.png"
isFind=None
while isFind is None:
    isFind=pyautogui.locateAllOnScreen(clangdpath)

time.sleep(2)
pyautogui.moveTo(340,214)
pyautogui.click(button= 'left')
time.sleep(3)
print("clangd installed")
#clear the clangd to intsall another one
pyautogui.hotkey('ctrl','w')
pyautogui.moveTo(338,143)
pyautogui.click(button= 'left')
pyautogui.hotkey('ctrl','a')
time.sleep(1)
pyautogui.press('backspace')
time.sleep(2)

#install c++TestMate
pyautogui.write('c++ testmate ')
TestMatepath = os.path.dirname(os.path.realpath(__file__))+ "/c++testmate.png"
isFind=None
while isFind is None:
    isFind=pyautogui.locateAllOnScreen(TestMatepath)

time.sleep(2)
pyautogui.moveTo(340,214)
pyautogui.click(button= 'left')
time.sleep(3)
print("c++TestMate installed")
pyautogui.hotkey('ctrl','w')
pyautogui.moveTo(338,143)
pyautogui.click(button= 'left')
pyautogui.hotkey('ctrl','a')
time.sleep(1)
pyautogui.press('backspace')
time.sleep(2)

#install c++ helper

pyautogui.write('c++ helper  ')
helperpath = os.path.dirname(os.path.realpath(__file__))+ "/c++helper.png"
isFind=None
while isFind is None:
    isFind=pyautogui.locateAllOnScreen(helperpath)

time.sleep(2)
pyautogui.moveTo(340,214)
pyautogui.click(button= 'left')
time.sleep(3)
print("c++ helper installed")
pyautogui.hotkey('ctrl','w')
pyautogui.moveTo(338,143)
pyautogui.click(button= 'left')
pyautogui.hotkey('ctrl','a')
time.sleep(1)
pyautogui.press('backspace')
time.sleep(2)

#cmake install
pyautogui.write('cmake ')
cmakepath = os.path.dirname(os.path.realpath(__file__))+ "/cmake.png"
isFind=None
while isFind is None:
    isFind=pyautogui.locateAllOnScreen(cmakepath)

time.sleep(2)
pyautogui.moveTo(340,214)
pyautogui.click(button= 'left')
time.sleep(3)
print("cmake installed")
pyautogui.hotkey('ctrl','w')
pyautogui.moveTo(338,143)
pyautogui.click(button= 'left')
pyautogui.hotkey('ctrl','a')
time.sleep(1)
pyautogui.press('backspace')
time.sleep(2)

#cmake tools install
pyautogui.write('cmake tools ')
cMakeToolspath = os.path.dirname(os.path.realpath(__file__))+ "/cmaketools.png"
isFind=None
while isFind is None:
    isFind=pyautogui.locateAllOnScreen(cMakeToolspath)

time.sleep(2)
pyautogui.moveTo(340,214)
pyautogui.click(button= 'left')
time.sleep(3)
print("cmake tools installed")
pyautogui.hotkey('ctrl','w')
pyautogui.moveTo(338,143)
pyautogui.click(button= 'left')
pyautogui.hotkey('ctrl','a')
time.sleep(1)
pyautogui.press('backspace')
time.sleep(2)