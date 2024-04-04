import pygame
import numpy
import random

# Custom Modules
from assets import *
from functionality import *

pygame.init()
########################## SCREEN ################################
screen = pygame.display.set_mode(DIMS)
clock = pygame.time.Clock()

# Game Variables
running = True
can_penetrate_tile = False
score = 0
streak = 0
accelerate_count = 0    # Check whether to increase ball speed
lives = 1
high_score = get_high_score()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, BLUE, player_start)
    # Game borders 
    pygame.draw.rect(screen, WHITE, wall_left)
    pygame.draw.rect(screen, WHITE, wall_right)
    pygame.draw.rect(screen, WHITE, border_top)
    # Game border blue
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, y*79.5, x*1, y*3))
    pygame.draw.rect(screen, BLUE, pygame.Rect(x*62.2, y*79.5, x*1, y*3))

    # Loop generating tiles
    for i in range(4):
        for tile in tile_array[i]:
            pygame.draw.rect(screen, COLORS[i], tile)
    
    # Loop generating colored side tiles
    for i in range(8):
        pygame.draw.rect(screen, side_tiles_colors[i], side_tiles[i])
        
    
    # Pong Ball
    pygame.draw.rect(screen, WHITE, pong)
    pong.move_ip(pong_velocity)
    ######################## Game Functionality #########################
    # Key Events
    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if player.right < 62.2*x:
                player.move_ip(5, 0)
        if keys[pygame.K_LEFT]:
            if player.left > 10:
                player.move_ip(-5, 0)

    # Bouncing off objects / Breaking tiles
    for object in objects:
        if pong.colliderect(object):
            # collision point P
            P = (pong.x, pong.y)
            # Bounce of object by changing velocity
            bounce(P, object, pong_velocity)
            if object == player or object == border_top:
                can_penetrate_tile = True
            for tiles in tile_array:
                if object in tiles:
                    if can_penetrate_tile:
                        score += get_score_gained(object, streak) 
                        streak += 1 
                        accelerate_count +=1
                        tiles.remove(object)
                        objects.remove(object)
                        can_penetrate_tile = False
                        # TODO: Score accumulates if there is a streak
                        print(score)
    
    # Respawn ball if it goes off boundary
    # Move Pong:
    if pong.x > 62.2*x or pong.x < 1*x:
        pong_velocity[0] *= -1

    if pong.y > DIMS[1]:
        pong.x, pong.y = generate_coordinate()
        lives += 1
        streak = 0
        accelerate_count = 0
        pong_velocity = [2, 2]
    
    # Accelerate Pong after every 10 point streak
    if accelerate_count > 1:
        accelerate(pong_velocity)   
        accelerate_count = 0 
    
    # Updates screen
    # Text rendering:
    update_text(screen, score, score_coord)
    update_text(screen, high_score, high_score_coord) 
    update_lives(screen, lives, lives_coord)
    
    pygame.display.flip()
    # limit FPS to 60
    clock.tick(60)

pygame.quit()

