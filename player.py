# player.py

import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, game, row=None, col=None):
        raise NotImplementedError
    
class HumanPlayer(Player):
    def make_move(self, game, row, col): #check the vadality of the crow and col
        if row < 0 or row > 2 or col < 0 or col > 2 or game.board[row][col] is not None:
            raise ValueError("Invalid move")
        game.current_player = 1 - game.current_player

        return row, col
    
class BotPlayer(Player):
    def make_move(self, game, row=None, col=None):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if game[i][j] is None]
        return random.choice(empty_cells) if empty_cells else None
