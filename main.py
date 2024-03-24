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
    screen.fill("grey")

    # RENDER YOUR GAME HERE
    # TODO: Creating a main player character
    color = (0, 141, 218)
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 30))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limit FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(60) # limits FPS to 60

pygame.quit()
