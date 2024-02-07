import pygame

class Disk():
    def __init__(self, color, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.rectangle = pygame.Rect(0, 0, width, height)
    
    def update(self):
        pass

    def moveAt(self, mid, bottom):
        self.rectangle.midbottom = (mid, bottom)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle, 0, 5)
    
    def putInFocus(self):
        self.rectangle.bottom = 100