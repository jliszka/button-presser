
from button_presser import *

class Anna(Game):
    def setup(self):
        self.wave(BLUE)

    def onButtonDown(self, n):
        if n < 8:
            if self.pixels[n] == OFF:
                if all([self.pixels[i] != OFF for i in range(n)]):
                    for i in range(n):
                        self.pixels[i] = OFF
                    self.pixels[n] = hue(n/8)
            else:
                if all([self.pixels[i] == OFF for i in range(n)]):
                    for i in range(n):
                        self.pixels[i] = hue(i/8)
                    self.pixels[n] = OFF
        else:
            if n == 8 or (self.pixels[n-1] != OFF and all([self.pixels[i] == OFF for i in range(8, n-1)])):
                if self.pixels[n] == OFF:
                    self.pixels[n] = hue(n/8)
                else:
                    self.pixels[n] = OFF

