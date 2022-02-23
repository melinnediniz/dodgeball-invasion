import pygame
import config


pygame.init()


# screen
size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:
    screen.fill(config.Config.COLOR_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # update screen
    pygame.display.flip()
    game_clock.tick(config.Config.CLOCK_TICK)

pygame.quit()
