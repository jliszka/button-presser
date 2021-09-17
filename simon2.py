
from button_presser import *
from speaker import *
import random

class Simon2(Game):
    def setup(self):
        self.sectors = [0, GREEN, RED, BLUE, YELLOW]
        self.notes = [0, note('E'), note('A'), note('E', 5), note('C#', 5)]
        self.order = [random.randint(1, 4) for i in range(16)]
        self.level = 1
        self.press = 0
        for i in range(16):
            self.pixels[i] = OFF
        self.show()

    def sector_to_pixels(self, sector):
        if sector == 1:
            return [0, 1, 4, 5]
        elif sector == 2:
            return [2, 3, 6, 7]
        elif sector == 3:
            return [10, 11, 14, 15]
        else:
            return [8, 9, 12, 13]

    def pixel_to_sector(self, n):
        for sector in [1, 2, 3, 4]:
            if n in self.sector_to_pixels(sector):
                return sector

    def show(self):
        self.bp.disable_keys()
        time.sleep(1)
        for i in range(self.level):
            play(self.notes[self.order[i]])
            for p in self.sector_to_pixels(self.order[i]):
                self.pixels[p] = self.sectors[self.order[i]]
            time.sleep(0.4)
            for p in self.sector_to_pixels(self.order[i]):
                self.pixels[p] = OFF
            stop()
            time.sleep(0.1)
        self.bp.enable_keys()

    def onButtonDown(self, n):
        sector = self.pixel_to_sector(n)
        play(self.notes[sector])
        for p in self.sector_to_pixels(sector):
            self.pixels[p] = self.sectors[sector]

    def onButtonUp(self, n):
        stop()
        sector = self.pixel_to_sector(n)
        for p in self.sector_to_pixels(sector):
            self.pixels[p] = OFF

        if sector == self.order[self.press]:
            self.press += 1
            if self.press == self.level:
                self.level += 1
                self.press = 0
                if self.level == 17:
                    for k in range(5):
                        for i in range(16):
                            self.pixels[i] = self.sectors[self.pixel_to_sector(i)]
                        time.sleep(0.3)
                        for i in range(16):
                            self.pixels[i] = OFF
                        time.sleep(0.3)
                    self.setup()
                    return
                self.show()
        else:
            for k in range(3):
                play(note('C'))
                for p in self.sector_to_pixels(self.order[self.press]):
                    self.pixels[p] = self.sectors[self.order[self.press]]
                time.sleep(0.05)
                stop()
                for p in self.sector_to_pixels(self.order[self.press]):
                    self.pixels[p] = OFF
                time.sleep(0.05)
            self.show()
            self.press = 0

