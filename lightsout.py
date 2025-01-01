
from button_presser import *
import random

class LightsOut(Game):
    def setup(self):
        self.wave(GREEN)

        for i in range(20):
            self.toggle(random.randint(0, 15))
            time.sleep(0.05)

    def flip(self, n):
        if self.pixels[n] == OFF:
            self.pixels[n] = hue(n/16)
        else:
            self.pixels[n] = OFF

    def toggle(self, n):
        self.flip(n)
        r = n // 4
        c = n % 4
        if c < 3:
            self.flip(4*r + (c+1))
        if c > 0:
            self.flip(4*r + (c-1))
        if r < 3:
            self.flip(4*(r+1) + c)
        if r > 0:
            self.flip(4*(r-1) + c)

    def onButtonDown(self, n):
        self.toggle(n)

        if all([self.pixels[i] == OFF for i in range(16)]):
            self.setup()
