import pygame

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/cursor.png')
        self.rect = self.image.get_rect(midbottom = (200, 85))
    
    def update(self):
        pass

    def moveToRod(self, rod):
        self.rect.centerx = rod.mid
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)