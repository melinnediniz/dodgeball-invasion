import pygame

class Colors:
    COLOR_BLACK = (0, 0, 0)


class Background:
    court = pygame.image.load('img/background.png')
    court_cord = (0, 0)
    
class Scope:
    scope = pygame.image.load('img/aim_1.png')
    scope = pygame.transform.scale(scope, (32, 32))

# Global variables
game_loop = True
live_1 = 3
live_2 = 3

# Constants
class Constants:
    CLOCK_TICK = 60
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    SPEED_BALL = 25
    SPEED_PLAYER = 8
    SPEED_NPC = 14
    FONT = "fonts/dogica.ttf"
    P1_LIVE_POS = (145, 645)
    P2_LIVE_POS = (600, 25)


# ------- FUNCTIONS
pygame.init()
font = pygame.font.Font(Constants.FONT, 30)

def play_sound(file):
    sound = pygame.mixer.Sound(file)
    sound.play()


def display_lives(surf, position, live):
        lives_surf = font.render(f'LIVES: {live}', True, (10, 89, 31))
        lives_rect = lives_surf.get_rect(topleft = position)
        surf.blit(lives_surf, lives_rect)

def upadate_live(player):
    global live_1, live_2
    if player == 1:
        live_1 -=1
    elif player == 2:
        live_2 -= 1