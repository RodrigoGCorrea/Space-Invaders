from spaceship import Spaceship
from enemy import Enemy
from bullet import Bullet
from PPlay.keyboard import Keyboard

keyboard = Keyboard()

class Play(object):
    def __init__(self, window, alien_spawn_adress):
        self.window = window
        self.alien_spawn_adress = alien_spawn_adress
        self.spaceship = Spaceship(window)
        self.enemy = Enemy(window, alien_spawn_adress)
        self.bullet = Bullet(window)
    
    def run(self):
        self.spaceship.run()
        self.enemy.run()
        self.bullet.run(self.spaceship.spaceship)
        self.point()
    
    def point(self):
        for bullet in self.bullet.bullet_array:
            for alien in self.enemy.enemy_mtx:
                if bullet.collided_perfect(alien):
                    self.enemy.enemy_mtx.remove(alien)
                    self.bullet.bullet_array.remove(bullet)