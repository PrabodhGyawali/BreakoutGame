import pygame
import math
import random
from assets import *

# Angles and Reflection:
def bounce_tile(veloctity): # Fix the bounce
    veloctity[1] *= -1
    

def bounce_paddle(velocity, can_bounce_paddle):
    # TODO: Check if this is only for top of the surface
    if can_bounce_paddle:
        if random.randint(0, 1):
            velocity[1] *= -1
        else:
            velocity *= -1
        can_bounce_paddle = False

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

# Moves asset when not visible on screen. Avoids creating unwanted errors.
storage = []
storage_coord = []
def store_asset(asset: pygame.Rect):    
    # Log asset into the storage unit
    storage.append(asset)
    asset_coord = np.asarray((asset.x, asset.y))
    storage_coord.append(asset_coord)

    asset.x = - 100
    asset.y = - 100


testArray = []
