from PPlay.window import Window
from PPlay.keyboard import Keyboard
from menu import Menu
from spaceship import Spaceship
import GVar

window = Window(GVar.WIDTH, GVar.HEIGHT)
window.set_title("Space Invaders")
window.set_background_color((0, 0, 0))

keyboard = Keyboard()

menu = Menu(window)
nave = Spaceship(window)

window.update()
while GVar.STATE != 4:
    window.set_background_color((0, 0, 0))

    if keyboard.key_pressed("esc"):
        GVar.STATE = 0
    if GVar.STATE == 0:
        menu.run()
    if GVar.STATE == 1:
        nave.run()

    window.update()