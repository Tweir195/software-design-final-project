from background import *
view = background()

import pygame

class GoToButton(object):
    """ Places image at the specified location to represent a click zone
    that takes you to new location"

    left: leftmost coordinate
    top: topmost coordinate
    width: distance from left
    height: distance from top
    """
    def __init__(self, left, top, width = 100, height = 50):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.surf = pygame.Surface((self.width,self.height))
        self.color = 255,0,0
        self.surf.fill(self.color)
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)
        self.rect.width = 0

    def draw(self):
        """ puts 'button' on screen"""
        button = pygame.draw.rect(self.surf,self.color,self.rect)
        view.screen.blit(self.surf,(self.left,self.top))
        pygame.display.update()

    def check_mouse(self, mouse, color):
        """checks to see if the cursor is within the button"""
        if self.left < mouse < self.left+self.width and self.top < mouse < self.top+self.height:
            self.color = color
