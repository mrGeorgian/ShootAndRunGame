import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (9).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        self.mleft = False
        self.mright = False



    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
        elif self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1




