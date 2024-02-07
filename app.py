import pygame, keyboard, time, sys
from pygame import mixer

pygame.init()
mixer.init()

win = pygame.display.set_mode((1920,1090))
pygame.display.set_caption("Grand Theft Vääksy")
#pygame.display.set_icon(pygame.image.load("imgs/logo.png").convert)

class Player:
    def __init__(self):
        ...

class Enviroment:
    def __init__(self):
        ...

player = Player()
enviroment = Enviroment()

game = 1

while game:
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            sys.exit()

    pygame.display.flip()