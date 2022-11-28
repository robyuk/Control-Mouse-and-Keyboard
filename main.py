#! /usr/bin/env /usr/bin/python3
"""
Gives examples on how to control the keyboard and mouse using pyautogui

Note: Does not wotk in a repl because replit has no GUI
Download this code to your desktop PC to try it out

pip install pyautogui
"""

import pyautogui

position=pyautogui(position) # Gets the current cursor position. Top left corner of the screen is position (x=0, y=0)
print(position)

# Move the cursor to a scrfeen location
pyautogui.moveTo(139,280, duration=1)  #duration is optional

# Left click at the current cursor localion
pyautogui.click()

# Left click at an absolute location
pyautogui.click(147,308) # (x,y)

# Doubleclick
pyautogui.doubleclick(x,y) # or
pyautogui.click(x,y,clicks=2)

#right click:
pyautogui.click(x,y, button='right') # or
pyautogui.dragTo(x,y, button='right')

# Move the cursor relative to the current position
pyautogui.move(100,200, duration=1)

# Use drag to draw (or move an item on screen)
#  This draws a square
pyautogui.click(1326,567)
pyautogui.drag(150,0,duration=1,button='left')
pyautogui.drag(0,-150,duration=1,button='left')
pyautogui.drag(-150,0,duration=1,button='left')
pyautogui.drag(0,150,duration=1,button='left')

# Say there is a text file icon at location (x=132, y=200)
pyautogui.doubleclick(132,200) # Open the file
pyautogui.press('down')  # Press the down keyboard key
pyautogui.press('enter')  # New line
pyautogui.write('Python is good too\n') #Enter text on the line

# Select all text in the file
pyautogui.hotkey('ctrl', 'a')

# Copy to the clipboard
pyautogui.hotkey('ctrl','c')

# Paste the text underneath the original test
pyautogui.press(2*['down'])    # Press the down keyboard key twice
pyautogui.press('enter')  # New line
pyautogui.hotkey('ctrl','v')

# Get the copied text in the clipboard
import pyperclip  #Standard library - no need to install it
text=pyperclip.paste()

pyautogui.alert(text)  # Display the captured text on the screen
