import pygame, random
from pygame.locals import *

up = 0
right = 1
down = 2
left = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

#Cobra
snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((128,0,128))

#Maçã
apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_position = (random.randint(0,590), random.randint(0,590))

direcao = left

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    screen.blit(apple, apple_position)
    for pos in snake:
        screen.blit(snake_skin, pos)
    pygame.display.update()
