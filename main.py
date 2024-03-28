import pygame
import numpy

# Custom Modules
from assets import *

pygame.init()
########################## SCREEN ################################
# Screen_width = (30 * 14) + tilespacing + 40
screen = pygame.display.set_mode((x*63.2, y*90))
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

    ######################## Game Functionality #########################
    # Key Events
    if event.type == pygame.KEYDOWN:
        key=pygame.key.name(event.key)
        if key == "right":
            if player.right < 62.2*x:
                player.move_ip(5, 0)
        if key == "left":
            if player.left > 10:
                player.move_ip(-5, 0)
    
    # Move Pong:
    pygame.draw.rect(screen, WHITE, pong)
    pong.move_ip(pong_velocity)

    # Bouncing off objects
    for object in objects:
        if pong.colliderect(object):
            pong_velocity *= -1
    # Updates screen
    pygame.display.flip()
    # limit FPS to 60
    clock.tick(40)

pygame.quit()

