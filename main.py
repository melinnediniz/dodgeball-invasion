import pygame
import config
from config import Constants, Sounds, Colors, Aim, Background
from config import play_sound, display_lives, upadate_live, live_1, live_2, game_loop
from players import Player
from ball import Ball


pygame.init()

# screen
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
pygame.display.set_caption("DODGEBALL INVASION")
pygame.display.set_icon(pygame.image.load('img/icon.png'))

# game clock (FPS)
game_clock = pygame.time.Clock()

# control var of sprite coordinates
player_1 = Player(30, 300, 'player_1')
player_2 = Player(900, 300, 'player_2')

# Balls
ball_1 = Ball(position_x = 240,\
              position_y = 325,\
              ball_image='ball_1')

ball_2 = Ball(position_x = 730,\
              position_y = 325,\
              ball_image='ball_2')

movemets = dict(
        up = lambda: player_1.moves('up'),
        down = lambda: player_1.moves('down'),
        right = lambda: player_1.moves('right'),
        left = lambda: player_1.moves('left')
        )
key_pressed = set()

def move_player():
    for move in key_pressed:
        movemets[move]()

player_1.get_ball(ball_1)
player_2.get_ball(ball_2)

# mouse invisible
pygame.mouse.set_visible(False)

while game_loop:
    screen.fill(Colors.COLOR_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                key_pressed.add('right')
            elif event.key == pygame.K_LEFT:
                key_pressed.add('left')
            elif event.key == pygame.K_UP:
                key_pressed.add('up')
            elif event.key == pygame.K_DOWN:
                key_pressed.add('down')
            elif event.key == pygame.K_SPACE:
                player_1.throw()
                play_sound

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                key_pressed.remove('right')
            elif event.key == pygame.K_LEFT:
                key_pressed.remove('left')
            elif event.key == pygame.K_UP:
                key_pressed.remove('up')
            elif event.key == pygame.K_DOWN:
                key_pressed.remove('down')
    
    move_player()
    if player_1.throw_ball:
        ball_1.move('player_1')

    if player_2.throw_ball:
        ball_2.move('player_2')

    # player 1 collision with left wall
    if player_1.position_x <= 0:
        player_1.position_x = 0

    # player 1 collision with the middle
    if player_1.position_x >= 450:
        player_1.position_x = 450

    # player 1 collision with the top
    if player_1.position_y <= 0:
        player_1.position_y = 0

    # player 1 collision with bottom
    if player_1.position_y >= 605:
        player_1.position_y = 605

    if ball_1.position_x > 1000:
        player_1.throw_ball = False
        player_1.hold()
    
    if ball_2.position_x < 0:
        player_2.throw_ball = False
        player_2.hold()

    player_2.npc(enemy=player_1, ball_enemy=ball_1)

    # scope position
    mx, my = pygame.mouse.get_pos()
    if mx >= 968:
        mx = 968
    if my >= 668:
        my = 668

    # drawing the objects
    screen.blit(Background.court, Background.court_cord)
    player_1.render(screen)
    player_2.render(screen)
    ball_1.render(screen)
    ball_2.render(screen)
    screen.blit(Aim.scope, (mx-16, my-16))
    display_lives(screen, Constants.P1_LIVE_POS, live_1)
    display_lives(screen, Constants.P2_LIVE_POS, live_2)
    
    # update screen
    pygame.display.flip()
    game_clock.tick(Constants.CLOCK_TICK)

