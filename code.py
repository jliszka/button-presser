
from button_presser import *
from easy import *
from anna import *
from mara import *
from wally import *
from memory import *
from simon import *
from simon2 import *
from piano import *

class Switcher(Game):
    def setup(self):
        self.games = [Easy(), Wally(), Mara(), Anna(), Memory(), Simon(), Simon2(), Piano()]
        for i in range(len(self.games)):
            self.pixels[i] = hue(i/8)

    def onButtonUp(self, n):
        self.bp.doGame(self.games[n])

ButtonPresser(Switcher()).run()


