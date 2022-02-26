import pygame
import config


class Player():
    def __init__(self, position_x, position_y, player):
        self.name = player
        self.position_x = position_x
        self.position_y = position_y     
        self.holding = []
        self.throw_ball = False
        self.speed = config.Constants.SPEED_PLAYER

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
        if not self.throw_ball:
            self.hold()

        match direction:
            case 'up':
                self.position_y -= self.speed
            case 'down':
                self.position_y += self.speed
            case 'right':
                self.position_x += self.speed
            case 'left':
                self.position_x -= self.speed
        
    def render(self, surface):
        surface.blit(self.image, (self.position_x, self.position_y))

    def npc(self, enemy, ball_enemy):

        def move_npc():
            self.speed = config.Constants.SPEED_NPC
            if not self.throw_ball:
                if self.position_x > 500:
                    self.moves('left')
                if self.position_y == enemy.position_y\
                    or self.position_y > enemy.position_y and\
                    self.position_y < enemy.position_y + 10:
                    self.throw()

                elif self.position_y != enemy.position_y:
                    if self.position_y > enemy.position_y:
                        self.moves('up')
                    elif self.position_y < enemy.position_y:
                        self.moves('down')
            else:
                if self.position_x < 730:
                    self.moves('right')
                   

        
        move_npc()
        