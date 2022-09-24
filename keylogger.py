#Install keyboard - pip3 install keyboard

import keyboard
keys = keyboard.record(until ='ENTER')
keyboard.play(keys)