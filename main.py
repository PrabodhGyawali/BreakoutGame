import pygame

pygame.init()
screen = pygame.display.set_mode((720, 900))
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
    player = pygame.draw.rect(screen, BLUE, pygame.Rect(20, 800, 60, 30))

    # TODO: Creating Game borders 
    WHITE = (255, 255, 255)
    wall_left = pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 20, 900))
    wall_right = pygame.draw.rect(screen, WHITE, pygame.Rect(700, 0, 20, 900))

    # TODO: Add blue things onto the border
    wall_left = pygame.draw.rect(screen, BLUE, pygame.Rect(0, 795, 20, 40))
    wall_right = pygame.draw.rect(screen, BLUE, pygame.Rect(700, 795, 20, 40))



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limit FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(60) # limits FPS to 60

pygame.quit()
