import pygame
import config
from sys import exit
from players import Players
import paddle

pygame.init()

# screen
screen = pygame.display.set_mode(config.Constants.SCREEN_SIZE)
pygame.display.set_caption("DODGEBALL INVASION")
pygame.display.set_icon(pygame.image.load('img/icon.png'))

# game clock (FPS)
game_clock = pygame.time.Clock()

while config.game_loop:
    screen.fill(config.Colors.COLOR_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.game_loop = False
            exit()

            paddle.moves()

    paddle.coordinates_1()

    # drawing the objects
    screen.blit(config.Background.court, config.Background.court_cord)
    screen.blit(Players.player_1, Players.player_1_cord)
    screen.blit(Players.player_2, Players.player_2_cord)

    # update screen
    pygame.display.flip()
    game_clock.tick(config.Constants.CLOCK_TICK)

