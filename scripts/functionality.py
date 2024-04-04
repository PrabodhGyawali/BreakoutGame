import pygame
import math
import random
from assets import *

# Angles and Reflection:
def bounce(point, surface: pygame.Rect, veloctity: pygame.Vector2):#, surface: pygame.Rect):
    # Check if point is in any of the surfaces.
    # print(surface.top, surface.bottom, surface.left, surface.right)
    if abs(point[0] - surface.left) < 2 and abs(point[0] - surface.right) < 2:
        veloctity *= -1
    if abs(point[0] - surface.left) < 2 or abs(point[0] - surface.right) < 2: # horizontal surface
        veloctity[0] *= -1
    else: #abs(point[1] - surface.top) < 2 or abs(point[1] - surface.bottom) < 2:
        # TOFIX: Line is creating TypeError: 'tuple' object does not support item assignment
        print("reached line 16")
        veloctity[1] *= -1
    

def generate_coordinate():
    x = random.randint(100, 500)
    y = random.randint(500, 600)
    return (x, y)

def get_high_score():
    with open("../misc/high_score.txt", "r") as f:
        return f.read()
    
def get_score_gained(tile: pygame.Rect, streak):
    if tile in red_tiles:
        return 4 + streak
    if tile in orange_tiles:
        return 3 + streak
    if tile in green_tiles:
        return 2 + streak
    if tile in yellow_tiles:
        return 1 + streak
    
def accelerate(velocity: pygame.Vector2):
    velocity *= 2