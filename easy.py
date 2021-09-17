
from button_presser import *

class Easy(Game):
    def setup(self):
        self.wave()

    def onButtonDown(self, n):
        if self.pixels[n] == OFF:
            if n < 4:
                row = 1
            elif n < 8:
                row = 2
            elif n < 12:
                row = 3
            else:
                row = 4

            if row % 2 == 0:
                if n % 2 == 0:
                    self.pixels[n] = CYAN
                else:
                    self.pixels[n] = PURPLE
            else:
                if n % 2 == 0:
                    self.pixels[n] = PURPLE
                else:
                    self.pixels[n] = CYAN

        else:
            self.pixels[n] = OFF



