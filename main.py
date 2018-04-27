#This is the main file for our project
from background import *
from convobubble import *
from realpicture import *
from sprite import *
from button import *

import pygame

def animate_between_pages(moveflag):
    """Makes the boat float from one page to the next"""
    rect = pygame.Rect((0,0),(1280,700))
    view.draw(images[index-1])
    for i in range(50):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        # view.screen.fill((69,0,230))
        # pygame.draw.rect(view.screen,(133,202,255),rect)
        boat.animate(15,4,moveflag,True,bob=True)
        boat.draw()
        pygame.time.wait(100)


if __name__ == "__main__":
    pygame.init()
    view = background()
    cb = ConvoBubble('images/convobubble.PNG', -400, -200)
    button = GoToButton(1100,780)
    images = ['images/WelcomeBG.PNG', 'images/Australia/AustraliaBG.PNG']
    testpic = real_picture('images/cat-grumpy-icon.png',20,70,width=600,height=300,resize=True)

    running = True
    clock = pygame.time.Clock()
    FPS = 15

    index = 0
    view.draw(images[index])
    moveflag = False
    boat = sprite('images/Quincy.PNG',250, 420,200,430,images[index],width=450,height=550,resize=True)
    boat.draw()

    while running: # main program loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        while index == 0 and running:
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            changepos = boat.animate(0,3,moveflag,False,bob=True)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()
            index = button.mousedown(mouseflag,index,len(images)-1)
            pygame.time.wait(100)
            changepos = False
        moveflag = True
        if running:
            animate_between_pages(moveflag)
        boat = sprite('images/Quincy.PNG',250, 420,200,430,images[index],width=450,height=550,resize=True)
        moveflag = False
        view.draw(images[index])
        testpic.update(True)
        while index == 1 and running:
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            changepos = boat.animate(0,3,moveflag,False,bob=True)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()
            index = button.mousedown(mouseflag,index,len(images)-1)
            pygame.time.wait(100)
            changepos = False
        # view.draw(images[index])
        # boat.draw()
        # while index == 1:
        #     mouse = pygame.mouse.get_pos()
        #     mouseflag = pygame.mouse.get_pressed()
        #     clock.tick(FPS)
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False
        #
        #     button.check_mouse(mouse)
        #     button.draw()
        #     index = button.mousedown(mouseflag,index,len(images)-1)
        #     pygame.time.wait(100)
        #     print('loop2')



    pygame.quit()
