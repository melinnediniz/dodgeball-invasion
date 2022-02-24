import pygame


class Clock:
    CLOCK_TICK = 60


class Colors:
    # colors
    COLOR_BLACK = (0, 0, 0)
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLUE = (0, 180, 250)
    COLOR_RED = (162, 8, 0)
    COLOR_YELLOW = (197, 199, 37)
    COLOR_GREEN = (0, 127, 33)
    COLOR_ORANGE = (183, 119, 0)


class Players:
    player_1 = pygame.image.load('player1.png')
    player_1_y = 300
    player_1_x = 10
    player_1_cord = (player_1_x, player_1_y)
    player_2 = pygame.image.load('player2.png')
    player_2_y = 300
    player_2_x = 960
    player_2_cord = (player_2_x, player_2_y)
