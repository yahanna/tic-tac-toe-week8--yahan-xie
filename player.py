# player.py

import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board, row=None, col=None):
        raise NotImplementedError

class HumanPlayer(Player):
    def make_move(self, board, row, col): #check the vadality of the crow and col
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] is not None:
            raise ValueError("Invalid move")
        return row, col

class BotPlayer(Player):
    def make_move(self, board, row=None, col=None):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        return random.choice(empty_cells) if empty_cells else None
