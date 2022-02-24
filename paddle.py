import pygame
import players
import config

pygame.init()


def moves():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.game_loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                players.Players.player_1_move_left = True
            elif event.key == pygame.K_RIGHT:
                players.Players.player_1_move_right = True
            elif event.key == pygame.K_UP:
                players.Players.player_1_move_up = True
            elif event.key == pygame.K_DOWN:
                players.Players.player_1_move_down = True


def coordinates():
    if players.Players.player_1_move_left:
        players.Players.player_1_x -= 5
    else:
        players.Players.player_1_x += 0

    if players.Players.player_1_move_right:
        players.Players.player_1_x += 5
    else:
        players.Players.player_1_x += 0
