import pygame
import numpy as np

# Constants
x, y = 10, 10
space = 4
pong_velocity = pygame.Vector2(2, -2)

BLUE, WHITE, RED, ORANGE, GREEN, YELLOW  = (0, 141, 218), (255, 255, 255), (237,25,9), (242,133,0), (50,205,50), (255,255,0)
COLORS = (RED, ORANGE, GREEN, YELLOW, BLUE, WHITE)
objects = []
player = pygame.Rect(x*2, y*80, x*3.5, y*1.5)
# Game borders 
wall_left = pygame.Rect(0, 0, x*1, y*90)
wall_right = pygame.Rect(x*62.2, 0, x*1, y*90)

# Loop generating tiles
red_tiles, orange_tiles, green_tiles, yellow_tiles = [], [], [], []
tile_array = [red_tiles, orange_tiles, green_tiles, yellow_tiles]
# red tile has no spacing
for j in range(4):    
    for k in range(1,3):
        for i in range(14):
            tile = pygame.Rect(
                x*1 + (i*x*4) + i*space,
                y*20 + k*x*1.5 + k*space +2*j*x*1.5 + 2*j*space,
                x*4, 
                y*1.5)
            tile_array[j].append(tile)
            objects.append(tile)

pong =  pygame.Rect(400, 400, 5, 5)

objects.append(wall_left)
objects.append(wall_right)
objects.append(player)