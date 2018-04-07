"""
Authors: Emily Nasiff, Andrew Schnurr

Description: Class that creates text boxs that blit onto the backgroud after a spacebar click from the user.
"""
import pygame

basicfont = pygame.font,SysFont(None, 48)



class ConvoBubble:
    def __init__(self,color=(200,200,200)):

        self.left = 500
        self.top = 400
        self.width = 200
        self.height = 280
        self.surf = pygame.Surface((self.width,self.height))
        self.color = color
        self.surf.fill(self.color)
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)

    def draw(self,image):
        """ Draws the specified image to the Infocard surface
        image: must be a string """

        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()

        info = pygame.image.load(image)
        view.screen.blit(info,self.card)
        pygame.display.update()

    def text(self,image):
        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()

        info = pygame.image.load(image)
        view.screen.blit(info,self.card)
        pygame.display.update()

    def name_draw(self,string):
        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()
        name = basicfont.render(string, True, (255, 0, 0), (255,255,255))
        view.screen.blit(name,self.card)
        pygame.display.update()

class real_picture:

    def __init__(self,color=(200,200,200)):
        """ Creates a surface to attach the image to """
        self.left = 20
        self.top = 500
        self.width = 400
        self.height = 400
        self.surf = pygame.Surface((self.width,self.height))
        self.color = color
        self.surf.fill(self.color)
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)

    def draw(self,image):
        """ Draws the specified image to the Infocard surface
        image: must be a string """

        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()

        picture = pygame.image.load(image)
        view.screen.blit(picture,self.card)
        pygame.display.update()

cb = ConvoBubble()
cb.draw('ConvoBubble.jpg')
