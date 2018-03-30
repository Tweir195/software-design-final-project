"""
Authors: Emily Nasiff, Andrew Schnurr

Description: Class that creates text boxs that blit onto the backgroud after a spacebar click from the user.
"""

class textbox:
     """ Imports an image of a textbox full of facts for each location and places that onto the screen """
    def __init__(self,color=(200,200,200)):
        """ Creates a surface to attach the image to """
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

        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()

        info = pygame.image.load(image)
        view.screen.blit(info,self.card)
        pygame.display.update()

class real_picture:
     """ Imports a real life image of the location to be displayed across from the textbox """
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

        info = pygame.image.load(image)
        view.screen.blit(info,self.card)
        pygame.display.update()
