import pygame
import game


class Colors:
    BLACK = (0, 0, 0)
    GREEN = (10, 89, 31)
    WHITE = (255, 255, 255)
    BLUE = (0, 110, 230)
    PLAYER = (196, 70, 20)


class Sounds:
    THROW_BALL = "sound/throw.ogg"
    HIT_ET = "sound/hit_et.ogg"
    HIT_HUMAN = "sound/roblox_death_sound.ogg"
    HUMAN_WIN = "sound/victory1.ogg"
    ET_WIN = "sound/victory2.ogg"
    BACKGROUND = "sound/music/pika-a-boo_8bit.mp3"


class Images:
    court = pygame.image.load('img/background.png')
    menu = pygame.image.load('img/menu.png')
    icon = pygame.image.load('img/icon.png')

    heart = pygame.image.load('img/heart.png')
    heart_et = pygame.image.load('img/et_heart.png')
    heart = pygame.transform.scale(heart, (65, 65))
    heart_et = pygame.transform.scale(heart_et, (65, 65))

    ball_1 = pygame.image.load("img/ball_1.png")
    ball_2 = pygame.image.load("img/ball_2.png")

    player_1 = pygame.image.load('img/player_1.png')
    player_1_hit = pygame.image.load('img/player_1_hit.png')

    player_2 = pygame.image.load('img/player_2.png')
    player_2_hit= pygame.image.load('img/player_2_hit.png')


class Aim:
    scope = pygame.image.load('img/aim_1.png')
    scope = pygame.transform.scale(scope, (32, 32))


# Constants
class Constants:
    CLOCK_TICK = 60
    SCREEN_SIZE = (1000, 700)
    
    SPEED_BALL = 25
    SPEED_PLAYER = 8
    SPEED_NPC = 14

    COURT_CORD = (0, 0)
    FONT_2 = "fonts/INVASION2000.ttf"


class Lives:
    FONT = "fonts/NormandyBeach.otf"
    MAX_LIVES = 10
    P1_LIVE_POS = (120, 630)
    P2_LIVE_POS = (780, 95)

    p1_heart_pos = (45, 615)
    p2_heart_pos = (830, 75)
    heart_pos = ()


# Global variables
game_loop = True
count = True
live_1 = Lives.MAX_LIVES
live_2 = Lives.MAX_LIVES
count_down = 5

# ------- FUNCTIONS
pygame.init()
font = pygame.font.Font(Lives.FONT, 45)
font_live = pygame.font.Font(Lives.FONT, 45)
font_name = pygame.font.Font(Lives.FONT, 30)
font_2 = pygame.font.Font(Constants.FONT_2, 64)


def play_sound(file, vol):
        sound = pygame.mixer.Sound(file)
        sound.set_volume(vol)
        sound.play()

def play_music():
        pygame.mixer.init()
        pygame.mixer.music.load(Sounds.BACKGROUND)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

def loser():
    loser = 0
    global live_1, live_2
    if live_1 == 0:
        loser = 1
        print('player 2 win')
    elif live_2 == 0:
        loser = 2
        print('player 1 win')
    print(loser)
    return loser

def victory(surf):
    winner = ''
    lose = loser()
    color = Colors.BLACK
    if live_2 == 0:
        winner = 'HUMAN'
        color = Colors.BLUE
        play_sound(Sounds.HUMAN_WIN, 0.5)
    elif live_1 == 0:
        winner = 'ALIEN'
        color = Colors.GREEN
        play_sound(Sounds.ET_WIN, 0.5)
    
    text = font_2.render(f'{winner} WINS', True, color)
    text_rect = text.get_rect(midbottom=(1000/2, 700/2))
    restart_text = font_2.render('Press R To Restart or Esc to Finish', True, Colors.BLACK)
    restart_text_rect = restart_text.get_rect(midbottom=(1000/2, 530))
    surf.blit(restart_text, restart_text_rect)
    surf.blit(text, text_rect)

def display_lives(surf, position, live):
    heart_surf = Images.heart
    name = ''
    text_pos = ()
    if live == 'player 1':
        live = live_1
        name = 'HUMAN'
        Lives.heart_pos = Lives.p1_heart_pos
        text_pos = (120, 600)
    elif live == 'player 2':
        live = live_2
        name = 'ALIEN'
        text_pos = (745, 70)
        Lives.heart_pos = Lives.p2_heart_pos
        heart_surf = Images.heart_et

    player_surf = font_name.render(name, True, Colors.PLAYER)
    player_rect = player_surf.get_rect(topleft=text_pos)

    lives_surf = font_live.render(f'{live}', True, Colors.WHITE)
    lives_rect = lives_surf.get_rect(topleft=position)

    surf.blit(lives_surf, lives_rect)
    surf.blit(player_surf, player_rect)
    surf.blit(heart_surf, Lives.heart_pos)


def update_live(player):
    global live_1, live_2
    if player == 1 and live_1 > 0:
        live_1 -= 1
        play_sound(Sounds.HIT_HUMAN, 0.2)
    elif player == 2 and live_2 > 0:
        live_2 -= 1
        play_sound(Sounds.HIT_ET, 0.1)


def reset_game(player_1, player_2, ball_1, ball_2):
    global live_1, live_2
    live_1 = Lives.MAX_LIVES
    live_2 = Lives.MAX_LIVES
    player_1.position_x, player_1.position_y = 30, 300
    player_2.position_x, player_2.position_y = 900, 300
    ball_1.position_x, ball_1.position_y = 30, 325
    ball_2.position_x, ball_2.position_y = 730, 325
    pygame.display.flip()
