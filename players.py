import config
from config import Images


class Player:
    def __init__(self, position_x, position_y, player):
        self.name = player
        self.position_x = position_x
        self.position_y = position_y
        self.holding = []
        self.throw_ball = False
        self.speed = config.Constants.SPEED_PLAYER

        if self.name == 'player_1':
            self.image = Images.player_1
        if self.name == 'player_2':
            self.image = Images.player_2

    
    def wall_limits(self):
        # player 1 collision with left wall
        if self.position_x <= 0:
            self.position_x = 0

        # player 1 collision with the middle
        if self.position_x >= 450:
            self.position_x = 450

        # player 1 collision with the top
        if self.position_y <= 0:
            self.position_y = 0

        # player 1 collision with bottom
        if self.position_y >= 605:
            self.position_y = 605

    def hold(self):
        for obj in self.holding:
            obj.position_x = self.position_x + 10
            obj.position_y = self.position_y + 30

    def get_ball(self, ball):
        self.holding.append(ball)
        self.hold()

    def throw(self):
        config.play_sound(config.Sounds.THROW_BALL, 0.07)
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
                if self.position_x >= 500:
                    self.moves('left')
                if self.position_y == enemy.position_y \
                        or enemy.position_y < self.position_y < enemy.position_y + 10:
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
