from background import *
view = background()

import pygame

class real_picture:
    """Adds a real image on the screen with the initial location
    """
    def __init__(self,image, right_l, left_l):
        self.image = pygame.image.load(image)
        self.rightl = right_l
        self.leftl = left_l
    def draw(self):
        """ intserts real image onto screen"""
        view.screen.blit(self.image,(self.rightl,self.leftl))
        pygame.display.update()
