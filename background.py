
import pygame

class background(object):
    """This class takes a size, creates a pygame window, and
    puts an image on the screen
    """
    def __init__(self, size=(1280,960)):
        self.screen = pygame.display.set_mode(size)
        self.size = size
    def draw(self, image):
        """Draws the background on the screen
        """
        self.screen.fill(pygame.Color(0,0,0))
        load = pygame.image.load(image)
        back_ground = pygame.transform.scale(load, self.size)
        self.screen.blit(back_ground, [0,0])
        pygame.display.update()
    def update(self,flag):
        if flag == True:
            self.draw()
