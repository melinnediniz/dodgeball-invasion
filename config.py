import pygame


class Colors:
    BLACK = (0, 0, 0)
    GREEN = (10, 89, 31)
    WHITE = (255, 255, 255)
    BLUE = (0, 110, 230)
    PLAYER = (196, 70, 20)
    WIN_MSG = (115, 14, 2)


class Sounds:
    THROW_BALL = "sound/throw.ogg"
    HIT_ET = "sound/hit_et.ogg"
    HIT_HUMAN = "sound/roblox_death_sound.ogg"
    HUMAN_WIN = "sound/human_win.ogg"
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
    player_2_hit = pygame.image.load('img/player_2_hit.png')


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
    FONT = 'fonts/PressStart2P-Regular.ttf'
    FONT_2 = "fonts/INVASION2000.ttf"


class Lives:
    FONT = "fonts/NormandyBeach.otf"
    MAX_LIVES = 5
    P1_LIVE_POS = (120, 630)
    P2_LIVE_POS = (780, 95)

    p1_heart_pos = (45, 615)
    p2_heart_pos = (830, 75)
    heart_pos = ()


# Global variables
game_loop = True
win_sound = True
live_1 = Lives.MAX_LIVES
live_2 = Lives.MAX_LIVES

# ------- FUNCTIONS
pygame.init()
font = pygame.font.Font(Lives.FONT, 45)
font_live = pygame.font.Font(Lives.FONT, 45)
font_name = pygame.font.Font(Lives.FONT, 30)
font_2 = pygame.font.Font(Constants.FONT_2, 64)
font_msg = pygame.font.Font(Constants.FONT, 20)


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


def victory(surf, loser):
    global win_sound
    winner = ''
    message = ''
    color = Colors.BLACK
    sound = Sounds.HUMAN_WIN
    if loser == 2:
        winner = 'HUMANS'
        color = Colors.BLUE
        message = 'THE WORLD IS A SAFE PLACE AGAIN!'
    elif loser == 1:
        winner = 'ALIENS'
        color = Colors.GREEN
        sound = Sounds.ET_WIN
        message = 'OH NO! IS THIS THE END OF THE WORLD?'

    if win_sound is True:
        play_sound(sound, 0.5)
        win_sound = False

    win_text = font_2.render(f'{winner} WON', True, color)
    win_text_rect = win_text.get_rect(midbottom=(1000 / 2, 700 / 2))
    restart_text = font_name.render("PRESS 'R' TO RESET", True, Colors.BLACK)
    restart_text_rect = restart_text.get_rect(midbottom=(1000 / 2, 530))

    message_surf = font_msg.render(message, True, Colors.WIN_MSG)
    message_rect = message_surf.get_rect()
    message_rect.center = (1000 / 2, 400)

    surf.blit(restart_text, restart_text_rect)
    surf.blit(win_text, win_text_rect)
    surf.blit(message_surf, message_rect)


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
    global live_1, live_2, win_sound
    win_sound = True
    live_1 = Lives.MAX_LIVES
    live_2 = Lives.MAX_LIVES
    player_1.position_x, player_1.position_y = 30, 300
    player_2.position_x, player_2.position_y = 900, 300
    ball_1.position_x, ball_1.position_y = 30, 325
    ball_2.position_x, ball_2.position_y = 730, 325
    pygame.display.flip()
