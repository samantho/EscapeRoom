import pygame
import pygame_menu

def begin():
    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Escape Room')
    clock = pygame.time.Clock()
    gameDisplay.fill((255,255,255))

    ending = False
    while not ending:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = True
            print(event)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
