W, H = 700, 600

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            gun.rect.centerx -= 5
            if gun.rect.centerx < 0:
                gun.rect.centerx = 0
        elif keys[pygame.K_RIGHT]:
            gun.rect.centerx += 5
            if gun.rect.centerx < 0:
                gun.rect.centerx = 0


def coll(self, platform):
    if self.rect.center >= platform.rect.top:
        self.kill()




def st(stats, sc, bullets):
    for bullet in bullets:
        if coll:
            stats.score += 1
            sc.image_score()


        controls.st(stats, sc, bullets)




def update_balls2(balls):
    balls.update_ball()
    for ball in balls.copy():
        if ball.rect.bottom <= 0:
            balls.remove(ball)



