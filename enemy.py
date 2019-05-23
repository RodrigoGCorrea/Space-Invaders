from PPlay.sprite import Sprite
from PPlay.keyboard import Keyboard

import GVar

keyboard = Keyboard()

class Enemy(object):
    def __init__(self, window, alien_spawn_adress):
        self.window = window
        self.alien_spawn_adress = alien_spawn_adress
        self.enemy_mtx = []
        self.enemy_speed = GVar.ENEMY_SPEED * GVar.DIFC
        self.spawn(alien_spawn_adress)
        self.speed_change_direction = "False"
    
    def run(self):
        self.move()
        self.__draw()

    def spawn(self, alien_spawn_adress):
        level_control = open(alien_spawn_adress, "r")
        line = level_control.readline()
        lin = 0
        while lin < 5:
            for col in range(len(line)):
                if line[col] == "1":
                    alien = Sprite("./images/alien.png")
                    alien.set_position(265 + col * (alien.width + 10), GVar.ENEMY_SPAWN_HEIGHT + lin * (alien.height + 10))
                    self.enemy_mtx.append(alien)
            lin += 1
            line = level_control.readline()


    def move(self):
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
            alien.x += self.enemy_speed * self.window.delta_time()

    def __draw(self):
        for i in range(len(self.enemy_mtx)):
            self.enemy_mtx[i].draw()