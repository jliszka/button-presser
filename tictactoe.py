
from button_presser import *

LIGHT_RED = (40, 0, 0)
LIGHT_BLUE = (0, 0, 40)

class TicTacToe(Game):
    def __init__(self, cycle=False):
        self.cycle = cycle

    def setup(self):
        self.red_wins = 0
        self.blue_wins = 0
        self.wave(RED)
        self.wave(BLUE)
        self.turn = 1
        self.reset()

    def reset(self):
        self.board = [0] * 12
        self.board[3] = -1
        self.board[7] = -1
        self.board[11] = -1
        self.moves = []
        self.show()

    def show(self):
        self.pixels[15] = RED if self.turn == 1 else BLUE
        for i in range(3):
            for j in range(3):
                k = 4*i + j
                fade = self.cycle and len(self.moves) > 5 and k == self.moves[0]
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
            if self.checkRow(i, i+4, i+8):
                return True
            if self.checkRow(4*i, 4*i+1, 4*i+2):
                return True
        if self.checkRow(0, 5, 10):
            return True
        if self.checkRow(2, 5, 8):
            return True
        return False

    def checkRow(self, i, j, k):
        if self.board[i] == self.board[j] == self.board[k] != 0:
            c = RED if self.turn == 1 else BLUE
            for _ in range(3):
                self.pixels[i] = 0
                self.pixels[j] = 0
                self.pixels[k] = 0
                time.sleep(0.2)
                self.pixels[i] = c
                self.pixels[j] = c
                self.pixels[k] = c
                time.sleep(0.2)
            time.sleep(1)
            return True
        return False

    def onButtonDown(self, n):
        if n < 12 and self.board[n] == 0:
            self.moves.append(n)
            if self.cycle and len(self.moves) > 6:
                self.board[self.moves[0]] = 0
                self.moves = self.moves[1:]
            self.board[n] = self.turn
            self.show()
            if self.check():
                if self.turn == 1:
                    self.red_wins += 1
                else:
                    self.blue_wins += 1
                if self.red_wins == 4 or self.blue_wins == 4:
                    self.setup()
                time.sleep(1)
                self.reset()
            elif len(self.moves) == 9:
                time.sleep(1)
                self.reset()
            self.turn = 3 - self.turn
        self.show()

    def onButtonUp(self, n):
        pass
