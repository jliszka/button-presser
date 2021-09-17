
from button_presser import *

class Mara(Game):
    def setup(self):
        self.wave(ORANGE)
        self.state = [False] * 16

    def onButtonDown(self, n):
        self.state[n] = not self.state[n]

    def loop(self):
        for i in range(16):
            if self.state[i]:
                self.pixels[i] = hue(i/16 + now() / 5)
            else:
                self.pixels[i] = OFF


