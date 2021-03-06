from assets.PPlay.sprite import Sprite
from assets.PPlay.keyboard import Keyboard
from random import randint, random

import GVar

keyboard = Keyboard()

class Enemy(object):
    def __init__(self, window, alien_spawn_adress):
        self.window = window
        self.enemy_mtx = []
        self.enemy__bullet_mtx = []
        self.enemy_speed = GVar.ENEMY_SPEED * GVar.DIFC * GVar.DIFC_MULTIPLIER
        self.spawn(alien_spawn_adress)
        self.speed_change_direction = "False"
        self.start = False
        self.can_shoot = False
        self.set_cooldown = False
        self.bullet_cooldown = 100
    
    def run(self):
        self.move()
        self.__draw()
        self.move_bullet()
        self.shoot()
        self.destroy()

    def spawn(self, alien_spawn_adress):
        level_control = open(alien_spawn_adress, "r")
        line = level_control.readline()
        lin = 0
        while lin < 7:
            for col in range(len(line)):
                if line[col] == "1":
                    alien = Sprite("./assets/images/alien.png")
                    alien.set_position(265 + col * (alien.width + 10), GVar.ENEMY_SPAWN_HEIGHT + lin * (alien.height + 10))
                    self.enemy_mtx.append(alien)
            lin += 1
            line = level_control.readline()


    def move(self):
        #start game
        if keyboard.key_pressed("enter"):
            self.start = True
        if len(self.enemy_mtx) == 0:
            self.start = False
        #change speed
        for alien in self.enemy_mtx:
            if alien.x <= 0:
                self.speed_change_direction = "left"
                self.enemy_speed = -self.enemy_speed
                break
            elif alien.x >= (GVar.WIDTH - alien.width):
                self.speed_change_direction = "right"
                self.enemy_speed = -self.enemy_speed
                break
        #reset position
        if self.speed_change_direction == "left":
            self.speed_change_direction = "False"
            for alien in self.enemy_mtx:
                alien.set_position(alien.x + 2, alien.y + alien.height)
        elif self.speed_change_direction == "right":
            self.speed_change_direction = "False"
            for alien in self.enemy_mtx:
                alien.set_position(alien.x - 2, alien.y + alien.height)
        #move
        for alien in self.enemy_mtx:
            if self.start == True:
                alien.x += self.enemy_speed * self.window.delta_time()

    def __draw(self):
        for i in range(len(self.enemy_mtx)):
            self.enemy_mtx[i].draw()

    def shoot(self):
        if self.can_shoot == True and self.set_cooldown == False:
            self.bullet_cooldown = 100 + randint(0, 50)
            self.set_cooldown = True

        if self.can_shoot:
            alien = self.enemy_mtx[randint(0, len(self.enemy_mtx) -1)]
            bullet = Sprite("./assets/images/bullet.png")
            bullet.set_position(alien.x + alien.width/2, alien.y + alien.height)
            self.enemy__bullet_mtx.append(bullet)
            self.can_shoot = False
            self.set_cooldown = False
        
        if self.can_shoot == False:
            self.bullet_cooldown -= self.window.delta_time() * GVar.ENEMY_BULLET_COOLDOWN
            if self.bullet_cooldown < 0:
                self.can_shoot = True
    
    def move_bullet(self):
        for bullet in self.enemy__bullet_mtx:
            bullet.y += GVar.BULLET_SPEED * self.window.delta_time()
            bullet.draw()
    
    def destroy(self):
        for bullet in self.enemy__bullet_mtx:
            if bullet.y > GVar.HEIGHT:
                self.enemy__bullet_mtx.remove(bullet)