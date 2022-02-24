import pygame
from pygame.locals import *
import players
import config

pygame.init()


def moves():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.game_loop = False

        # player 1 keystroke event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                players.Players.player_1_move_left = True
            elif event.key == pygame.K_RIGHT:
                players.Players.player_1_move_right = True
            elif event.key == pygame.K_UP:
                players.Players.player_1_move_up = True
            elif event.key == pygame.K_DOWN:
                players.Players.player_1_move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                players.Players.player_1_move_left = False
            elif event.key == pygame.K_RIGHT:
                players.Players.player_1_move_right = False
            elif event.key == pygame.K_UP:
                players.Players.player_1_move_up = False
            elif event.key == pygame.K_DOWN:
                players.Players.player_1_move_down = False


# player 1 coordinates method
def coordinates_1():
    if players.Players.player_1_move_left:
        players.Players.player_1_x -= 5
    else:
        players.Players.player_1_x += 0

    if players.Players.player_1_move_right:
        players.Players.player_1_x += 5
    else:
        players.Players.player_1_x += 0

    if players.Players.player_1_move_up:
        players.Players.player_1_y += 5
    else:
        players.Players.player_1_y += 0

    if players.Players.player_1_move_down:
        players.Players.player_1_y -= 5
    else:
        players.Players.player_1_y += 0