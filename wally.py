
from button_presser import *
from random import randint

class Wally(Game):
    def setup(self):
        self.h = 0.5
        self.init()

    def init(self):
        self.wave(hue(self.h))
        self.i = randint(0, 15)

    def onButtonDown(self, n):
        if self.pixels[n] == OFF:
            if n == self.i:
                self.pixels[n] = hue(self.h+0.7)
            else:
                self.pixels[n] = hue(self.h)
        else:
            self.pixels[n] = OFF
            if n == self.i:
                self.h += 0.7
                self.init()



