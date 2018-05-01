from background import *
view = background()

import pygame

class sprite:
    """Creates an image that can be moved across the screen
    """
    def __init__(self,image, x, y, swidth, sheight, backing, width=None, height=None, resize=False):
        backing = pygame.image.load(backing)
        self.backimage = pygame.transform.scale(backing, (1280,960))
        image = pygame.image.load(image)
        if resize is True:
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.image = image
        self.surf = pygame.Surface([swidth,sheight], pygame.SRCALPHA)
        self.surf.fill((255,255,255,0))
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.state = 0
        crop_rect = (self.x, self.y, swidth, sheight)
        self.backing = self.backimage.subsurface(crop_rect)
        self.longflag = False
        long_rect = (self.x, self.y, 1280-self.x, sheight)
        self.backing_long = self.backimage.subsurface(long_rect)
        self.surf_long = pygame.Surface([1280-self.x,sheight], pygame.SRCALPHA)
    def draw(self):
        """ inserts real image onto screen"""
        if self.longflag == True:
            self.surf_long.blit(self.backing_long,(0,0))
            self.surf_long.blit(self.image,(-120+self.dx,-80+self.dy))
            print(self.surf_long.get_size())
            view.screen.blit(self.surf_long,(self.x,self.y))
            self.longflag = False
        else:
            self.surf.blit(self.backing,(0,0))
            self.surf.blit(self.image,(-120+self.dx,-80+self.dy))
            print(self.surf.get_size())
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
    # def update_backing(self,newx,newy):
    #     crop_rect = ((newx, newy), self.surf.get_size())
    #     cropped = self.backimage.subsurface(crop_rect)
    #     self.backing = cropped
    # def animate_surf(self, offx, offy, moveflag, bob=False):
    #     """Moves surface across the screen, with offx and offy as the distance
    #     in each flip"""
    #     if moveflag == False:
    #         self.x = self.x
    #     else:
    #         self.x += offx
    #     if bob == False:
    #         self.y = self.y
    #     else:
    #         uplist = [0,1,2,3,4,15,16,17,18,19]
    #         downlist = [5,6,7,8,9,10,11,12,13,14]
    #         if self.state in uplist:
    #             self.y -= offy
    #         elif self.state in downlist:
    #             self.y += offy
    #         if self.state == uplist[-1]:
    #             self.state = 0
    #         else:
    #             self.state += 1
    #     self.longflag = True
    #     return True

    def animate(self, offx, offy, moveflag, longflag, bob=False):
        """Moves image on the surface, with offx and offy as the distance
        in each flip"""
        if moveflag == False:
            self.dx = 0
        else:
            self.dx += offx
        if bob == False:
            self.dy = 0
        else:
            uplist = [0,1,2,3,4,15,16,17,18,19]
            downlist = [5,6,7,8,9,10,11,12,13,14]
            # uplist = [0,3]
            # downlist = [1,2]
            if self.state in uplist:
                self.dy += -offy
            elif self.state in downlist:
                self.dy += offy
            if self.state == uplist[-1]:
            # if self.state == 3:
                self.state = 0
            else:
                self.state += 1
        self.longflag = longflag
        return True
