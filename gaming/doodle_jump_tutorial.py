#inspired from: https://www.youtube.com/watch?v=qmcgrk5KfHQ
import pygame
pygame.init()

#libraray of game constants
white = (255,255,255)
black = (0,0,0)
gray = (120,120,120)
dull_white = (250,250,250)
WIDTH = 400
HEIGHT = 500
background = dull_white

player = pygame.transform.scale(pygame.image.load('hippo.png'),(90,70))
fps = 60
font = pygame.font.Font('freesansbold.ttf',16)
timer = pygame.time.Clock()

#game variables
player_x = 170
player_y = 400
platforms = [[175,480,70,10]]

#create screen
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Doodle Jumper')

running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player,(player_x,player_y))

    for i in range(len(platforms)):
        block = pygame.draw.rect(screen,black,platforms[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.flip()
pygame.quit()

