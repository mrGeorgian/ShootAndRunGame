import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Platform, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (11).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center


    def output1(self):
        self.screen.blit(self.image, self.rect)

    def update_platform(self):
        W, H = 700, 600
        if self.rect.centerx < W:
            self.rect.centerx += 1
        else:
            self.rect.centerx = 0

