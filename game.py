import pygame

from config import Constants, Aim, Background, Sounds, play_sound
from config import display_lives, update_live, reset_game, loser
from players import Player
from ball import Ball
from sys import exit

# screen
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
pygame.display.set_caption("DODGE-BALL INVASION")
pygame.display.set_icon(pygame.image.load('img/icon.png'))

# control var of sprite coordinates
player_1 = Player(30, 300, 'player_1')
player_2 = Player(900, 300, 'player_2')
collision = 50


# Balls
ball_1 = Ball(position_x=240,
              position_y=325,
              ball_image='ball_1')

ball_2 = Ball(position_x=730,
              position_y=325,
              ball_image='ball_2')

movements = dict(
    up=lambda: player_1.moves('up'),
    down=lambda: player_1.moves('down'),
    right=lambda: player_1.moves('right'),
    left=lambda: player_1.moves('left')
)
key_pressed = set()


def move_player():
    for move in key_pressed:
        movements[move]()


player_1.get_ball(ball_1)
player_2.get_ball(ball_2)


# mouse invisible
pygame.mouse.set_visible(False)


class Game:
    def __init__(self):
        self.current_screen = "start_screen"

    def start_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_screen = "main"
                elif event.key == pygame.K_ESCAPE:
                    exit()

        screen.blit(Background.start_court, Background.court_cord)
        pygame.display.flip()

    # PLAYING THE GAME
    def main(self):
        global live_1, live_2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                # testing update lives
                if event.key == pygame.K_1:
                    update_live(1)
                elif event.key == pygame.K_2:
                    update_live(2)
                elif event.key == pygame.K_RIGHT:
                    key_pressed.add('right')
                elif event.key == pygame.K_LEFT:
                    key_pressed.add('left')
                elif event.key == pygame.K_UP:
                    key_pressed.add('up')
                elif event.key == pygame.K_DOWN:
                    key_pressed.add('down')
                elif event.key == pygame.K_SPACE:
                    player_1.throw()

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

        # ball collision with player_1
        if ball_2.position_x <= player_1.position_x:
            if player_1.position_y < ball_2.position_y + collision:
                if player_1.position_y + collision > ball_2.position_y:
                    if loser():
                        play_sound(Sounds.ET_WIN, 0.6)
                        self.current_screen = "start_screen"
                        reset_game(player_1, player_2, ball_1, ball_2)
                    else:
                        update_live(1)
                        play_sound(Sounds.HIT_HUMAN, 0.1)
                        player_2.hold()
                        player_2.throw_ball = False


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
        screen.blit(Aim.scope, (mx - 16, my - 16))
        display_lives(screen, Constants.P1_LIVE_POS, 'player 1')
        display_lives(screen, Constants.P2_LIVE_POS, 'player 2')

        # update screen
        pygame.display.flip()

    def change_screen(self):
        if self.current_screen == "start_screen":
            self.start_screen()
        if self.current_screen == "main":
            self.main()
