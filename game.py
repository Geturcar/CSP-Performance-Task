import pygame

WIDTH = 1200
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    #INSIDE OF THE GAME LOOP
    screen.blit(pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT)), (0, 0))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
