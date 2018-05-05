
import pygame
from background import *
view = background()


class real_picture:
    """Adds a real image on the screen with the initial location
    """
    def __init__(self,left, top, width=None, height=None, resize=False):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.resize = resize
        self.spaceflag = True
        self.oldindex = 0

    def draw(self,image):
        image = pygame.image.load(image)
        if self.resize is True:
            self.image = pygame.transform.scale(image, (self.width, self.height))
        else:
            self.image = image
        view.screen.blit(self.image,(self.left,self.top))
        pygame.display.update()

    def update(self,image):
        if self.spaceflag == True:
            self.draw(image)
            self.spaceflag = False
        return self.spaceflag

    def spacedown(self,index,max):
        """Checks if the space bar has been pressed"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.spaceflag = True
        if self.spaceflag == True and index<max:
            index += 1
            if index == max:
                index = 0
            self.oldindex = index
            # print('SPACE',index)
        return self.oldindex
if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    #'images/convobubble.PNG'
    realimage=['images/Australia/A1.jpg','images/Australia/A2.jpg','images/Australia/A3.jpg','images/Australia/A4.jpg',
    'images/Australia/A5.jpg','images/Australia/A6.jpg','images/Australia/A7.jpg','images/Australia/A8.jpg'
    ,'images/Australia/A9.jpg','images/Australia/A10.jpg','images/Australia/A11.jpg','images/Australia/A12.jpg']
    images = ['images/Australia/AustraliaBG.PNG']
    # realimage=['images/Australia/Australia_1.jpg','images/Australia/Australia_2.jpg','images/Australia/Australia_3.jpg','images/Australia/Australia_4.jpg',
    # 'images/Australia/Australia_5.jpg','images/Australia/Australia_6.jpg','images/Australia/Australia_7.jpg','images/Australia/Australia_8.jpg'
    # ,'images/Australia/Australia_9.jpg','images/Australia/Australia_10.jpg','images/Australia/Australia_11.jpg','images/Australia/Australia_12.jpg']
    # images = ['images/Australia/AustraliaBG.PNG']
    index = 0
    i = 0
    running = True
    view.draw(images[index])
    rp = real_picture(100,100,width = 400, height = 300, resize=True)


    while running:



        rp.update(realimage[i])
        i = rp.spacedown(i,len(realimage))
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:
        #             i = i + 1


        clock.tick(40)
