from PPlay.sprite import Sprite
from PPlay.mouse import Mouse

import GVar

mouse = Mouse()

class Difficulty(object):
    def __init__(self, window):
        self.window = window
        self.easy_button = Sprite("./images/easy.png")
        self.norm_button = Sprite("./images/norm.png")
        self.hard_button = Sprite("./images/hard.png")
        self.__set_pos()

    def run(self):
        self.__draw()
        self.set_difficulty()


    def set_difficulty(self):
        if mouse.is_over_object(self.easy_button) and mouse.is_button_pressed(1):
            GVar.DIFC = 1 * GVar.DIFC_MULTIPLIER
            GVar.DIFC_CHOSEN = True
            GVar.STATE = 1
        if mouse.is_over_object(self.norm_button) and mouse.is_button_pressed(1):
            GVar.DIFC = 2 * GVar.DIFC_MULTIPLIER
            GVar.DIFC_CHOSEN = True
            GVar.STATE = 1
        if mouse.is_over_object(self.hard_button) and mouse.is_button_pressed(1):
            GVar.DIFC = 3 * GVar.DIFC_MULTIPLIER
            GVar.DIFC_CHOSEN = True
            GVar.STATE = 1

    def __draw(self):
        self.easy_button.draw()
        self.norm_button.draw()
        self.hard_button.draw()
    
    def __set_pos(self):
        button_distance = (GVar.HEIGHT - 3 * self.easy_button.height)/4
        self.easy_button.set_position(GVar.WIDTH/2 - self.easy_button.width/2, button_distance)
        self.norm_button.set_position(GVar.WIDTH/2 - self.easy_button.width/2, self.easy_button.height + 2 * button_distance)
        self.hard_button.set_position(GVar.WIDTH/2 - self.easy_button.width/2, 2 * self.easy_button.height + 3 * button_distance)
