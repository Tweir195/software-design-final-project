from background import *
view = background()

import pygame
import time

class ConvoBubble:
    """This class takes a location, and forms the converstation bubble
    """
    def __init__(self,image, right_l, left_l):
        self.image = pygame.image.load(image)
        self.rightl = right_l
        self.leftl = left_l

    def draw(self):
        """ Takes a list of convobubble and cycles through them when the space bar is pressed.
        """

        view.screen.blit(self.image,(self.rightl,self.leftl))

        pygame.display.update()
        # font = pygame.font.SysFont('Sans',35)
        # text=font.render('Learning Learning Learning',0,(0,0,0))
        # text_rect=text.get_rect()
        # text_rect.centerx = 350
        # text_rect.centery = 450
        # text_rect.width = 2
        # view.screen.blit(text,text_rect)
        pygame.display.update()
    def text(self,image):
        """Adds text to the bubble
        """
        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display()

        info = pygame.image.load(image)
        view.screen.blit(info,(0,0))
        pygame.display.update()

    #def name_draw(self,string):
        #self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        #view.screen.blit(self.surf, self.card)
        #pygame.display.update()
        #name = basicfont.render(string, True, (255, 0, 0), (255,255,255))
        #view.screen.blit(name,self.card)
        #pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    #'images/convobubble.PNG'
    text_bubble=['images/Australia/Australia_1.png','images/Australia/Australia_2.png','images/Australia/Australia_3.png','images/Australia/Australia_4.png',
    'images/Australia/Australia_5.png','images/Australia/Australia_6.png','images/Australia/Australia_7.png','images/Australia/Australia_8.png'
    ,'images/Australia/Australia_9.png','images/Australia/Australia_10.png','images/Australia/Australia_11.png','images/Australia/Australia_12.png']
    images = ['images/Australia/AustraliaBG.PNG']
    index = 0
    keys=pygame.key.get_pressed()
    if keys[pygame.K_BACKSPACE] == True:
        print('taco')
    #view.draw(images[index])
    # for i in range(len(text_bubble)):
    #     cb = ConvoBubble(text_bubble[i], 100, 100)
    #     cb.draw()
    #     time.sleep()

    #cb.text('images/WelcomeBG.PNG')
    #cb.text(images[1])
#        panama.draw()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
