
import time
import busio
import board
from adafruit_neotrellis.neotrellis import NeoTrellis
import adafruit_fancyled.adafruit_fancyled as fancy
import random
from analogio import AnalogIn

OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
ORANGE = (255, 64, 0)
WHITE = (255, 255, 255)

def hue(h):
    return fancy.gamma_adjust(fancy.CHSV(h % 1), brightness=0.5).pack()

def now():
    return time.monotonic()

def shuffle(xs):
    n = len(xs)
    for i in range(n-1):
        j = random.randint(i, n-1)
        t = xs[i]
        xs[i] = xs[j]
        xs[j] = t
    return xs

class PixelWrapper:
    def __init__(self, pixels):
        self.pixels = pixels
        self.state = [OFF] * 16

    def __getitem__(self, i):
        return self.state[i]

    def __setitem__(self, i, val):
        self.state[i % 16] = val
        self.pixels[i % 16] = val

class Game:
    def setup(self):
        pass
    def onButtonDown(self, num):
        pass
    def onButtonUp(self, num):
        pass
    def loop(self):
        pass

    def wave(self, color=PURPLE):
        for i in range(16):
            self.pixels[i] = color
            time.sleep(0.02)

        for i in range(16):
            self.pixels[i] = OFF
            time.sleep(0.02)


class ButtonPresser:
    def __init__(self, game):
        random.seed(AnalogIn(board.A2).value)
        # TODO: board.I2C()
        i2c_bus = busio.I2C(board.SCL, board.SDA)
        self.trellis = NeoTrellis(i2c_bus)
        self.neopixels = self.trellis.pixels
        self.pixels = PixelWrapper(self.neopixels)
        self.state = [False] * 16

        for i in range(16):
            # activate rising edge events on all keys
            self.trellis.activate_key(i, NeoTrellis.EDGE_RISING)
            # activate falling edge events on all keys
            self.trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
            # set all keys to trigger the blink callback
            self.trellis.callbacks[i] = self.handler

            self.pixels[i] = OFF

        self.doGame(game)

    def doGame(self, game):
        self.game = game
        self.game.bp = self
        self.game.pixels = self.pixels
        self.game.setup()

    def disable_keys(self):
        for i in range(16):
            # activate rising edge events on all keys
            self.trellis.activate_key(i, NeoTrellis.EDGE_RISING, False)
            # activate falling edge events on all keys
            self.trellis.activate_key(i, NeoTrellis.EDGE_FALLING, False)

    def enable_keys(self):
        for i in range(16):
            # activate rising edge events on all keys
            self.trellis.activate_key(i, NeoTrellis.EDGE_RISING, True)
            # activate falling edge events on all keys
            self.trellis.activate_key(i, NeoTrellis.EDGE_FALLING, True)

    def handler(self, event):
        if event.edge == NeoTrellis.EDGE_RISING:
            self.game.onButtonDown(event.number)
            self.state[event.number] = True
        if event.edge == NeoTrellis.EDGE_FALLING:
            self.game.onButtonUp(event.number)
            self.state[event.number] = False

    def isButtonDown(self, num):
        return self.state[num]

    def run(self):
        while True:
            # call the sync function call any triggered callbacks
            self.trellis.sync()
            # the trellis can only be read every 17 milliseconds or so
            time.sleep(0.02)
            self.game.loop()

