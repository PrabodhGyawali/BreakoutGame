import pygame
import math
import random
from assets import *

# Angles and Reflection:
def bounce(point, surface: pygame.Rect, veloctity): # Fix the bounce
    # Check if point is in any of the surfaces.
    # print(surface.top, surface.bottom, surface.left, surface.right)
    if abs(point[0] - surface.left) < 2 and abs(point[0] - surface.right) < 2:
        veloctity *= -1
    if abs(point[0] - surface.left) < 2 or abs(point[0] - surface.right) < 2: # horizontal surface
        veloctity[0] *= -1
    else: #abs(point[1] - surface.top) < 2 or abs(point[1] - surface.bottom) < 2:
        # print("reached line 16")
        veloctity[1] *= -1
    

def generate_coordinate():
    x = random.randint(100, 500)
    y = random.randint(500, 600)
    return (x, y)

def get_high_score():
    with open("../misc/high_score.txt", "r") as f:
        return f.read()
    
def get_score_gained(tile: pygame.Rect):
    if tile in red_tiles:
        return 7
    if tile in orange_tiles:
        return 5
    if tile in green_tiles:
        return 3
    if tile in yellow_tiles:
        return 1 
    
def accelerate(velocity: pygame.Vector2):
    if (abs(velocity[0]) < 7 and abs(velocity[1] < 7)):
        try:
            velocity *= 2 
        except TypeError:
            print("TypeError at line 42 is caught")
    print(velocity)

def change_paddle_size(paddle: pygame.Rect):
    if paddle.width > 15:
        paddle.width -= 5

testArray = []
