#This is the main file for our project
from background import *
from convobubble import *
from realpicture import *
from sprite import *
from button import *

import pygame

def animate_between_pages(moveflag,running):
    """Makes the boat float from one page to the next"""
    rect = pygame.Rect((0,0),(1280,700))
    view.draw(background_images[backindex-1])
    for i in range(50):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        boat.animate(15,4,moveflag,True,bob=True)
        boat.draw()
        pygame.time.wait(100)


if __name__ == "__main__":
    pygame.init()
    view = background()
    cb = ConvoBubble(400, 200,width=300,height=300,resize=True)
    Aus_realimage = ['images/Australia/Australia_1.jpg','images/Australia/Australia_2.jpg','images/Australia/Australia_3.jpg','images/Australia/Australia_4.jpg',
    'images/Australia/Australia_5.jpg','images/Australia/Australia_6.jpg','images/Australia/Australia_7.jpg','images/Australia/Australia_8.jpg'
    ,'images/Australia/Australia_9.jpg','images/Australia/Australia_10.jpg','images/Australia/Australia_11.jpg','images/Australia/Australia_12.jpg']
    Aus_text = ['images/Australia/Australia_1.png','images/Australia/Australia_2.png','images/Australia/Australia_3.png','images/Australia/Australia_4.png',
    'images/Australia/Australia_5.png','images/Australia/Australia_6.png','images/Australia/Australia_7.png','images/Australia/Australia_8.png'
    ,'images/Australia/Australia_9.png','images/Australia/Australia_10.png','images/Australia/Australia_11.png','images/Australia/Australia_12.png'] #convo bubles for australia

    NAG_realimage = ['images/North_Atlantic_Gyre/NAG_1_opt.jpg','images/North_Atlantic_Gyre/NAG_2_opt.jpg','images/North_Atlantic_Gyre/NAG_3_opt.jpg',
    'images/North_Atlantic_Gyre/NAG_4_opt.jpg','images/North_Atlantic_Gyre/NAG_5_opt.jpg','images/North_Atlantic_Gyre/NAG_6_opt.jpg',
    'images/North_Atlantic_Gyre/NAG_7_opt.jpg']
    NAG_text = ['images/North_Atlantic_Gyre/NAG_1.png','images/North_Atlantic_Gyre/NAG_2.png','images/North_Atlantic_Gyre/NAG_3.png','images/North_Atlantic_Gyre/NAG_4.png',
    'images/North_Atlantic_Gyre/NAG_5.png','images/North_Atlantic_Gyre/NAG_6.png','images/North_Atlantic_Gyre/NAG_7.png']

    #Flint_realimage = []
    #Flint_text = []

    background_images = ['images/WelcomeBG.PNG', 'images/Australia/AustraliaBG.PNG','images/North_Atlantic_Gyre/NAGBG.PNG',
    'images/Flint/FlintBG.jpg'] # list of background images


    running = True
    clock = pygame.time.Clock()
    FPS = 15
    button = GoToButton(1100,780)
    cbindex = 0
    cbflag = False
    backindex = 0
    view.draw(background_images[backindex])
    moveflag = False
    boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images[backindex],width=450,height=550,resize=True)
    boat.draw()


    while running: # main program loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        while backindex == 0 and running:
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
            backindex = button.mousedown(mouseflag,backindex,len(background_images)-1)
            pygame.time.wait(100)
            changepos = False
        moveflag = True
        if running:
            animate_between_pages(moveflag,running)
        boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images
        [backindex],width=450,height=550,resize=True)
        moveflag = False
        cb = ConvoBubble(800,0,width=500,height=500,resize=True)
        rp = real_picture(100,50,width = 450, height = 350, resize=True)
        view.draw(background_images[backindex])
        #testpic.update(True)
        cbindex = 0
        while backindex == 1 and running:
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if cbindex == len(Aus_text):
                cbindex = 0
            cb.draw(Aus_text[cbindex])
            rp.draw(Aus_realimage[cbindex])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        cbindex = cbindex + 1

            changepos = boat.animate(0,3,moveflag,False,bob=True)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()
            #cbindex= cb.spacedown(cbindex,len(text))
            #if cb.redraw == True:
                #cb = ConvoBubble(-400, -200,width=300,height=300,resize=True)
                #cb.spaceflag = True
                #cb.update(text[cbindex])
            backindex = button.mousedown(mouseflag,backindex,len(background_images)-1)
            pygame.time.wait(100)
            changepos = False

        cbindex = 0
        view.draw(background_images[backindex])
        boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images[backindex],width=450,height=550,resize=True)
        while backindex == 2 and running:
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if cbindex == len(NAG_text):
                cbindex = 0
            cb.draw(NAG_text[cbindex])
            rp.draw(NAG_realimage[cbindex])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        cbindex = cbindex + 1

            changepos = boat.animate(0,3,moveflag,False,bob=True)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()

            #cbindex= cb.spacedown(cbindex,len(text))
            #if cb.redraw == True:
                #cb = ConvoBubble(-400, -200,width=300,height=300,resize=True)
                #cb.spaceflag = True
                #cb.update(text[cbindex])
            backindex = button.mousedown(mouseflag,backindex,len(background_images)-1)
            pygame.time.wait(100)
            changepos = False

        cbindex = 0
        cb = ConvoBubble(850,300,width=500,height=500,resize=True)
        view.draw(background_images[backindex])
        boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images[backindex],width=450,height=550,resize=True)
        while backindex == 3 and running:
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if cbindex == len(NAG_text):
                cbindex = 0
            cb.draw(NAG_text[cbindex])
            rp.draw(NAG_realimage[cbindex])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        cbindex = cbindex + 1

            changepos = boat.animate(0,3,moveflag,False,bob=True)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()
        # view.draw(images[index])
        # boat.draw()
        # while index == 2 and running:
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
