import pygame


class Colors:
    BLACK = (0, 0, 0)
    GREEN = (10, 89, 31)


class Sounds:
    THROW_BALL = "sound/throw.ogg"
    HIT_ET = "sound/hit_et.ogg"
    HIT_HUMAN = "sound/roblox_death_sound.ogg"
    HUMAN_WIN = "sound/victory1.ogg"
    ET_WIN = "sound/victory2.ogg"
    HIT_WALL = "sound/hit_wall.ogg"


class Background:
    court = pygame.image.load('img/background.png')
    court_cord = (0, 0)
    start_court = pygame.image.load('img/start_bg.png')


class Aim:
    scope = pygame.image.load('img/aim_1.png')
    scope = pygame.transform.scale(scope, (32, 32))


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
    MAX_LIVES = 10
    DAMAGE = 1


# Global variables
game_loop = True

live_1 = Constants.MAX_LIVES
live_2 = Constants.MAX_LIVES

# ------- FUNCTIONS
pygame.init()
font = pygame.font.Font(Constants.FONT, 30)


def play_sound(file, vol):
    sound = pygame.mixer.Sound(file)
    sound.play().set_volume(vol)


def display_lives(surf, position, live):
    if live == 'player 1':
        live = live_1
    elif live == 'player 2':
        live = live_2
    lives_surf = font.render(f'LIVES: {live}', True, Colors.GREEN)
    lives_rect = lives_surf.get_rect(topleft=position)
    surf.blit(lives_surf, lives_rect)


def update_live(player):
    global live_1, live_2
    if player == 1 and live_1 > 0:
            live_1 -= Constants.DAMAGE
    elif player == 2 and live_2 > 0:
            live_2 -= Constants.DAMAGE

def loser():
    loser = 0
    global live_1, live_2
    if live_1 == 0:
        loser = 1
        print('player 2 win')
    elif live_2 == 0:
        loser = 2
        print('player 1 win')
    return loser

def reset_game(player_1, player_2, ball_1, ball_2):
    global live_1, live_2
    live_1 = Constants.MAX_LIVES
    live_2 = Constants.MAX_LIVES
    player_1.position_x, player_1.position_y = 30, 300
    player_2.position_x, player_2.position_y = 900, 300
    ball_1.position_x, ball_1.position_y = 30, 325
    ball_2.position_x, ball_2.position_y = 730, 325
