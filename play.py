from spaceship import Spaceship
from enemy import Enemy
from bullet import Bullet

class Play(object):
    def __init__(self, window, alien_spawn_adress):
        self.spaceship = Spaceship(window)
        self.enemy = Enemy(window, alien_spawn_adress)
        self.bullet = Bullet(window)
    
    def run(self):
        self.spaceship.run()
        self.enemy.run()
        self.bullet.run(self.spaceship)