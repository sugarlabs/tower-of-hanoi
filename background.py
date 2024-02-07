import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, screen, state):
        super().__init__()
        self.screen = screen
        self.change_state(state)
        self.rect = self.image.get_rect(topleft = (0, 0))
    
    def change_state(self, state):
        if state == "instructions":
            self.image = pygame.image.load('./assets/instructions-background.png')
        else:
            self.image = pygame.image.load('./assets/running-background.png')

    def update(self):
        pass

    def resize(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))