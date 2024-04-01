import pygame
import math
import random

# Angles and Reflection:
def bounce(point, surface: pygame.Rect, veloctity):#, surface: pygame.Rect):
    # Check if point is in any of the surfaces.
    # print(point)
    # print(surface.top, surface.bottom, surface.left, surface.right)
    if abs(point[0] - surface.left) < 2 or abs(point[0] - surface.right) < 2: # horizontal surface
        veloctity[0] *= -1
    else: #abs(point[1] - surface.top) < 2 or abs(point[1] - surface.bottom) < 2:
        veloctity[1] *= -1
    

def generate_coordinate():
    x = random.randint(100, 500)
    y = random.randint(500, 600)
    return (x, y)