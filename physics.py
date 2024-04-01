import pygame
import math

# Angles and Reflection:
def surface_check(point, surface: pygame.Rect):#, surface: pygame.Rect):
    # Check if point is in any of the surfaces.
    print(point)
    print(surface.top, surface.bottom, surface.left, surface.right)
    if abs(point[0] - surface.left) < 2 or abs(point[0] - surface.right) < 2: # horizontal surface
        return 0 
    elif abs(point[1] - surface.top) < 2 or abs(point[1] - surface.bottom) < 2:
        return 1
    else:
        return 2