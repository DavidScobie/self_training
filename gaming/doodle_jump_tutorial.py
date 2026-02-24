#inspired from: https://www.youtube.com/watch?v=qmcgrk5KfHQ 
import pygame
import random
pygame.init()

#libraray of game constants
white = (255,255,255)
black = (0,0,0)
gray = (120,120,120)
dull_white = (250,250,250)
WIDTH = 400
HEIGHT = 500
background = dull_white
score = 0 #score tracking
high_score = 0
game_over = False
score_last = 0
super_jumps = 2 #2 super jumps allowed per game
jump_last = 0 #tracks the last time you were given a super jump

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

#handle movement of platforms as game progresses
def update_platforms(my_list,y_pos,change):
    global score #make score global as otherwise we'd need to output score from this function (we could do this tho, but it's clunky)
    if y_pos < 250 and change < 0:  #if we are (near the top of the screen) and (moving upwards)
        for i in range (len(my_list)):
            my_list[i][1] -= change #change the y coordinate of the platform
    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(10,320),random.randint(-50,-10),70,10] #randomly assign the x and y position of new platforms
            score += 1 #increase score for player
    return my_list

running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player,(player_x,player_y)) #put the player on the screen
    blocks = []
    high_score_text = font.render('High score:'+ str(high_score), True, black, background) 
    screen.blit(high_score_text, (280,0)) #write high score on the screen
    score_text = font.render('score:'+ str(score), True, black, background) 
    screen.blit(score_text, (320,20)) #write score on the screen
    super_jumps_text = font.render('Super Jumps (Spacebar): ' + str(super_jumps), True, black, background) 
    screen.blit(super_jumps_text, (10,10)) #write score on the screen

    for i in range(len(platforms)):
        block = pygame.draw.rect(screen,black,platforms[i]) #draw the platforms
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #end the game if instructed
            running = False
        if event.type == pygame.KEYDOWN: #if a key is pressed
            if event.key == pygame.K_SPACE and game_over: #if you've fallen and press space then the game resets
                game_over = False
                score = 0
                player_x = 170 #reset position
                player_y = 400
                background = dull_white
                platforms = [[175,480,70,10], [85,370,70,10], [265,370,70,10], [200,260,70,10], [85,150,70,10], [265,150,70,10], [75,40,70,10]] 
                score_last = 0
                super_jumps = 3 #3 not 2 as spacebar is used for restarting the game and jumping
                jump_last = 0
            if event.key == pygame.K_SPACE and not game_over and super_jumps > 0: #super jump
                super_jumps -= 1
                y_change = -15 #slightly higher than a normal jump
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

    if player_y < 440: #dont want the player to fall completely off the screen
        player_y = update_player(player_y)
    else:
        game_over = True
        y_change = 0 #no matter that gravity is effecting player, it will stay at bottom of screen
        x_change = 0 # player stays still if they fall down to the bottom
        reset_game_text = font.render('Press spacebar to play again', True, black, background) 
        screen.blit(reset_game_text, (170,200)) #text to tell player how to restart the game

    platforms = update_platforms(platforms,player_y,y_change)

    if player_x < -20: #stop player going off the sides of the screen
        player_x = -20
    elif player_x > 330:
        player_x = 330

    if x_change > 0: #character moving right (it should face right)
        player = pygame.transform.scale(pygame.image.load('hippo.png'),(90,70))
    elif x_change < 0: #character moving left (it should face left)
        player = pygame.transform.flip(pygame.transform.scale(pygame.image.load('hippo.png'),(90,70)),1,0)

    if score > high_score: #if score is higher than high score then reassign high score
        high_score = score

    if score - score_last > 14: #change the background colour when you exceed a new multiple of 15 platforms
        score_last = score
        background = (random.randint(50,255), random.randint(50,255), random.randint(50,255)) #we dont want to allow the darkest colours

    if score - jump_last > 50: #with every 50 points you are allowed an extra super jump
        jump_last = score
        super_jumps += 1

    pygame.display.flip()
pygame.quit()

