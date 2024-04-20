import pygame
import math
import random
from assets import *

# Bouncing ball
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 5:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy
def generate_coordinate():
    x = random.randint(100, 500)
    y = random.randint(500, 600)
    return (x, y)

def get_high_score():
    with open("../misc/high_score.txt", "r") as f:
        return f.read()
    
def new_high_score(score):
    with open("../misc/high_score.txt", "w") as f:
        f.write(str(score))
    
def get_score_gained(tile: pygame.Rect):
    if tile in red_tiles:
        return 7
    if tile in orange_tiles:
        return 5
    if tile in green_tiles:
        return 3
    if tile in yellow_tiles:
        return 1 

def change_paddle_size(paddle: pygame.Rect):
    if paddle.width > 20:
        paddle.width -= 1

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

def color_changer(ball_color: pygame.Color):
    if ball.y > 218 and ball.y < 218 + 1*38:
        ball_color.update(RED[0], RED[1], RED[2])
    elif ball.y > 218 + 1*38 and ball.y < 218 + 2*38:
        ball_color.update(ORANGE[0], ORANGE[1], ORANGE[2])
    elif ball.y > 218 + 2*38 and ball.y < 218 + 3*38:
        ball_color.update(GREEN[0], GREEN[1], GREEN[2])
    elif ball.y > 218 + 3*38 and ball.y < 218 + 4*38:
        ball_color.update(YELLOW[0], YELLOW[1], YELLOW[2])
    elif ball.y > 790 and ball.y < 790 + 35:
        ball_color.update(BLUE[0], BLUE[1], BLUE[2])
    else:
        ball_color.update(255,255,255)
    
