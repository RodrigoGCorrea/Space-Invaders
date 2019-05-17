from PPlay.sprite import Sprite
from PPlay.gameimage import GameImage

import GVar

class Enemy(object):
    def __init__(self, window, alien_spawn_adress):
        self.window = window
        self.enemy_mtx = []
        self.enemy_speed = 200
        self.spawn(alien_spawn_adress)

    
    def run(self):
        self.move()
        self.__draw()

    def spawn(self, alien_spawn_adress):
        border_1 = GameImage("./images/alien.png")
        border_2 = GameImage("./images/alien.png")
        border_1.set_position(265, 200)
        border_2.set_position(265 + 11 * (border_2.width + 10), 200)
        
        self.enemy_mtx.append(border_1)
        self.enemy_mtx.append(border_2)

        level_control = open(alien_spawn_adress, "r")
        line = level_control.readline()
        lin = 0
        while lin < 5:
            for col in range(len(line)):
                if line[col] == "1":
                    alien = Sprite("./images/alien.png")
                    alien.set_position(265 + col * (alien.width + 10), 200 + lin * (alien.height + 10))
                    self.enemy_mtx.append(alien)
            lin += 1
            line = level_control.readline()


    def move(self):
        speed = GVar.ENEMY_SPEED
        if self.enemy_mtx[0].x == 0:
            speed = -speed
        elif self.enemy_mtx[1].x == (GVar.WIDTH - self.enemy_mtx[1].height):
            speed = -speed
        for alien in self.enemy_mtx:
            alien.x += speed * self.window.delta_time()

    def __draw(self):
        for i in range(2, len(self.enemy_mtx)):
            self.enemy_mtx[i].draw()