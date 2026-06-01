import pygame
from gpiozero import Button
from signal import pause
import time

pygame.mixer.init(devicename="C-Media USB Headphone Set, USB Audio")
sound=pygame.mixer.Sound("sound2.mp3")
pl = 0

def in24() :
    global sound
    global pl
    if pl != 1:
        pl = 1
        sound.stop()
        sound=pygame.mixer.Sound("nar_central1.mp3")
        sound.play(0)
        time.sleep(5)
        pl = 0
    return

def in25():
    global pl
    global sound
    if pl != 2:
        pl = 2
        sound.stop()
        sound=pygame.mixer.Sound("nar_Wex.mp3")
        sound.play(0)
        time.sleep(5)
        pl = 0
    return

def in26():
    global pl
    global sound
    if pl != 3:
        pl = 3
        sound.stop()
        sound=pygame.mixer.Sound("nar_central2.mp3")
        sound.play(0)
        time.sleep(5)
        pl = 0
    return

def in27():
    global pl
    global sound
    if pl != 4:
        pl = 4
        sound.stop()
        sound=pygame.mixer.Sound("nar_Nex.mp3")
        sound.play(0)
        time.sleep(5)
        pl = 0
    return

button1 = Button(24, pull_up=True, hold_time=0.2)
button2 = Button(25, pull_up=True, hold_time=0.2)
button3 = Button(26, pull_up=True, hold_time=0.2)
button4 = Button(27, pull_up=True, hold_time=0.2)



button1.when_held = in24
button2.when_held = in25
button3.when_held = in26
button4.when_held = in27


pause()
