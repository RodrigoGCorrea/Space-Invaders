from spaceship import Spaceship
from enemy import Enemy
from bullet import Bullet
from PPlay.keyboard import Keyboard

import GVar

keyboard = Keyboard()

class Play(object):
    def __init__(self, window, alien_spawn_adress):
        self.window = window
        self.alien_spawn_adress = alien_spawn_adress
        self.spaceship = Spaceship(window)
        self.enemy = Enemy(window, alien_spawn_adress)
        self.bullet = Bullet(window)
        self.border = {
            "left": 0,
            "right": 0,
            "up": 0,
            "down": 0 
        }
    
    def run(self):
        self.spaceship.run()
        self.enemy.run()
        self.bullet.run(self.spaceship.spaceship)
        self.game_over()
        self.set_border()
        self.point()

    def set_border(self):
        for alien in self.enemy.enemy_mtx:
            if alien.x <= self.border["left"]:
                self.border["left"] = alien.x
            if alien.x + alien.width >= self.border["right"]:
                self.border["right"] = alien.x + alien.width
            if alien.y <= self.border["up"]:
                self.border["up"] = alien.y
            if alien.y + alien.height >= self.border["down"]:
                self.border["down"] = alien.y + alien.height
    
    def point(self):
        for bullet in self.bullet.bullet_array:
            if self.border["left"] <= bullet.x <= self.border["right"]:
                if self.border["up"] <= bullet.y <= self.border["down"]:
                    for alien in self.enemy.enemy_mtx:
                        if alien.collided_perfect(bullet):
                            self.bullet.bullet_array.remove(bullet)
                            self.enemy.enemy_mtx.remove(alien)

    def game_over(self):
        for alien in self.enemy.enemy_mtx:
            if alien.collided_perfect(self.spaceship.spaceship):
                GVar.STATE = 0
                self.__init__(self.window, self.alien_spawn_adress)
                break