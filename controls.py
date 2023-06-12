import pygame, sys
from bullet import Bullet
from ball import Ball


def events(screen, gun, bullets, balls):
    pygame.time.set_timer(pygame.USEREVENT, 2000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                new_ball = Ball(screen)
                balls.add(new_ball)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                gun.mleft = False
            elif event.key == pygame.K_RIGHT:
                gun.mright = False


def update(bg_color, screen, stats, sc, gun, platform, bullets, balls):
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        bullet.sp(stats)
    for balls in balls.sprites():
        balls.draw_ball()


    gun.output()
    platform.output1()
    pygame.display.flip()


def bullets_kill(bullets):
    bullets.empty()

def balls_kill(balls):
    balls.empty()

def gun_kill(stats, sc):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
    else:
        stats.run_game = False
        sys.exit()


def update_bullets(bullets):
    W, H = 700, 600
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.top >= H:
            bullets.remove(bullet)
    #print(len(bullets))


def update_balls(balls, sc):
    balls.update()
    sc.image_guns()
    for ball in balls.copy():
        if ball.rect.bottom <= 0:
            balls.remove(ball)
    #print(len(balls))



def coll(platform, stats, sc,  bullets):
    if pygame.sprite.spritecollideany(platform, bullets):
        stats.score += 1
        sc.image_score()

        bullets_kill(bullets)



def coll2(gun, stats, sc, balls):
    if pygame.sprite.spritecollideany(gun, balls):
        gun_kill(stats, sc)
        balls_kill(balls)
