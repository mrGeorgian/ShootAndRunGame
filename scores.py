import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 42)
        self.image_score()
        self.image_guns()

    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (255, 255, 255))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 40
        self.score_rect.top = 530

    def image_guns(self):
        self.guns = Group()
        for gun_number in range(self.stats.guns_left + 1):
            gun = Gun(self.screen)
            gun.rect.x = 550 + gun_number * gun.rect.width
            gun.rect.y = 500
            self.guns.add(gun)

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.guns.draw(self.screen)


