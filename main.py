#This is the main file for our project
from background import *
from convobubble import *
from realpicture import *
from sprite import *
from button import *

import pygame


if __name__ == "__main__":
    pygame.init()
    view = background()
    cb = ConvoBubble('images/convobubble.PNG', -400, -200)
    panama = real_picture('images/panama.jpg', 300, 100)
    boat = sprite('images/Quincy.PNG',250, 450,200,400,width=450,height=550,resize=True)
    button = GoToButton(1100,780)
    images = ['images/WelcomeBG.PNG', 'images/Australia/AustraliaBG.PNG']

    running = True
    clock = pygame.time.Clock()
    FPS = 15

    index = 0
    view.draw(images[index])
    # cb.draw()
    # panama.draw()
    boat.draw()
    moveflag = False

    while running: # main program loop
        while index == 0:
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # boat.clear()
            boat.animate_surf(0,3,moveflag,bob=True)
            # view.draw(images[index])
            boat.move()
            # boat.draw()
            button.check_mouse(mouse)
            button.draw()
            index = button.mousedown(mouseflag,index,len(images)-1)
            pygame.time.wait(100)

        while index == 1:
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            boat.animate(0,3,moveflag,bob=True)
            view.draw(images[index])
            boat.draw()
            button.check_mouse(mouse)
            button.draw()
            index = button.mousedown(mouseflag,index,len(images)-1)
            pygame.time.wait(100)



    pygame.quit()
