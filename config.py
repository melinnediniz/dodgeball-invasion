from tkinter import Y
import pygame

class Colors:
    # colors
    COLOR_BLACK = (0, 0, 0)


class Background:
    court = pygame.image.load('img/background.png')
    court_cord = (0, 0)
    
class Scope:
    scope = pygame.image.load('img/aim_1.png')
    scope = pygame.transform.scale(scope, (32, 32))

# Game loop variable
game_loop = True

# Constants
class Constants:
    CLOCK_TICK = 60
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    SPEED_BALL = 10


# ------- FUNCTIONS

def play_sound(file):
    sound = pygame.mixer.Sound(file)
    sound.play()
