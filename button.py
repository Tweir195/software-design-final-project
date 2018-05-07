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
        self.color = 29,206,159
        self.color2 = 5,127,94
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)
        self.rect.width = 0
        self.onbutton = False

    def draw(self, color=None):
        """ puts 'button' on screen"""
        if self.onbutton == False:
            color = self.color
        else:
            color = self.color2
        self.surf.fill(color)
        pygame.draw.rect(self.surf,color,self.rect)
        view.screen.blit(self.surf,(self.left,self.top))
        pygame.display.update()

    def update(self,flag):
        if flag == True:
            self.draw()

    def check_mouse(self, mousepos):
        """checks to see if the cursor is within the button"""
        if self.left < mousepos[0] < self.left+self.width and self.top < mousepos[1] < self.top+self.height:
            self.onbutton = True
        else:
            self.onbutton = False
    def mousedown(self,mouseflag,index,max):
        """checks to see if the user has clicked on the button"""
        if self.onbutton == True and mouseflag[0] == 1:
            view.screen.fill(pygame.Color(200,200,200))
            if index<max:
                index+=1
        return index
