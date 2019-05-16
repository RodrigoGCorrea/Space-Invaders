from PPlay.keyboard import Keyboard
from PPlay.sprite import Sprite

import GVar

keyboard = Keyboard()

class Bullet(object):
    def __init__(self, window):
        self.window = window
        self.bullet_array = []
        self.bullet_speed = GVar.BULLET_SPEED
        self.can_shoot = True
        self.cooldown = 100

    def shoot(self, nave):
        if keyboard.key_pressed("space") and self.can_shoot:
            bullet = Sprite("./images/bullet.png")
            bullet.set_position(nave.x + nave.width/2, nave.y)
            self.bullet_array.append(bullet)
            self.can_shoot = False
        
        if self.can_shoot == False:
            self.cooldown -= self.window.delta_time() * GVar.BULLET_COOLDOWN
            if self.cooldown <= 0:
                self.can_shoot = True
                self.cooldown = 100
    
    def move(self):
        for bullet in self.bullet_array:
            bullet.y -= self.bullet_speed * self.window.delta_time()
            bullet.draw()