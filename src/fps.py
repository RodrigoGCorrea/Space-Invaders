class Fps(object):
    def __init__(self, window):
        self.window = window
    
    def print_fps(self, clock):
        self.window.draw_text("fps: ", 39, 20, "./assets/font/pixel.ttf",
                    size=30, color=(255,255,255), bold=False, italic=False)
        fps  = int(clock.get_fps())
        self.window.draw_text(str(fps), 90, 20, "./assets/font/pixel.ttf",
                    size=30, color=(255,255,255), bold=False, italic=False)