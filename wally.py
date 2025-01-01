
from button_presser import *
from random import randint

class Wally(Game):
    def __init__(self, k):
        self.k = k

    def setup(self):
        self.h = 0.5
        self.init()

    def init(self):
        self.wave(hue(self.h))
        self.i = shuffle([x for x in range(16)])[0:self.k]

    def onButtonDown(self, n):
        if self.pixels[n] == OFF:
            if n in self.i:
                m = self.i.index(n)
                self.pixels[n] = hue(self.h+0.41 + m * 0.15)
            else:
                self.pixels[n] = hue(self.h)
        else:
            self.pixels[n] = OFF
            if n in self.i:
                m = self.i.index(n)
                self.h += 0.41 + m * 0.15
                self.init()



