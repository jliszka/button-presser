from button_presser import *

LIGHT_RED = (127, 0, 0)
LIGHT_BLUE = (0, 0, 127)

class TicTacToe(Game):
    def __init__(self, cycle=False):
        self.cycle = cycle

    def setup(self):
        self.red_wins = 0
        self.blue_wins = 0
        self.reset()

    def reset(self):
        self.turn = 1
        self.board = [0] * 9
        self.moves = []
        self.wave(RED)
        self.wave(BLUE)
        self.show()

    def show(self):
        self.pixels[15] = RED if self.turn == 1 else BLUE
        for i in range(3):
            for j in range(3):
                k = 4*i + j
                fade = self.cycle and len(self.moves) > 5 and k == self.moves[5]
                if self.board[k] == 1:
                    self.pixels[k] = LIGHT_RED if fade else RED
                elif self.board[k] == 2:
                    self.pixels[k] = LIGHT_BLUE if fade else BLUE
                else:
                    self.pixels[k] = OFF
        for i in range(self.red_wins):
            self.pixels[3+4*i] = RED
        for i in range(self.blue_wins):
            self.pixels[12+i] = BLUE

    def check(self):
        for i in range(3):
            if self.board[i] == self.board[i+4] == self.board[i+8] != 0:
                return True
            if self.board[4*i] == self.board[4*i+1] == self.board[4*i+2] != 0:
                return True
        if self.board[0] == self.board[5] == self.board[10] != 0:
            return True
        if self.board[2] == self.board[5] == self.board[8] != 0:
            return True
        return False

    def onButtonDown(self, n):
        if self.board[n] == 0:
            if self.cycle and len(self.moves) > 6:
                self.board[self.moves[6]] = 0
            self.board[n] = self.turn 
            self.show()
            if self.check():
                self.wave(RED if self.turn == 1 else BLUE)
                if self.turn == 1:
                    self.red_wins += 1
                else:
                    self.blue_wins += 1
                if self.red_wins == 4:
                    self.wave(RED)
                    time.sleep(1)
                    self.setup()
                if self.blue_wins == 4:
                    self.wave(BLUE)
                    time.sleep(1)
                    self.setup()
                time.sleep(1)
                self.reset()
            else:
                self.turn = 3 - self.turn

    def onButtonUp(self, n):
        pass