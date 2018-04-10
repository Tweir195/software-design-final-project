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
    def __init__(self,image, right_l, left_l):
        self.image = pygame.image.load(image)
        self.rightl = right_l
        self.leftl = left_l
    def draw(self):
        """ Draws a base convobubble so text can be blited on."""

        view.screen.blit(self.image,(self.rightl,self.leftl))
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


    def __init__(self,image, right_l, left_l):
        self.image = pygame.image.load(image)
        self.rightl = right_l
        self.leftl = left_l
    def draw(self):
        """ intserts real image onto screen"""
        view.screen.blit(self.image,(self.rightl,self.leftl))
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    view = background()
    cb = ConvoBubble('convobubble.PNG', -400, -200)
    panama = real_picture('panama.jpg', 300, 100)



    #view.screen.blit(view.background,(0,0))
    running = True





    view.draw("Attachment-1.png")
    cb.draw()
    panama.draw()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        #view.clear_screen()"""
