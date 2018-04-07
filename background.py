"""This is the background class for our project, it displays the images we need
for our animation
"""

import pygame

class background(object):
    def __init__(self, images, size=(1280,960)):
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.screen.get_size())
        self.images = images
    def clear_screen(self):
        self.background.fill((0,0,0))
        pygame.display.update()
    def display_image(self, index, x, y):
        image = pygame.image.load(self.images[index])
        self.image = pygame.transform.scale(image, (1280,960))
        self.background.blit(self.image,(x,y))
    def draw(self, index,x,y):
        self.screen.blit(view.background,(0,0))
        self.clear_screen()
        self.display_image(index,x,y)
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    view = background(["Attachment-1.png"], size=(1280,960))
    running = True
    view.screen.blit(view.background,(0,0))
    view.clear_screen()
    view.display_image(0, 0,0)
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        view.draw(0,0,0)
        view.clear_screen()
