from spaceship import Spaceship
from enemy import Enemy
from bullet import Bullet
from assets.PPlay.keyboard import Keyboard
from math import exp

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
        self.clock = 0
        self.level = 1
        self.point_total = 0
        self.life = GVar.LIVES

    def run(self):
        self.spaceship.run()
        self.enemy.run()
        self.bullet.run(self.spaceship.spaceship)
        self.game_over()
        self.set_border()
        self.point()
        self.run_clock()
        self.new_level()
        self.print_score()
        self.collision()
        self.print_life()

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
                            self.point_total += int(exp(-0.06 *
                                                        self.clock) * 100)

    def new_level(self):
        if self.level > GVar.LEVEL_AMOUNT:
            self.level = 1
            self.enemy.__init__(
                self.window, "./assets/lvl/level_" + str(self.level) + ".txt")
            GVar.STATE = 0
        if len(self.enemy.enemy_mtx) == 0:
            self.level += 1
            if self.level <= GVar.LEVEL_AMOUNT:
                self.enemy.__init__(
                    self.window, "./assets/lvl/level_" + str(self.level) + ".txt")

    def game_over(self):
        for alien in self.enemy.enemy_mtx:
            if alien.collided_perfect(self.spaceship.spaceship):
                GVar.STATE = 0
                self.__init__(self.window, self.alien_spawn_adress)
                break
        if self.life < 0:
            GVar.STATE = 0
            self.__init__(self.window, self.alien_spawn_adress)

    def run_clock(self):
        if len(self.enemy.enemy_mtx) != 0 and self.enemy.start == True:
            self.clock += self.window.delta_time()
        else:
            self.clock = 0

    def print_score(self):
        score = str(self.point_total)
        if len(score) == 2:
            score = "000" + score
        elif len(score) == 3:
            score = "00" + score
        elif len(score) == 4:
            score = "0" + score
        self.window.draw_text(
            "pontos:", 60, 20, "./assets/font/pixel.ttf", 30, (255, 255, 255))
        self.window.draw_text(str(self.point_total), 150,
                              20, "./assets/font/pixel.ttf", 30, (255, 255, 255))
    
    def collision(self):
        for enemy_bullet in self.enemy.enemy__bullet_mtx:
            if self.spaceship.spaceship.collided(enemy_bullet):
                self.spaceship.__init__(self.window)
                self.enemy.enemy__bullet_mtx.remove(enemy_bullet)
                self.life -= 1

    def print_life(self):
        self.window.draw_text("vidas:", 48, 80, "./assets/font/pixel.ttf", 30, (255, 255, 255))
        self.window.draw_text(str(self.life), 99, 80, "./assets/font/pixel.ttf", 30, (255, 255, 255))