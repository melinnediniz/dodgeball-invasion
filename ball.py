import pygame
import config


class Ball(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y , ball_image):
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.position_y = position_y
        self.speed = config.Constants.SPEED_BALL
        
        # check image
        if ball_image == 'ball_1':
            self.image = pygame.image.load("img/ball_1.png")
        elif ball_image == 'ball_2':
            self.image = pygame.image.load("img/ball_2.png")

    def move(self,player):
        if player == 'player_1':
            self.position_x += self.speed
        elif player == 'player_2':
            self.position_x -= self.speed

    def render(self,surface):
        surface.blit(self.image,(self.position_x, self.position_y))