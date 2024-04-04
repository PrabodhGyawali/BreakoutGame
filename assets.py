import pygame
import numpy as np

pygame.init()
# Constants
x, y = 10, 10
DIMS = (x*63.2, y*90)
space = 4
pong_velocity = pygame.Vector2(2, 2)
BLACK = (0, 0, 0)
BLUE, WHITE, RED, ORANGE, GREEN, YELLOW  = (0, 141, 218), (255, 255, 255), (237,25,9), (242,133,0), (50,205,50), (255,255,0)
COLORS = (RED, ORANGE, GREEN, YELLOW, BLUE, WHITE)
objects = []
player = pygame.Rect(x*2, y*80, x*3.5, y*1.5)
# Game borders 
wall_left = pygame.Rect(0, 0, x*1, y*90)
wall_right = pygame.Rect(x*62.2, 0, x*1, y*90)

border_top = pygame.Rect(0, y*8, x*63.2, y*3.5)

# Loop generating tiles
red_tiles, orange_tiles, green_tiles, yellow_tiles = [], [], [], []
tile_array = [red_tiles, orange_tiles, green_tiles, yellow_tiles]
side_tiles = []
side_tiles_colors = [RED, RED, ORANGE, ORANGE, GREEN, GREEN, YELLOW, YELLOW]
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

# Colors on side walls:
for i in range(4):
    for k in range(2):
        side_tile = pygame.Rect(
            0 + 622*k, # Left
            20-2 + 200+ 38*i, # Top
            10, # Width
            38, # Height
        )
        side_tiles.append(side_tile)

pong =  pygame.Rect(400, 400, 5, 5)

objects.append(wall_left)
objects.append(wall_right)
objects.append(player)
objects.append(border_top)

# Text rendering
font = pygame.font.Font("pixel-loot.ttf", 50)
score_coord = (100, 190)
lives_coord = (400, 140)
high_score_coord = (500, 190)

def update_text(screen, score, coord):
    score_text = ('000' + str(score))[-3:]
    text = font.render(score_text, True, WHITE, None)
    textRect = text.get_rect()
    textRect.center = coord
    screen.blit(text, textRect)

def update_lives(screen, lives, coord):
    text = font.render(str(lives), True, WHITE, None)
    textRect = text.get_rect()
    textRect.center = coord
    screen.blit(text, textRect)
