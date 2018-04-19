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
    cat = sprite('images/cat-grumpy-icon.png',20,200)
    boat = sprite('images/Quincy.PNG',100, 100,width=250,height=300,resize=True)
    button = GoToButton(1100,780)
    images = ['images/Attachment-1.png']

    running = True
    clock = pygame.time.Clock()
    FPS = 15

    index = 0
    view.draw(images[index])
    cb.draw()
    panama.draw()


    while running: # main program loop
        mouse = pygame.mouse.get_pos()
        mouseflag = pygame.mouse.get_pressed()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        cat.animate(6,3,bob=True)
        boat.animate(6,3,bob=True)
        view.screen.fill(pygame.Color(60,0,245)) # make the background
        cat.draw()
        boat.draw()
        button.check_mouse(mouse)
        button.draw()
        button.mousedown(mouseflag)
        pygame.time.wait(100)



    pygame.quit()
