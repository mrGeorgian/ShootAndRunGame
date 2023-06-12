import pygame
from random import randrange


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (15).png')
        self.rect = self.image.get_rect()
        self.speed = 1.5
        self.screen_rect = screen.get_rect()
        self.rect.centerx = randrange(700)
        self.rect.bottom = self.screen_rect.bottom
        self.y = float(self.rect.y)



    def update(self):
        self.y -= self.speed
        self.rect.y = self.y


    def draw_ball(self):
        self.screen.blit(self.image, self.rect)
