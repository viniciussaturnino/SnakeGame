import pygame, random
from pygame.locals import *

#Função para alinhamento da maçã em posições multiplos de 10px
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return(x//10 *10, y//10 *10)

def collision(c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

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
apple_position = on_grid_random()

#direção inicial para a cobra
direcao = left

clock = pygame.time.Clock()

#Gameloop
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        #Controle dos movimentos atraves das teclas
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direcao = up
            if event.key == K_DOWN:
                direcao = down
            if event.key == K_RIGHT:
                direcao = right
            if event.key == K_LEFT:
                direcao = left

    if collision(snake[0], apple_position):
        apple_position = on_grid_random()
        snake.append((0,0))

    for i in range(len(snake)-1,0,-1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #Movimentos da cobra
    if direcao == up:
        snake[0] = (snake[0][0], snake[0][1]-10)
    if direcao == down:
        snake[0] = (snake[0][0], snake[0][1]+10)
    if direcao == right:
        snake[0] = (snake[0][0]+10, snake[0][1])
    if direcao == left:
        snake[0] = (snake[0][0]-10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_position)
    for pos in snake:
        screen.blit(snake_skin, pos)
    pygame.display.update()
