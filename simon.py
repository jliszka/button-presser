
from button_presser import *

class Simon(Game):
    def setup(self):
        self.order = shuffle([i for i in range(16)])
        self.level = 1
        self.press = 0
        for i in range(16):
            self.pixels[i] = OFF
        self.show()

    def show(self):
        self.bp.disable_keys()
        time.sleep(1)
        for i in range(self.level):
            self.pixels[self.order[i]] = hue(self.order[i]/16)
            time.sleep(0.4)
            self.pixels[self.order[i]] = OFF
        self.bp.enable_keys()

    def onButtonDown(self, n):
        self.pixels[n] = hue(n/16)

    def onButtonUp(self, n):
        self.pixels[n] = OFF
        if n == self.order[self.press]:
            self.press += 1
            if self.press == self.level:
                self.level += 1
                self.press = 0
                if self.level == 17:
                    for k in range(5):
                        for i in range(16):
                            self.pixels[i] = hue(i/16)
                            time.sleep(0.3)
                            self.pixels[self.order[i]] = OFF
                            time.sleep(0.3)
                            self.setup()
                            return
                self.show()
        else:
            self.press = 0
            for k in range(3):
                self.pixels[n] = hue(n/16)
                time.sleep(0.05)
                self.pixels[n] = OFF
                time.sleep(0.05)
            self.show()
