import pygame
import pygame.draw_py

# Custom Modules
from assets import *
from functionality import *

pygame.init()
########################## SCREEN ################################
screen = pygame.display.set_mode(DIMS)
clock = pygame.time.Clock()

running = True
# State Variables
test, has_started = True, False

# Starting banner message:
banner_message = "Press Space to Start"

while running:
    # Misc Variables
    score, accelerate_count, lives = 0, 0, 5
    high_score = int(get_high_score())
    # Starting Screen -> bouncing ball
    while not has_started:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    has_started = True
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        banner(screen, banner_message, 0)
        
        render_game(screen, player_start)

        # Ball configuration
        pygame.draw.rect(screen, ball_color, ball)
        pygame.draw.circle(screen, ball_color, ball.center, ball_radius) # Inscribed invisible circle for bounce calculation
        ball.x += ball_speed * dx
        ball.y -= ball_speed * dy


        # Bouncing off walls:
        if ball.colliderect(wall_left) or ball.colliderect(wall_right):
            dx *= -1
        # Collision with top border:
        if ball.colliderect(border_top):
            dy *= -1
        
        # Collision with player:
        if ball.colliderect(player_start):
            dx, dy = detect_collision(dx, dy, ball, player_start)

        # Collision with tiles
        for tiles in tile_array:
            for tile in tiles:
                if ball.colliderect(tile):
                    # Bounce of the tile:
                    dx, dy = detect_collision(dx, dy, ball, tile)
                    ball_speed = random.choice([3,4,6,8])
                
        pygame.display.flip()
        
        clock.tick(80)
    # Reset ball and settings
    ball.x, ball.y = generate_coordinate()
    FPS = 30
    while has_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        render_game(screen, player)
            
        # Ball configuration
        pygame.draw.rect(screen, ball_color, ball)
        pygame.draw.circle(screen, ball_color, ball.center, ball_radius) # Inscribed invisible circle for bounce calculation
        ball.x += ball_speed * dx
        ball.y -= ball_speed * dy
        ######################## Game Functionality #########################
        # Key Events
        if test:
            FPS = 120
            player.x = ball.x
        else:
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    if player.right < 62.2*x:
                        player.move_ip(6, 0)
                if keys[pygame.K_LEFT]:
                    if player.left > 10:
                        player.move_ip(-6, 0)

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
        
        # Respawn ball / Settings if ball lost
        if ball.y > DIMS[1]:
            # Check for loss
            if lives == 5:
                if score > high_score: 
                    banner_message = "New Highscore"
                    new_high_score(score) 
                else:
                    banner_message = "You Lose! Try Again"
                    
                has_started = False  # Back to start screen
            # Ball config reset
            ball.x, ball.y = generate_coordinate()
            FPS = 30
            lives += 1 # MISC
            accelerate_count = 0
            ball_speed = 3
            player.width = x*4  # player reset
        
        if accelerate_count > 4:
            if FPS <= 80:
                FPS += 5 
            if random.choice([True, False]):
                change_paddle_size(player)
            accelerate_count = 0 
        
        # Check for Win
        total_tiles = tile_array[0] + tile_array[1] + tile_array[2] + tile_array[3]
        if len(total_tiles) == 0:
            banner(screen, "You win!", ball_speed)
            has_started = False
        
        # Updates screen
        # Text rendering:
        update_text(screen, score, score_coord)
        update_text(screen, high_score, high_score_coord)
        update_lives(screen, lives, lives_coord)
        banner(screen, "Prabbodh's Breakout Game", ball_speed)
        color_changer(ball_color)
        
        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()

