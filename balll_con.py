import pygame
from ball import Ball

balls_data = ({'path': 'pixil-frame-0 (1).png'},
              {'path': 'pixil-frame-0 (2).png'},
              {'path': 'pixil-frame-0 (3).png'})

balls_surf = [pygame.image.load('images/' + data['path']).convert_alpha() for data in balls_data]

def createBall(group):
    W, H = 700, 600
    indx = randint(0, len(balls_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], group)






