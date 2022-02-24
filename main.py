import pygame
import config

pygame.init()

# screen
size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:
    screen.fill(config.Colors.COLOR_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # drawing the objects
    screen.blit(config.Players.player_1, config.Players.player_1_cord)
    screen.blit(config.Players.player_2, config.Players.player_2_cord)
    # update screen
    pygame.display.flip()
    game_clock.tick(config.Clock.CLOCK_TICK)

pygame.quit()
