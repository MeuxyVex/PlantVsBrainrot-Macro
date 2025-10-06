from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import pydirectinput
import time

mouse = MouseController()
keyboard = KeyboardController()

running = True
paused = False

def presstouch(x,y,o):
    keyboard.press(x)
    time.sleep(y)
    keyboard.release(x)
    if o == 1:
        keyboard.press(x)
        time.sleep(y)
        keyboard.release(x)

def mouvement(a,b,c):
    pydirectinput.moveRel(a, b, duration=c)
    pydirectinput.moveRel(0, 1, duration=10)


def seeds():
    for i in range(1,9):
        mouse.click(Button.left, 1)
        time.sleep(1)
        mouse.scroll(1, 1.54)
        pydirectinput.moveRel(0, 1, duration=10)
    presstouch("e",1, 0)
    time.sleep(1)
    presstouch(Key.shift,1,1)
    presstouch("s" ,2.4, 0)

def gear():
    time.sleep(2)
    presstouch(Key.shift,0.5,1)
    time.sleep(1)
    presstouch("e",1, 0)
    time.sleep(3)
    mouse.scroll(0, -6)
    time.sleep(1)
    mouvement(-42,200,10)
    mouse.click(Button.left, 1)
    for j in range(2):
        if j == 0 or 1:
            mouse.click(Button.left, 1)
            time.sleep(1)
            mouse.scroll(1, 1.54)
            mouse.click(Button.left, 1)
    
    for k in range(2):
        time.sleep(1)
        mouse.click(Button.left, 1)
        mouvement(0,-218,10)
        for m in range(6):
            time.sleep(0.5)
            mouse.click(Button.left, 1)
    time.sleep(1)
    presstouch("e",1, 0)

def retour():
    time.sleep(1)
    presstouch(Key.shift,0.5,1)
    presstouch("w" ,2.4, 0)
    time.sleep(1)
    presstouch("e" ,1, 0)
    mouse.scroll(0, -20)
    time.sleep(1)
    mouvement(-51,207,10)












