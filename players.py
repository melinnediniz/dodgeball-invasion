import pygame
import config


class Player():
    def __init__(self, position_x, position_y , player):
        self.name = player
        self.position_x = position_x
        self.position_y = position_y     
        self.holding = []
        self.throw_ball = False

        if self.name == 'player_1':
            self.image = pygame.image.load('img/player_1.png')
        if self.name == 'player_2':
            self.image = pygame.image.load('img/player_2.png')

    def hold(self):
        for object in self.holding:
            object.position_x = self.position_x + 10
            object.position_y = self.position_y + 30

    def get_ball(self, ball):
        self.holding.append(ball)
        self.hold()
    
    def throw(self):
        self.throw_ball = True
        return self.throw_ball

    def moves(self, direction):
        self.hold()
        match direction:
            case 'up':
                self.position_y -= config.Constants.SPEED_PLAYER
            case 'down':
                self.position_y += config.Constants.SPEED_PLAYER
            case 'right':
                self.position_x += config.Constants.SPEED_PLAYER
            case 'left':
                self.position_x -= config.Constants.SPEED_PLAYER
        
    def render(self, surface):
        surface.blit(self.image, (self.position_x, self.position_y))
