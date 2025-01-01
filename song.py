
from button_presser import *
from speaker import *

class Song(Game):
    def play(self, n, d=0.25):
        self.pixels[n] = hue(n/8)
        play(self.notes[n])
        time.sleep(d-0.01)
        stop()
        self.pixels[n] = OFF
        time.sleep(0.01)

    def setup(self):
        self.wave(GREEN)
        scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        s1 = [note(n, 4) for n in scale] + [note('C', 5)]
        s2 = [note(n, 5) for n in scale] + [note('C', 6)]
        self.notes = s1 + s2

        song = [8, 9]
        song += [10, 12, 11, 11, 13, 12, 12, 15, 14]
        song += [15, 12, 10, 8, 9, 10, 11, 12, 13, 12, 11, 10]
        song += [9, 10, 8, 6, 7, 9, 4, 6, 9, 11, 10, 9, 10, 8, 9]
        song += [10, 12, 11, 11, 13, 12, 12, 15, 14]
        song += [15, 12, 10, 8, 9, 10, 4, 12, 11, 10, 9, 8]
        song += [4, 7, 6, 8, 10, 12, 15, 12, 10, 8, 10, 12, 15]
        while True:
            for n in song:
                self.play(n)
