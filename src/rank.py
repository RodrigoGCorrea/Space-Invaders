import GVar


def check_rank(score):
    file = open("./assets/rank/rank.txt", "r")
    lines = file.readlines()
    file.close()
    maior = False
    for i in range(len(lines)):
        new_line = lines[i].strip()
        lines[i] = new_line
        if score > int(new_line) and maior == False:
            lines.insert(i, str(score))
            maior = True
            lines.pop(len(lines) - 1)
    file = open("./assets/rank/rank.txt", "w")
    for i in range(len(lines)):
        file.write(lines[i] + "\n")
    file.close()
    maior = False


class Rank(object):
    def __init__(self, window):
        self.window = window

    def print_rank(self):
        file = open("./assets/rank/rank.txt", "r")
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            new_line = lines[i].strip()
            lines[i] = new_line
            self.window.draw_text(str(i+1) + ". " + new_line, GVar.WIDTH/2, GVar.HEIGHT/2 + ((i - 1)*150), "./assets/font/pixel.ttf",
                                  size=90, color=(255, 255, 255))

    def run(self):
        self.print_rank()
