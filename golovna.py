import pygame, controls
from gun import Gun
from stats import Stats
from platform import Platform
from scores import Scores
from pygame.sprite import Group


def run():
    pygame.init()
    W, H = 700, 600
    screen = pygame.display.set_mode((W, H))
    bg_color = (255, 255, 255)
    gun = Gun(screen)
    bullets = Group()
    balls = Group()
    platform = Platform(screen)
    stats = Stats()
    sc = Scores(screen, stats)


    while 1:
        controls.events(screen,  gun, bullets, balls)
        if stats.run_game:
            gun.update_gun()
            platform.update_platform()
            controls.update(bg_color, screen, stats, sc, gun, platform, bullets, balls)
            controls.update_bullets(bullets)
            controls.update_balls(balls, sc)
            controls.coll(platform, stats, sc, bullets)
            controls.coll2(gun, stats, sc, balls)

run()