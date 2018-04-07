class GoToButton(object):
    """ Places image at the specified location to represent a click zone
    that takes you to new location"
    .

    Location: string with name of Location it takes yo to
    left: leftmost coordinate
    top: topmost coordinate
    width: distance from left
    height: distance from top
    """
    def __init__(self, location, left, top, width = 20, height = 20):
        self.location = location
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.surf = pygame.Surface((self.width,self.height))
        self.color = 255,0,0
        self.surf.fill(self.color)
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)
        self.rect.width = 0
