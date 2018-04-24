from background import *
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
        # font = pygame.font.SysFont('Sans',35)
        # text=font.render('Learning Learning Learning',0,(0,0,0))
        # text_rect=text.get_rect()
        # text_rect.centerx = 350
        # text_rect.centery = 450
        # text_rect.width = 2
        # view.screen.blit(text,text_rect)
        # pygame.display.update()
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

    cb = ConvoBubble('images/convobubble.PNG', -900, -200)
    images = ['images/WelcomeBG.PNG', 'images/Australia/AustraliaBG.PNG']


    index = 0
    view.draw(images[index])
    cb.draw()
    posx = 300
    posy = 300
    position = posx,posy
    font = pygame.font.SysFont('Sans',35)
    if text ==
    info = ['Chicken Nuggets', 'Pollo de Nugget', 'Applesauce','Chicken Noodle Soup']
    for i in range(len(info)):
            font = pygame.font.SysFont('Sans',35)
            text=font.render(i,0,(0,0,0))
            text_rect=text.get_rect()
            text_rect.centerx = 350
            text_rect.centery = 450
            text_rect.width = 2
            view.screen.blit(text,text_rect)
            pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
