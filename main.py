import pygame
import game
from config import game_loop, Constants


pygame.init()

# game clock (FPS)
game_clock = pygame.time.Clock()
game = game.Game()

while game_loop:
    game.change_screen()
    game_clock.tick(Constants.CLOCK_TICK)
