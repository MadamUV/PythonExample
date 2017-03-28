import pyautogui
import random
#import os
pyautogui.size()
#os.system('C:\Program Files (x86)\KADOKAWA\RPGMV\RPGMV.exe')
width, height = pyautogui.size()
pyautogui.PAUSE = 1
for x in range(2, 320):
    pyautogui.moveTo(260, 42, duration=0.25)
    pyautogui.click()
    pyautogui.moveTo(260, 165, duration=0.25)
    pyautogui.click()
    pyautogui.moveTo(207, 450, duration=0.25)
    pyautogui.click()
    pyautogui.moveTo(200, 630, duration=0.25)
    pyautogui.click()
#tools menu 290, 42
#menu option 290, 165
#randomize 207, 450
#save settings 200, 630
    
#tap right key
#tap left key 5 times
#tap backspace
#type number in increment
#hit enter
    pyautogui.typewrite(['right', 'left', 'left', 'left', 'left', 'left', , 'enter'])
