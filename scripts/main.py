import pygame
import numpy
import random

import pygame.draw_py

# Custom Modules
from assets import *
from functionality import *

pygame.init()
########################## SCREEN ################################
screen = pygame.display.set_mode(DIMS)
clock = pygame.time.Clock()

# Game Variables
running = True
score, accelerate_count, lives = 0, 0, 1
high_score = get_high_score()

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
    pygame.draw.rect(screen, WHITE, border_top)
    # Game border blue
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, y*79, x*1, y*3.5))
    pygame.draw.rect(screen, BLUE, pygame.Rect(x*62.2, y*79, x*1, y*3.5))
    # Loop generating colored side tiles
    for i in range(8):
        pygame.draw.rect(screen, side_tiles_colors[i], side_tiles[i])

    # Loop generating tiles
    for i in range(4):
        for tile in tile_array[i]:
            pygame.draw.rect(screen, COLORS[i], tile)
            
    
    
    # Ball configuration
    pygame.draw.rect(screen, ball_color, ball)
    pygame.draw.circle(screen, WHITE, ball.center, ball_radius) # Inscribed invisible circle for bounce calculation
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
    ######################## Game Functionality #########################
    # Key Events
    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if player.right < 62.2*x:
                player.move_ip(10, 0)
        if keys[pygame.K_LEFT]:
            if player.left > 10:
                player.move_ip(-10, 0)

    # Bouncing off walls:
    if ball.colliderect(wall_left) or ball.colliderect(wall_right):
        dx *= -1
    # Collision with top border:
    if ball.colliderect(border_top):
        dy *= -1
    
    # Collision with player:
    if ball.colliderect(player):
        dx, dy = detect_collision(dx, dy, ball, player)

    # Collision with tiles
    for tiles in tile_array:
        for tile in tiles:
            if ball.colliderect(tile):
                # Bounce of the tile:
                dx, dy = detect_collision(dx, dy, ball, tile)
                score += get_score_gained(tile) 
                accelerate_count += score
                # Removing Tiles from screen
                tiles.remove(tile)

    hit_index = ball.collidelist(tile_array[0] + tile_array[1] + tile_array[2] + tile_array[3])
    # Ball hits sides: if ball.x > 62.2*x or ball.x < 1*x:
    
    # Respawn ball / Settings if ball lost
    if ball.y > DIMS[1]:
        ball.x, ball.y = generate_coordinate()
        lives += 1
        accelerate_count = 0
        ball_speed = 6
        player.width = x*4
    
    if accelerate_count > 4:
        accelerate(ball_speed) 
        change_paddle_size(player)
        accelerate_count = 0 
    
    
    # Updates screen
    # Text rendering:
    update_text(screen, score, score_coord)
    update_text(screen, high_score, high_score_coord) 
    update_lives(screen, lives, lives_coord)
    color_changer(ball_color)
    
    pygame.display.flip()
    # limit FPS to 60
    clock.tick(60)

pygame.quit()

