import pygame

pygame.init()

# TODO: Adjust size of border/tiles/screen using variables for ease
x, y = 10, 10
space = x*0.4
movex = 0
########################## SCREEN ################################
# Screen_width = (30 * 14) + tilespacing + 40
screen = pygame.display.set_mode((x*63.2, y*90))
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
    player = pygame.draw.rect(screen, BLUE, pygame.Rect(x*2 + movex, y*80, x*3.5, y*1.5))

    # TODO: Creating Game borders 
    WHITE = (255, 255, 255)
    wall_left = pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, x*1, y*90))
    wall_right = pygame.draw.rect(screen, WHITE, pygame.Rect(x*62.2, 0, x*1, y*90))

    # TODO: Add blue things onto the border
    wall_left = pygame.draw.rect(screen, BLUE, pygame.Rect(0, y*79.5, x*1, y*3))
    wall_right = pygame.draw.rect(screen, BLUE, pygame.Rect(x*62.2, y*79.5, x*1, y*3))

    # TODO use a loop to generate red tiles, green tiles, orange tiles, yellow tiles
    RED, ORANGE, GREEN, YELLOW = (237,25,9), (242,133,0), (50,205,50), (255,255,0)
    COLORS = (RED, ORANGE, GREEN, YELLOW)
    red_tiles, orange_tiles, green_tiles, yellow_tiles = [], [], [], []
    tile_array = [red_tiles, orange_tiles, green_tiles, yellow_tiles]
    # red tile has no spacing
    for j in range(4):    
        for k in range(1,3):
            for i in range(14):
                tile_array[j].append(pygame.draw.rect(screen, COLORS[j], pygame.Rect(
                    x*1 + (i*x*4) + i*space,
                    y*20 + k*x*1.5 + k*space +2*j*x*1.5 + 2*j*space,
                    x*4, 
                    y*1.5)))
                
    # Game Functionality
    if event.type == pygame.KEYDOWN:
        key=pygame.key.name(event.key)
        if key == "right":
            movex +=5
        if key == "left":
            movex -=5 
        

        pygame.display.flip()
        pygame.time.delay(20)
    # Updates screen
    pygame.display.flip()


    # limit FPS to 60
    clock.tick(60) 

pygame.quit()
