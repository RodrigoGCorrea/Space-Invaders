from PPlay.sprite import Sprite
from PPlay.keyboard import Keyboard
from bullet import Bullet
from enemy import Enemy

import GVar

keyboard = Keyboard()

class Spaceship(object):
    def __init__(self, window):
        self.window = window
        self.spaceship = Sprite("./images/spaceship.png")
        self.velocity = 0
        self.__set_pos()

    def run(self):
        self.__draw()
        self.move(self.velocity)

    def move(self, velocity):
        if keyboard.key_pressed("left"):
            self.velocity = -GVar.SPACESHIP_VELOCITY
        elif keyboard.key_pressed("right"):
            self.velocity = GVar.SPACESHIP_VELOCITY
        else:
            self.velocity = 0

        if self.spaceship.x >= (GVar.WIDTH - self.spaceship.width):
            self.spaceship.set_position(GVar.WIDTH - self.spaceship.width - 1, GVar.HEIGHT - self.spaceship.height - 10)

        if self.spaceship.x <= 0:
            self.spaceship.set_position(0.5, GVar.HEIGHT - self.spaceship.height - 10)
        
        self.spaceship.x += velocity * self.window.delta_time()

    def __draw(self):
        self.spaceship.draw()
    
    def __set_pos(self):
        self.spaceship.set_position(GVar.WIDTH/2 - self.spaceship.width/2, GVar.HEIGHT - self.spaceship.height - 10)
