import pygame
from pygame import *
import random
import math

pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('sky.png')

# Background_sound
mixer.music.load('wind1.wav')
mixer.music.play(-1)

# icon
pygame.display.set_caption("Flying Dart")
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('dart1.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# dart
dartImg = []
dartX = []
dartY = []
dartX_change = []
dartY_change = []
num_of_darts = 6

for i in range(num_of_darts):
    dartImg.append(pygame.image.load('logo2.png'))
    dartX.append(random.randint(0, 735))
    dartY.append(random.randint(50, 150))
    dartX_change.append(2)
    dartY_change.append(20)

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

# You win text
win_font = pygame.font.Font('freesansbold.ttf', 72)

# Play again text
#again_font = pygame.font.Font('freesansbold.ttf', 32)


# functions
def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def winning_text():
    win_text = win_font.render("YOU WON", True, (0, 255, 255))
    screen.blit(win_text, (200, 250))


#def play_again_text():
   # pagain_text = again_font.render("Press 'P' to play again", True, (0, 255, 255))
    #screen.blit(pagain_text, (200, 350))


def player(x, y):
    screen.blit(playerImg, (x, y))


def dart(x, y, i):
    screen.blit(dartImg[i], (x, y))


def isCollision(dartX, dartY, playerX, playerY):
    distance = math.sqrt((math.pow(dartX - playerX, 2)) + (math.pow(dartY - playerY, 2)))
    if distance < 10:
        return True
    else:
        return False


# while loop
running = True
while running:
    screen.fill((128, 128, 128))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # player keystrokes
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        if event.key == pygame.K_UP:
            playerY_change = -5
        if event.key == pygame.K_DOWN:
            playerY_change = 5
        if event.key == pygame.K_q:
            running = False

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0

    # Checking For Boundaries of rabbit
    playerX += playerX_change
    playerY += playerY_change
    # issue with top corners !

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Checking for dart's boundaries
    for i in range(num_of_darts):

        # You won
        if score_value == 100:
            for a in range(num_of_darts):
                dartY[a] = 1500
            winning_text()
            mixer.music.stop()
            fire_sound = mixer.Sound('fireworks.ogg')
            fire_sound.play(-1)
            break

        # GAme over
        if dartY[i] > 500:
            for j in range(num_of_darts):
                dartY[j] = 2000
            game_over_text()
            mixer.music.stop()
            #play_again_text()
            break

        dartX[i] += dartX_change[i]

        if dartX[i] <= 0:
            dartX_change[i] = 2
            dartY[i] += dartY_change[i]
        elif dartX[i] >= 736:
            dartX_change[i] = -2
            dartY[i] += dartY_change[i]

            # collision
        collision = isCollision(dartX[i], dartY[i], playerX, playerY)
        if collision:
            explosion_sound = mixer.Sound("whoosh1.wav")
            explosion_sound.play()

            score_value += 1

            dartX[i] = random.randint(0, 735)
            dartY[i] = random.randint(50, 150)

        dart(dartX[i], dartY[i], i)

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
