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
platforms = [[175,480,70,10], [85,370,70,10], [265,370,70,10], [200,260,70,10], [85,150,70,10], [265,150,70,10], [75,40,70,10]] 
jump = False #is the character jumping?
y_change = 0
x_change = 0
player_speed = 3

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
        if rect_list[i].colliderect([player_x +30, player_y + 60, 30, 5]) and jump == False and y_change > 0:
            j = True #j is jump
    return j

#update y position every loop
def update_player(y_pos):
    global jump 
    global y_change
    jump_height = 10
    gravity = .4 #a greater value of y is lower down in the screen
    if jump:
        y_change = -jump_height #a greater value of y is lower down in the screen
        jump = False
    y_pos += y_change 
    y_change += gravity #this is the kinematics quadratic update
    return y_pos

"""
#handle movement of platforms as game progresses
def update_platforms(my_list,y_pos,change):
    if player_y < 250 and y_change < 0:  #if we are (near the top of the screen) and (moving upwards)
        for i in range (len(my_list)):
            my_list[i][1] -= change
"""

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
        if event.type == pygame.KEYDOWN: #if a key is pressed
            if event.key == pygame.K_LEFT: #if the key 'left' is pressed
                x_change = -player_speed
            if event.key == pygame.K_RIGHT: #if the key 'right' is pressed
                x_change = player_speed
        if event.type == pygame.KEYUP: #if a key is pressed
            if event.key == pygame.K_LEFT: #if the key 'left' is pressed
                x_change = 0
            if event.key == pygame.K_RIGHT: #if the key 'right' is pressed
                x_change = 0

    jump = check_collisions(blocks,jump)
    player_x += x_change
    player_y = update_player(player_y)
    """
    platforms = update_platforms(platforms,player_y,y_change)
    """

    pygame.display.flip()
pygame.quit()

