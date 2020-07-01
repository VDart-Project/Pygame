import random

import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Super Dope Game Simulator")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
background = pygame.image.load('pygame_background.png')

playerImg = pygame.image.load('vdart_logo.png')
#heell
playerX = 80
playerY = 220
vel = 10

asteroidImg = []
asteroidX = []
asteroidY = []
asteroidX_change = []
asteroidY_change = []
num_asteroid = 2

for i in range(num_asteroid):
    asteroidImg.append(pygame.image.load('asteroid.png'))
    asteroidX.append(random.randint(550, 700))
    asteroidY.append(random.randint(0, 400))
    asteroidX_change.append(2)
    asteroidY_change.append(0)



def player(x, y):
    screen.blit(playerImg, (x, y))

def asteroid(x: object, y: object) -> object:
    screen.blit(asteroidImg[i], (x, y))

running_game = True
while running_game:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        playerY -= vel
    if keys[pygame.K_DOWN]:
        playerY += vel

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    if playerY <= 0:
        playerY = 0
    elif playerY >= 566:
        playerY = 566

    for i in range(num_asteroid):
        asteroidX[i] += asteroidX_change[i]
        if asteroidX[i] <= 0:
            asteroidX_change[i] = -7
        elif asteroidX[i] >= 467:
            asteroidX_change[i] = -7

    player(playerX, playerY)
    asteroid(asteroidX[i], asteroidY[i])
    pygame.display.update()
