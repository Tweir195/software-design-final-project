"""This is the background class for our project, it displays the images we need
for our animation
"""

import pygame

class background(object):
    def __init__(self, images, size=(1280,960)):
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.screen.get_size())
        self.images = images
    def display_image(self, index):
        image = pygame.image.load(self.images[index])
        self.image = pygame.transform.scale(image, (1280,960))

if __name__ == "__main__":
    pygame.init()
    view = background(["example1.png"], size=(1280,960))
    view.display_image(0)
    running = True
    view.screen.blit(view.background,(0,0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
