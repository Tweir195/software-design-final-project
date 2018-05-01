
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
        """ Takes a list of images and cycles through them when the space bar is pressed.
        """


        view.screen.blit(self.image,(self.left,self.top))

        pygame.display.update()

    def update(self,flag):
        if flag == True:
            self.draw()

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    #'images/convobubble.PNG'
    realimage=['images/Australia/Australia_1.jpg','images/Australia/Australia_2.jpg','images/Australia/Australia_3.jpg','images/Australia/Australia_4.jpg',
    'images/Australia/Australia_5.jpg','images/Australia/Australia_6.jpg','images/Australia/Australia_7.jpg','images/Australia/Australia_8.jpg'
    ,'images/Australia/Australia_9.jpg','images/Australia/Australia_10.jpg','images/Australia/Australia_11.jpg','images/Australia/Australia_12.jpg']
    images = ['images/Australia/AustraliaBG.PNG']
    index = 0
    i = 0
    running = True
    view.draw(images[index])
    while running:


        rp = real_picture(realimage[i],0,0)

        rp.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i = i + 1


        clock.tick(40)
