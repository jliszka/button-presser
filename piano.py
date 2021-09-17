
from button_presser import *
from speaker import *

class Piano(Game):
    def setup(self):
        scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        s1 = [note(n, 4) for n in scale] + [note('C', 5)]
        s2 = [note(n, 5) for n in scale] + [note('C', 6)]
        self.notes = s1 + s2
        self.wave(WHITE)

    def onButtonDown(self, n):
        self.pixels[n] = hue(n/8)
        play(self.notes[n])

    def onButtonUp(self, n):
        self.pixels[n] = OFF
        stop()
