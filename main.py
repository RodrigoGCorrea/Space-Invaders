from PPlay.window import Window
from PPlay.keyboard import Keyboard
from menu import Menu
from play import Play
from difficulty import Difficulty
import GVar

window = Window(GVar.WIDTH, GVar.HEIGHT)
window.set_title("Space Invaders")
window.set_background_color((0, 0, 0))

keyboard = Keyboard()

menu = Menu(window)
play = Play(window, "./lvl/alien_spawn.txt")
difficulty_menu = Difficulty(window)

window.update()
while GVar.STATE != 4:
    window.set_background_color((0, 0, 0))

    if keyboard.key_pressed("esc"):
        GVar.STATE = 0
        play.__init__(window, "./lvl/alien_spawn.txt")
    if GVar.STATE == 0:
        menu.run()
    if GVar.STATE == 1:
        if GVar.DIFC_CHOSEN == True:
            play.__init__(window, "./lvl/alien_spawn.txt")
            GVar.DIFC_CHOSEN = False
        play.run()
    if GVar.STATE == 2:
        difficulty_menu.run()
    window.update()