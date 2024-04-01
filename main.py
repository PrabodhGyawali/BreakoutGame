import pygame
import numpy
import random

# Custom Modules
from assets import *
from physics import *

pygame.init()
########################## SCREEN ################################
DIMS = (x*63.2, y*90)
screen = pygame.display.set_mode(DIMS)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, BLUE, player)
    # Game borders 
    pygame.draw.rect(screen, WHITE, wall_left)
    pygame.draw.rect(screen, WHITE, wall_right)
    # Game border blue
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, y*79.5, x*1, y*3))
    pygame.draw.rect(screen, BLUE, pygame.Rect(x*62.2, y*79.5, x*1, y*3))

    # Loop generating tiles
    for i in range(4):
        for tile in tile_array[i]:
            pygame.draw.rect(screen, COLORS[i], tile)
    
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
            for tiles in tile_array:
                if object in tiles:
                    # Check if previous collision was with paddle
                    tiles.remove(object)
                    objects.remove(object)
                    print("tile removed")
    
    # Respawn ball if it goes off boundary
    # Move Pong:
    if pong.y > DIMS[1]:
        pong.x, pong.y = generate_coordinate()
    
            
    # Updates screen
    pygame.display.flip()
    # limit FPS to 60
    clock.tick(60)

pygame.quit()

