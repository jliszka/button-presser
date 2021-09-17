
from button_presser import *
import time

class Memory(Game):
    def setup(self):
        self.a = None
        for k in range(20):
            self.colors = shuffle([hue(i/8) for i in range(16)])
            for i in range(16):
                self.pixels[i] = self.colors[i]
            time.sleep(max(0.5-k/20, 0.05))
        for i in range(16):
            self.pixels[i] = OFF
        self.colors = shuffle([hue(i/8) for i in range(16)])

    def onButtonDown(self, n):
        if self.a is None:
            self.a = n
            self.pixels[n] = self.colors[n]
        elif self.a != n:
            self.pixels[n] = self.colors[n]
            if self.pixels[self.a] != self.pixels[n]:
                time.sleep(1)
                self.pixels[self.a] = OFF
                self.pixels[n] = OFF
            else:
                time.sleep(0.3)
                for k in range(3):
                    self.pixels[self.a] = OFF
                    self.pixels[n] = OFF
                    time.sleep(0.1)
                    self.pixels[self.a] = self.colors[self.a]
                    self.pixels[n] = self.colors[n]
                    time.sleep(0.1)
            self.a = None

        if all([self.pixels[i] != OFF for i in range(16)]):
            for k in range(3):
                for i in range(16):
                    self.pixels[i] = OFF
                time.sleep(0.3)
                for i in range(16):
                    self.pixels[i] = self.colors[i]
                time.sleep(0.3)
            self.setup()

