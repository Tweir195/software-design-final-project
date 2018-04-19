from background import *
view = background()

import pygame

class sprite:
    """Creates an image that can be moved across the screen
    """
    def __init__(self,image, x, y, width=None, height=None, resize=False):
        image = pygame.image.load(image)
        if resize is True:
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.image = image
        self.x = x
        self.y = y
        self.state = 0
    def draw(self):
        """ intserts real image onto screen"""
        view.screen.blit(self.image,(self.x,self.y))
        pygame.display.update()
    def animate(self, offx, offy, moveflag, bob=False):
        """Moves image across the screen, with offx and offy as the distance
        in each flip"""
        if bob == False:
            self.y += offy
            if moveflag == False:
                self.x = self.x
            else:
                self.x += offx
        else:
            if moveflag == False:
                self.x = self.x
            else:
                self.x += offx
            uplist = [0,1,2,3,4,15,16,17,18,19]
            downlist = [5,6,7,8,9,10,11,12,13,14,]
            if self.state in uplist:
                self.y -= offy
            elif self.state in downlist:
                self.y += offy
            if self.state == 19:
                self.state = 0
            else:
                self.state += 1
