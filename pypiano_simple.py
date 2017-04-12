import pypiano_main

import pygame
from pygame.locals import *
import threading
import time
import queue
import os

def run():
    pygame.init()
    pygame.display.set_mode((640,480),0,32)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                space_down =pygame.key.get_pressed()[K_SPACE]
                if (event.key, space_down) in pypiano_main.key2note.keys():
                    note_name=pypiano_main.key2note[(event.key, space_down)]
                    # TODO 修改乐器名字
                    filename='./piano/' + note_name + '.ogg'
                    pygame.mixer.Sound(filename).play()

run()