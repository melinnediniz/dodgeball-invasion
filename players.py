import pygame

class Players:
    player_1 = pygame.image.load('img/player_1.png')
    player_1_y = 300
    player_1_x = 30
    player_1_move_left = False
    player_1_move_right = False
    player_1_move_up = False
    player_1_move_down = False
    player_1_cord = (player_1_x, player_1_y)

    player_2 = pygame.image.load('img/player_2.png')
    player_2_y = 300
    player_2_x = 900
    player_2_cord = (player_2_x, player_2_y)