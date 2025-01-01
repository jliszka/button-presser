
from button_presser import *
from easy import *
from anna import *
from mara import *
from wally import *
from memory import *
from simon import *
from simon2 import *
from piano import *
from song import *
from lightsout import *

class Switcher(Game):
    def setup(self):
        self.games = [
            Easy(), Wally(3), Mara(), Anna(),
            Memory(), Simon(), Simon2(), Piano(),
            Song(), Wally(1), LightsOut(),
        ]
        for i in range(len(self.games)):
            self.pixels[i] = hue(i/8)

    def onButtonUp(self, n):
        self.bp.doGame(self.games[n])

ButtonPresser(Switcher()).run()


