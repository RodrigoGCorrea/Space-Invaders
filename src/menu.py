from assets.PPlay.sprite import Sprite
from assets.PPlay.mouse import Mouse

import GVar


class Menu(object):
    def __init__(self, window):
        self.window = window
        self.play = Sprite("./assets/images/play.png")
        self.difc = Sprite("./assets/images/difc.png")
        self.rank = Sprite("./assets/images/rank.png")
        self.quit = Sprite("./assets/images/quit.png")
        self.mouse = Mouse()
        self.__set_pos()
        self.__draw()

    def run(self):
        if self.mouse.is_over_object(self.play) and self.mouse.is_button_pressed(1):
            GVar.STATE = 1

        if self.mouse.is_over_object(self.difc) and self.mouse.is_button_pressed(1):
            GVar.STATE = 2

        if self.mouse.is_over_object(self.rank) and self.mouse.is_button_pressed(1):
            GVar.STATE = 3

        if self.mouse.is_over_object(self.quit) and self.mouse.is_button_pressed(1):
            GVar.STATE = 4

        self.__draw()

    def __draw(self):
        self.play.draw()
        self.difc.draw()
        self.rank.draw()
        self.quit.draw()

    def __set_pos(self):
        button_distance = (GVar.HEIGHT - 4 * self.play.height)/5
        self.play.set_position(
            GVar.WIDTH/2 - self.play.width/2, button_distance)
        self.difc.set_position(
            GVar.WIDTH/2 - self.play.width/2, 2 * button_distance + self.play.height)
        self.rank.set_position(
            GVar.WIDTH/2 - self.play.width/2, 3 * button_distance + 2 * self.play.height)
        self.quit.set_position(
            GVar.WIDTH/2 - self.play.width/2, 4 * button_distance + 3 * self.play.height)
