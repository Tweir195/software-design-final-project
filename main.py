#This is the main file for our project
from background.py import *
from informationclasses.py import *

import pygame

if __name__ == "__main__":
    pygame.init()
    view = background(["Attachment-1.png"], size=(1280,960))
    running = True
    view.screen.blit(view.background,(0,0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        view.draw(0,0,0)
        view.clear_screen()
