
import pygame
from background import *
view = background()


class real_picture:
    """Adds a real image on the screen with the initial location
    """
    def __init__(self, image, left, top, width=None, height=None, resize=False):
        image = pygame.image.load(image)
        if resize is True:
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.image = image
        self.left = left
        self.top = top
    def draw(self):
        """ intserts real image onto screen"""
        view.screen.blit(self.image, (self.left, self.top))
        pygame.display.update()
