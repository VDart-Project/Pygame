import random
import math
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('gaaa.png')

pygame.display.set_caption("Dino Run")
icon = pygame.image.load('fossil.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('dino.png')
playerx = 50
playery = 200
playery_change = 0

cactusimg = []
cactusx = []
cactusy = []
cactusx_change = []
num_of_cactus = 4

for i in range(num_of_cactus):
    cactusimg.append(pygame.image.load('cat.png'))
    cactusx.append(random.randint(400, 736))
    cactusy.append(random.randint(36, 450))
    cactusx_change.append(3)

fireimg = pygame.image.load('r.png')
firex = 0
firey = 200
firex_change = 50
firey_change = 0
fire_state = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textx = 10
texty = 10
# game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render(" GAME OVER:" + str(score_value), True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerimg, (x, y))


def cactus(x, y, i):
    screen.blit(cactusimg[i], (x, y))


def fire_fire(x, y):
    global fire_state
    fire_state = "fire"
    screen.blit(fireimg, (x + 16, y + 10))


def iscollision(cactusx, cactusy, firex, firey):
    distance = math.sqrt((math.pow(cactusx - firex, 2)) + (math.pow(cactusy - firey, 2)))
    if distance < 35:
        return True
    else:
        return False


running = True
while running:
    screen.fill((128, 128, 128))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playery_change = -8
            if event.key == pygame.K_DOWN:
                playery_change = +8
            if event.key == pygame.K_SPACE:
                if fire_state is "ready":
                    firey = playery
                    fire_fire(firex, firey)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playery_change = 0

    playery += playery_change

    if playery <= 36:
        playery = 36
    elif playery >= 450:
        playery = 450

    if firex >= 800:
        firex = 150
        fire_state = "ready"

    if fire_state is "fire":
        fire_fire(firex, firey)
        firex += firex_change

    collision = iscollision(firex, firey, cactusx[i], cactusy[i], )
    if collision:
        firex = 150
        fire_state = "ready"
        score_value += 1
        cactusx[i] = random.randint(400, 736)
        cactusy[i] = random.randint(36, 450)
    for i in range(num_of_cactus):
        if cactusx[i] < 50:
            for j in range(num_of_cactus):
                cactusx[j] = 2000
            game_over_text()
            break

        cactusx[i] += cactusx_change[i]

        cactusx_change[i] = -2.4
        collision = iscollision(firex, firey, cactusx[i], cactusy[i], )
        if collision:
            firex = 150
            fire_state = "ready"
            score_value += 1
            cactusx[i] = random.randint(400, 736)
            cactusy[i] = random.randint(36, 450)
        cactus(cactusx[i], cactusy[i], i)

    player(playerx, playery)
    show_score(textx, texty)

    pygame.display.update()
