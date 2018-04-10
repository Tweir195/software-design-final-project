#This is the main file for our project


import pygame


class background(object):
    def __init__(self, size=(1280,960)):
        self.screen = pygame.display.set_mode(size)
        self.size = size
    def draw(self, image):
        self.screen.fill(pygame.Color(0,0,0))
        load = pygame.image.load(image)
        back_ground = pygame.transform.scale(load, self.size)
        self.screen.blit(back_ground, [0,0])
        pygame.display.update()


class ConvoBubble:
    def __init__(self,color=(200,200,200)):

        self.left = 500
        self.top = 400
        self.width = 200
        self.height = 280
        self.surf = pygame.Surface((self.width,self.height))
        self.color = color
        self.surf.fill(self.color)
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)

    def draw(self,image):
        """ Draws the specified image to the Infocard surface
        image: must be a string """

        """"self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()"""

        c_b = pygame.image.load(image)
        view.screen.blit(c_b,(-400,-200))
        pygame.display.update()

    def text(self,image):
        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()

        info = pygame.image.load(image)
        view.screen.blit(info,(0,0))
        pygame.display.update()

    #def name_draw(self,string):
        #self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        #view.screen.blit(self.surf, self.card)
        #pygame.display.update()
        #name = basicfont.render(string, True, (255, 0, 0), (255,255,255))
        #view.screen.blit(name,self.card)
        #pygame.display.update()

class real_picture:

    def __init__(self,color=(200,200,200)):
        """ Creates a surface to attach the image to """
        self.left = 20
        self.top = 500
        self.width = 400
        self.height = 400
        self.surf = pygame.Surface((self.width,self.height))
        self.color = color
        self.surf.fill(self.color)
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)

    def draw(self,image):
        """ Draws the specified image to the Infocard surface
        image: must be a string """

        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()

        picture = pygame.image.load(image)
        view.screen.blit(picture,self.card)
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    view = background()
    cb = ConvoBubble()



    #view.screen.blit(view.background,(0,0))
    running = True






    while running:
        view.draw("Attachment-1.png")
        cb.draw('convobubble.PNG')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        #view.clear_screen()"""
