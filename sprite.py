from background import *
view = background()

import pygame

class sprite:
    """Creates an image that can be moved across the screen
    """
    def __init__(self,image, x, y, swidth, sheight, backing, width=None, height=None, resize=False):
        back = pygame.image.load(backing)
        image = pygame.image.load(image)
        if resize is True:
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.image = image
        self.surf = pygame.Surface([swidth,sheight], pygame.SRCALPHA)
        self.surf.fill((255,255,255,128))
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.state = 0
        crop_rect = (self.x, self.y, swidth, sheight)
        cropped = back.subsurface(crop_rect)
        self.backing = cropped
    def draw(self):
        """ intserts real image onto screen"""
        self.surf.blit(self.backing,(0,0))
        self.surf.blit(self.image,(-120+self.dx,-100+self.dy))
        view.screen.blit(self.surf,(self.x,self.y))
        pygame.display.update()
    def update(self,flag):
        if flag == True:
            self.draw()
    # def move(self):
    #     self.image.scroll(self.dx,self.dy)
        # self.surf.blit(self.image,(-120,-100))
        # view.screen.blit(self.surf,(self.x,self.y))
        # pygame.display.update()
    def animate(self, offx, offy, moveflag, bob=False):
        """Moves image across the screen, with offx and offy as the distance
        in each flip"""
        if moveflag == False:
            self.x = self.x
        else:
            self.x += offx
        if bob == False:
            self.y += offy
        else:
            uplist = [0,1,2,3,4,15,16,17,18,19]
            downlist = [5,6,7,8,9,10,11,12,13,14]
            if self.state in uplist:
                self.y -= offy
            elif self.state in downlist:
                self.y += offy
            if self.state == 19:
                self.state = 0
            else:
                self.state += 1
        return True

    def animate_surf(self, offx, offy, moveflag, bob=False):
        """Moves image across the screen, with offx and offy as the distance
        in each flip"""
        if moveflag == False:
            self.dx = 0
        else:
            self.dx = offx
        if bob == False:
            self.dy = 0
        else:
            uplist = [0,1,2,3,4,15,16,17,18,19]
            downlist = [5,6,7,8,9,10,11,12,13,14]
            if self.state in uplist:
                self.dy = -offy
            elif self.state in downlist:
                self.dy = offy
            if self.state == 19:
                self.state = 0
            else:
                self.state += 1
        return True
