import pygame

pygame.init()

# TODO: Adjust size of border/tiles/screen using variables for ease
x = 6.9
y = 10
space = x*0.2
########################## SCREEN ################################
# Screen_width = (30 * 14) + tilespacing + 40
screen = pygame.display.set_mode((x*90.6, y*90))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    # TODO: Creating a main player character
    BLUE = (0, 141, 218)
    player = pygame.draw.rect(screen, BLUE, pygame.Rect(x*2, y*80, x*6, y*3))

    # TODO: Creating Game borders 
    WHITE = (255, 255, 255)
    wall_left = pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, x*2, y*90))
    wall_right = pygame.draw.rect(screen, WHITE, pygame.Rect(x*88.6, 0, x*2, y*90))

    # TODO: Add blue things onto the border
    wall_left = pygame.draw.rect(screen, BLUE, pygame.Rect(0, y*79.5, x*2, y*4))
    wall_right = pygame.draw.rect(screen, BLUE, pygame.Rect(x*88.6, y*79.5, x*2, y*4))

    # TODO: Add Tiles to break
    RED = (237, 25, 9)
    ORANGE = (255,69,0)
    GREEN = (50,205,50)
    YELLOW = (255,255,0)

    # TODO use loop to generate 14 red tiles with spacing of 1 px
    red_tiles = []
    # red tile has no spacing
    red_tiles.append(pygame.draw.rect(screen, RED, pygame.Rect(x*2, y*20, x*6, y*3)))
    for i in range(1, 14):
        tile = pygame.draw.rect(screen, RED, pygame.Rect(x*2 + (i*x*6) + i*space, y*20, x*6, y*3))
        red_tiles.append(tile)
    # second row of red tiles
    red_tiles.append(pygame.draw.rect(screen, RED, pygame.Rect(x*2, y*23 + space, x*6, y*3)))
    for i in range(1, 14):
        tile = pygame.draw.rect(screen, RED, pygame.Rect(x*2 + (i*x*6) + i*space, y*23 + space, x*6, y*3))
        red_tiles.append(tile)
    

    
    # 
    # orange_tiles = []
    # orange_tiles.append(pygame.draw.rect(screen, ORANGE, pygame.Rect(x*2, y*20 + space, x*6, y*3)))
    # for i in range(1, 14):
    #     tile = pygame.draw.rect(screen, RED, pygame.Rect(x*2 + (i*x*6) + i*space, y*20, x*6, y*3))
    #     red_tiles.append(tile)

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limit FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(60) # limits FPS to 60

pygame.quit()
