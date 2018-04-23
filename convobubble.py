pytfrom background import *
view = background()

import pygame

class ConvoBubble:
    """This class takes a location, and forms the converstation bubble
    """
    def __init__(self,image, right_l, left_l):
        self.image = pygame.image.load(image)
        self.rightl = right_l
        self.leftl = left_l

    def draw(self):
        """ Draws a base convobubble so text can be blited on.
        """

        view.screen.blit(self.image,(self.rightl,self.leftl))
        pygame.display.update()

    def text(self,image):t *
view = background()

import pygame

class ConvoBubble:
    """This class takes a location, and forms the converstation bubble
    """
    def __init__(self,image, right_l, left_l):
        self.image = pygame.image.load(image)
        self.rightl = right_l
        self.leftl = left_l

    def draw(self):
        """ Draws a base convobubble so text can be blited on.
        """

        view.screen.blit(self.image,(self.rightl,self.leftl))
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

    running = True
    while running:
        load = pygame.image.load('images/WelcomeBG.PNG')
        view.screen.blit(load, [0,0])
        cb = ConvoBubble('images/convobubble.PNG', -900, -200)
        images = ['images/WelcomeBG.PNG', 'images/Australia/AustraliaBG.PNG']


        index = 0
        view.draw(images[index])
        cb.draw()
        #cb.text(images[1])
#        panama.draw()
    if event.type ==pygame.QUIT:
        running = False
