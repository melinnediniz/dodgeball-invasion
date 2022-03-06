import pygame
import game


class Colors:
    BLACK = (0, 0, 0)
    GREEN = (10, 89, 31)
    WHITE = (255, 255, 255)
    BLUE = (0, 110, 230)


class Sounds:
    THROW_BALL = "sound/throw.ogg"
    HIT_ET = "sound/hit_et.ogg"
    HIT_HUMAN = "sound/roblox_death_sound.ogg"
    HUMAN_WIN = "sound/victory1.ogg"
    ET_WIN = "sound/victory2.ogg"
    HIT_WALL = "sound/hit_wall.ogg"
    BACKGROUND = "sound/music/pika-a-boo_8bit.mp3"


class Images:
    court = pygame.image.load('img/background.png')
    menu = pygame.image.load('img/menu.png')
    icon = pygame.image.load('img/icon.png')

    heart = pygame.image.load('img/heart.png')
    heart = pygame.transform.scale(heart, (65, 65))

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
    P1_LIVE_POS = (120, 630)
    P2_LIVE_POS = (770, 80)
    MAX_LIVES = 10
    heart_pos = (0, 0)


# Global variables
game_loop = True
victory_alien = True
victory_human = True
count = True
live_1 = Lives.MAX_LIVES
live_2 = Lives.MAX_LIVES
count_down = 5

# ------- FUNCTIONS
pygame.init()
font = pygame.font.Font(Lives.FONT, 45)
font_2 = pygame.font.Font(Constants.FONT_2, 64)
font_3 = pygame.font.Font(Constants.FONT_2, 18)


def play_sound(file, vol):
        sound = pygame.mixer.Sound(file)
        sound.set_volume(vol)
        sound.play()

def play_music():
        pygame.mixer.init()
        pygame.mixer.music.load(Sounds.BACKGROUND)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)


def victory_1():
    global victory_alien
    while victory_alien:
        endgame2()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    pygame.time.wait(500)
                    victory_alien = False
                elif event.key == pygame.K_ESCAPE:
                    exit()


def victory_2():
    global victory_human
    while victory_human:
        endgame1()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    pygame.time.wait(500)
                    victory_human = False
                elif event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.QUIT:
                exit()


def endgame1():
    lock()
    victory_h()
    restart()
    pygame.display.flip()


def endgame2():
    lock()
    victory_a()
    restart()
    pygame.display.flip()


def victory_h():
    human_text = font_2.render('HUMAN WINS', True, Colors.BLUE)
    human_text_rect = human_text.get_rect()
    human_text_rect.center = (1000/2, 700/2)
    game.screen.blit(human_text, human_text_rect)


def victory_a():
    alien_text = font_2.render('ALIEN WINS', True, Colors.GREEN)
    alien_text_rect = alien_text.get_rect()
    alien_text_rect.center = (1000/2, 700/2)
    game.screen.blit(alien_text, alien_text_rect)


def restart():
    restart_text = font_3.render('Press R To Restart or Esc to Finish', True, Colors.BLACK)
    restart_text_rect = restart_text.get_rect()
    restart_text_rect.center = (1000/2, 530)
    game.screen.blit(restart_text, restart_text_rect)


def display_lives(surf, position, live):
    heart_surf = Images.heart
    if live == 'player 1':
        live = live_1
        Lives.heart_pos = (45, 615)
    elif live == 'player 2':
        live = live_2
        Lives.heart_pos = (820, 75)
    surf.blit(heart_surf, Lives.heart_pos)
    lives_surf = font.render(f'{live}', True, Colors.WHITE)
    lives_rect = lives_surf.get_rect(topleft=position)
    surf.blit(lives_surf, lives_rect)


def lock():
    game.screen.blit(Images.court, Constants.COURT_CORD)
    pygame.mouse.set_visible(True)
    display_lives(game.screen, Lives.P1_LIVE_POS, 'player 1')
    display_lives(game.screen, Lives.P2_LIVE_POS, 'player 2')
    game.player_1.render(game.screen)
    game.player_2.render(game.screen)


def update_live(player):
    global live_1, live_2
    if player == 1 and live_1 > 0:
        live_1 -= 1
        play_sound(Sounds.HIT_HUMAN, 0.2)
    elif player == 2 and live_2 > 0:
        live_2 -= 1
        play_sound(Sounds.HIT_ET, 0.1)


def reset_game():
    global live_1, live_2
    live_1 = Lives.MAX_LIVES
    live_2 = Lives.MAX_LIVES
    game.player_1.position_x, game.player_1.position_y = 30, 300
    game.player_2.position_x, game.player_2.position_y = 900, 300
    game.ball_1.position_x, game.ball_1.position_y = 30, 325
    game.ball_2.position_x, game.ball_2.position_y = 730, 325
    pygame.display.flip()
