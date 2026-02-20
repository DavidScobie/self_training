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
jump = False #is the character jumping?
y_change = 0

#create screen
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Hippo Jumper')

#check for collision with blocks
def check_collisions(rect_list,j):
    global player_x
    global player_y
    global y_change
    #for each platform, is it: (colliding with our player) while the (player is not jumping) and the (player is falling down)?
    for i in range (len(rect_list)): 
        if rect_list[i].colliderect([player_x, player_y + 60, 90, 10]) and jump == False and y_change > 0:
            j = True #j is jump
    return j

#update y position every loop
def update_player(y_pos):
    global jump 
    global y_change
    jump_height = 10
    gravity = 1 #a greater value of y is lower down in the screen
    if jump:
        y_change -= jump_height #a greater value of y is lower down in the screen
        jump = False
    y_pos += y_change 
    y_change += gravity #this is the kinematics quadratic update
    return y_pos


running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player,(player_x,player_y)) #put the player on the screen
    blocks = []

    for i in range(len(platforms)):
        block = pygame.draw.rect(screen,black,platforms[i]) #draw the platforms
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #end the game if instructed
            running = False

    player_y = update_player(player_y)
    jump = check_collisions(blocks,jump)

    pygame.display.flip()
pygame.quit()

