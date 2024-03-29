import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x // 10 * 10, y // 10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210,200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,255))

my_direction = LEFT

clock = pygame.time.Clock()

maçã_pos = on_grid_random()
maçã = pygame.Surface((10,10))
maçã.fill((178,34,34))

while True:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], maçã_pos):
        maçã_pos = on_grid_random()
        snake.append((0,0))

    if my_direction == UP: 
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN: 
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT: 
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT: 
        snake[0] = (snake[0][0] - 10, snake[0][1]) 

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])  


    screen.fill((0,0,0))
    screen.blit(maçã, maçã_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()









