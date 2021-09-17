# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
from board import SCL, SDA
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis
import adafruit_fancyled.adafruit_fancyled as fancy

print("Hello")

# some color definitions
OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)


# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# create the trellis
trellis = NeoTrellis(i2c_bus)

state = [False] * 16

# this will be called when button events are received
def blink(event):
    # turn the LED on when a rising edge is detected
    if event.edge == NeoTrellis.EDGE_RISING:
        state[event.number] = not state[event.number]

    # turn the LED off when a rising edge is detected
    #elif event.edge == NeoTrellis.EDGE_FALLING:
    #    trellis.pixels[event.number] = OFF


for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink

    # cycle the LEDs on startup
    trellis.pixels[i] = PURPLE
    time.sleep(0.05)

for i in range(16):
    trellis.pixels[i] = OFF
    time.sleep(0.05)

while True:
    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 millisecons or so
    time.sleep(0.02)

    for i in range(16):
        if state[i]:
            hue = i / 16 + (time.monotonic() / 8) % 1
            trellis.pixels[i] = fancy.CHSV(hue % 1, 1.0, 0.4).pack()
        else:
            trellis.pixels[i] = OFF

