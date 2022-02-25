import pygame
import config
from players import Players, get_ball
from ball import Ball


pygame.init()

# screen
screen = pygame.display.set_mode(config.Constants.SCREEN_SIZE)
pygame.display.set_caption("DODGEBALL INVASION")
pygame.display.set_icon(pygame.image.load('img/icon.png'))

# game clock (FPS)
game_clock = pygame.time.Clock()

# control var of sprite coordinates
sprite_x = Players.player_1_x
sprite_y = Players.player_1_y

# Balls
ball_1 = Ball(position_x = 240,\
              position_y = 325,\
              ball_image='ball_1')

ball_2 = Ball(position_x = 730,\
              position_y = 325,\
              ball_image='ball_2')


while config.game_loop:
    screen.fill(config.Colors.COLOR_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sprite_x += 30
            elif event.key == pygame.K_LEFT:
                sprite_x -= 30
            elif event.key == pygame.K_UP:
                sprite_y -= 30
            elif event.key == pygame.K_DOWN:
                sprite_y += 30
            elif event.key == pygame.K_SPACE:
                get_ball(ball_1)

    # player 1 collision with left wall
    if sprite_x <= 0:
        sprite_x = 0

    # player 1 collision with the middle
    if sprite_x >= 450:
        sprite_x = 450

    # player 1 collision with the top
    if sprite_y <= 0:
        sprite_y = 0

    # player 1 collision with bottom
    if sprite_y >= 605:
        sprite_y = 605

    # drawing the objects
    screen.blit(config.Background.court, config.Background.court_cord)
    screen.blit(Players.player_1, (sprite_x, sprite_y))
    screen.blit(Players.player_2, Players.player_2_cord)
    ball_1.render(screen)
    ball_2.render(screen)
    # ball_1.move('player_1')
    
    # update screen
    pygame.display.flip()
    game_clock.tick(config.Constants.CLOCK_TICK)

