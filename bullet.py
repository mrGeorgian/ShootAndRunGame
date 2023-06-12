import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (10).png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.rect.centerx = gun.rect.centerx+6
        self.rect.bottom = gun.rect.bottom-10
        self.y = self.rect.y

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

    def sp(self, stats):
        if stats.score >= 10:
            self.speed = 5


