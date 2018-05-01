from background import *
view = background()

import pygame
import time

class ConvoBubble:
    """This class takes a location, and forms the converstation bubble
    """
    def __init__(self,image, left, top,width=None,height=None,resize=False):
        image = pygame.image.load(image)
        if resize is True:
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.image = image
        self.left = left
        self.top = top

    def draw(self):
        """ Takes a list of convobubble and cycles through them when the space bar is pressed.
        """
        view.screen.blit(self.image,(self.left,self.top))

        pygame.display.update()
        # font = pygame.font.SysFont('Sans',35)
        # text=font.render('Learning Learning Learning',0,(0,0,0))
        # text_rect=text.get_rect()
        # text_rect.centerx = 350
        # text_rect.centery = 450
        # text_rect.width = 2
        # view.screen.blit(text,text_rect)
        #pygame.display.update()
    def update(self,flag):
        if flag == True:
            self.draw()
    def text(self,image):
        """Adds text to the bubble
        """
        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display()

        info = pygame.image.load(image)
        view.screen.blit(info,(0,0))
        pygame.display.update()

    def next_text(self,i):
        flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i = i + 1
                    flag = True
        return i,flag

    #def name_draw(self,string):
        #self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        #view.screen.blit(self.surf, self.card)
        #pygame.display.update()
        #name = basicfont.render(string, True, (255, 0, 0), (255,255,255))
        #view.screen.blit(name,self.card)
        #pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    #'images/convobubble.PNG'
    text_bubble=['images/Australia/Australia_1.png','images/Australia/Australia_2.png','images/Australia/Australia_3.png','images/Australia/Australia_4.png',
    'images/Australia/Australia_5.png','images/Australia/Australia_6.png','images/Australia/Australia_7.png','images/Australia/Australia_8.png'
    ,'images/Australia/Australia_9.png','images/Australia/Australia_10.png','images/Australia/Australia_11.png','images/Australia/Australia_12.png']
    images = ['images/Australia/AustraliaBG.PNG']
    index = 0
    i = 0
    running = True
    view.draw(images[index])
    while running:


        cb = ConvoBubble(text_bubble[i],700,-100,600,600,True)

        cb.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i = i + 1


        clock.tick(40)

    #view.draw(images[index])
    # for i in range(len(text_bubble)):
    #     cb = ConvoBubble(text_bubble[i], 100, 100)
    #     cb.draw()
    #     time.sleep()

    #cb.text('images/WelcomeBG.PNG')
    #cb.text(images[1])
#        panama.draw()
