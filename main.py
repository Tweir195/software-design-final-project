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
    """ Lists are full of different elements that must be blited to the screen at different locations, all elements are included so we can cycle through them """

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

    Flint_realimage = ['images/Flint/flint_1.jpeg','images/Flint/flint_2.jpg','images/Flint/flint_3.jpg','images/Flint/flint_4.jpg','images/Flint/flint_5.jpg',
    'images/Flint/flint_6.jpg','images/Flint/flint_7.jpg','images/Flint/flint_8.jpg','images/Flint/flint_9.jpg']
    Flint_text = ['images/Flint/flint_1.png','images/Flint/flint_2.png','images/Flint/flint_3.png','images/Flint/flint_4.png','images/Flint/flint_5.png',
    'images/Flint/flint_6.png','images/Flint/flint_7.png','images/Flint/flint_8.png','images/Flint/flint_9.png']

    Arc_realimage = ['images/Arctic/Arctic_1.jpg','images/Arctic/Arctic_2.jpg','images/Arctic/Arctic_3.jpg','images/Arctic/Arctic_4.jpg','images/Arctic/Arctic_5.jpg',
    'images/Arctic/Arctic_6.jpg','images/Arctic/Arctic_7.jpg','images/Arctic/Arctic_8.jpg','images/Arctic/Arctic_9.jpg',]
    Arc_text = ['images/Arctic/Arctic_1.png','images/Arctic/Arctic_2.png','images/Arctic/Arctic_3.png','images/Arctic/Arctic_4.png','images/Arctic/Arctic_5.png','images/Arctic/Arctic_6.png',
    'images/Arctic/Arctic_7.png','images/Arctic/Arctic_8.png','images/Arctic/Arctic_9.png']

    Bang_realimage = ['images/Bangladesh/Bangladesh_1.jpg','images/Bangladesh/Bangladesh_2.jpg','images/Bangladesh/Bangladesh_3.jpg','images/Bangladesh/Bangladesh_4.jpg','images/Bangladesh/Bangladesh_5.jpg',
    'images/Bangladesh/Bangladesh_6.jpg','images/Bangladesh/Bangladesh_7.JPG','images/Bangladesh/Bangladesh_8.jpg','images/Bangladesh/Bangladesh_9.jpg',
    'images/Bangladesh/Bangladesh_10.jpg','images/Bangladesh/Bangladesh_11.jpg','images/Bangladesh/Bangladesh_12.jpg']
    Bang_text = ['images/Bangladesh/Bangladesh_1.png','images/Bangladesh/Bangladesh_2.png','images/Bangladesh/Bangladesh_3.png','images/Bangladesh/Bangladesh_4.png',
    'images/Bangladesh/Bangladesh_4.png','images/Bangladesh/Bangladesh_5.png','images/Bangladesh/Bangladesh_6.png','images/Bangladesh/Bangladesh_7.png',
    'images/Bangladesh/Bangladesh_8.png','images/Bangladesh/Bangladesh_9.png','images/Bangladesh/Bangladesh_10.png','images/Bangladesh/Bangladesh_11.png',
    'images/Bangladesh/Bangladesh_12.png',]

    background_images = ['images/WelcomeBG.PNG', 'images/Australia/AustraliaBG.PNG','images/North_Atlantic_Gyre/NAGBG.PNG',
    'images/Flint/FlintBG.jpg','images/Arctic/ArcticBG.PNG','images/Bangladesh/BangladeshBG.PNG','images/EndingBG.PNG','images/Credits.PNG'] # list of background images


    running = True
    pausetime = 150
    music = ['music/home.mp3','music/adaytoremember.mp3','music/home.mp3']
    musicindex = 0
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
    """ Adds music to game """
        pygame.mixer.music.load(music[musicindex])
        pygame.mixer.music.play(-1)
        while backindex == 0 and running:
            """Welcome screen"""
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            changepos = boat.animate(0,3,moveflag,False,bob=True)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()
            backindex = button.mousedown(mouseflag,backindex,len(background_images)-1)
            pygame.time.wait(pausetime)
            changepos = False
        moveflag = True
        if running:
    """ Makes sprite bob across screen after you click on the button and before you move to the next location """
            animate_between_pages(moveflag,running)
        pygame.mixer.music.fadeout(400)
        musicindex += 1
        boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images
""" Blits new Background according to index change (Changes locaion on screen) """
        [backindex],width=450,height=550,resize=True)
        moveflag = False
        cb = ConvoBubble(800,0,width=500,height=500,resize=True)
        rp = real_picture(100,50,width = 450, height = 350, resize=True)
        view.draw(background_images[backindex])
        cbindex = 0
        pygame.mixer.music.load(music[musicindex])
        pygame.mixer.music.play(-1)
        while backindex == 1 and running:
            """Australia"""
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
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
            pygame.time.wait(pausetime)
            changepos = False
        moveflag = True
        if running:
            animate_between_pages(moveflag,running)
        cbindex = 0
        view.draw(background_images[backindex])
        cb = ConvoBubble(700,0,width=700,height=700,resize=True)
        boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images[backindex],width=450,height=550,resize=True)
        while backindex == 2 and running:
            """North Atlantic Gyre"""
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
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
            backindex = button.mousedown(mouseflag,backindex,len(background_images)-1)
            pygame.time.wait(pausetime)
            changepos = False
        moveflag = True
        if running:
            animate_between_pages(moveflag,running)
        cbindex = 0
        cb = ConvoBubble(310,-100,width=650,height=650,resize=True)
        rp = real_picture(45,50,width = 400, height = 325, resize=True)
        view.draw(background_images[backindex])
        boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images[backindex],width=450,height=550,resize=True)
        while backindex == 3 and running:
            """Flint"""
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if cbindex == len(Flint_text):
                cbindex = 0
            cb.draw(Flint_text[cbindex])
            rp.draw(Flint_realimage[cbindex])
            backindex = button.mousedown(mouseflag,backindex,len(background_images)-1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        cbindex = cbindex + 1

            changepos = boat.animate(0,3,moveflag,False,bob=True)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()
            pygame.time.wait(pausetime)
            changepos = False
        moveflag = True
        if running:
            animate_between_pages(moveflag,running)
        cbindex = 0
        cb = ConvoBubble(600,100,width=600,height=600,resize=True)
        rp = real_picture(100,50,width = 450, height = 350, resize=True)
        view.draw(background_images[backindex])
        boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images[backindex],width=450,height=550,resize=True)
        while backindex == 4 and running:
            """Arctic"""
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if cbindex == len(Flint_text):
                cbindex = 0
            cb.draw(Arc_text[cbindex])
            rp.draw(Arc_realimage[cbindex])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        cbindex = cbindex + 1

            backindex = button.mousedown(mouseflag,backindex,len(background_images)-1)
            changepos = boat.animate(0,3,moveflag,False,bob=True)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()
            pygame.time.wait(pausetime)
            changepos - False

        moveflag = True
        if running:
            animate_between_pages(moveflag,running)
        cbindex = 0
        cb = ConvoBubble(850,200,width=500,height=500,resize=True)
        rp = real_picture(450,50,width = 450, height = 350, resize=True)
        view.draw(background_images[backindex])
        boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images[backindex],width=450,height=550,resize=True)
        while backindex == 5 and running:
            """Bangladesh"""
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if cbindex == len(Flint_text):
                cbindex = 0
            cb.draw(Bang_text[cbindex])
            rp.draw(Bang_realimage[cbindex])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        cbindex = cbindex + 1

            backindex = button.mousedown(mouseflag,backindex,len(background_images)-1)
            changepos = boat.animate(0,3,moveflag,False,bob=True)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()
            pygame.time.wait(pausetime)
        moveflag = True
        if running:
            animate_between_pages(moveflag,running)
        view.draw(background_images[backindex])
        pygame.mixer.music.fadeout(400)
        musicindex += 1
        pygame.mixer.music.load(music[musicindex])
        pygame.mixer.music.play(-1)
        boat = sprite('images/Quincy.PNG',250, 420,200,430,background_images[backindex],width=450,height=550,resize=True)
        while backindex == 6 and running:
            """End screen"""
            mouse = pygame.mouse.get_pos()
            mouseflag = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            changepos = boat.animate(0,3,moveflag,False,bob=True)
            backindex = button.mousedown(mouseflag,backindex,len(background_images)-1)
            boat.update(changepos)
            button.check_mouse(mouse)
            button.draw()
            pygame.time.wait(pausetime)
        moveflag = True
        if running:
            animate_between_pages(moveflag,running)
        view.draw(background_images[backindex])
        pygame.mixer.music.fadeout(700)
        while backindex == 7 and running:
            """Credits"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.time.wait(100)



    pygame.quit()
