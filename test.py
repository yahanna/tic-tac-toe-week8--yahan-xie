# tests.py
import unittest
from tic_tac_toe_game import TicTacToeGame
from player import HumanPlayer, BotPlayer

class TestTicTacToeGame(unittest.TestCase):
    
    def test_initial_board_empty(self):
        game = TicTacToeGame(HumanPlayer('X'), BotPlayer('O'))
        self.assertTrue(all(all(cell is None for cell in row) for row in game.board))

    def test_player_assignment(self):
        human = HumanPlayer('X')
        bot = BotPlayer('O')
        game = TicTacToeGame(human, bot)
        self.assertEqual(game.players[0].symbol, 'X')
        self.assertEqual(game.players[1].symbol, 'O')

    def test_alternating_turns(self):
        game = TicTacToeGame(HumanPlayer('X'), BotPlayer('O'))
        game.board[0][0] = 'X'
        game.current_player = 1  # Assuming 'X' was player 0
        game.board[1][0] = 'O'
        self.assertEqual(game.board[1][0], 'O')

    def test_winner_detection(self):
        game = TicTacToeGame(HumanPlayer('X'), BotPlayer('O'))
        # Create a winning condition
        x_winning_cases = [
            [['X', 'X', 'X'], [None, 'O', None], [None, 'O', None]],
            [[None, 'O', None], ['X', 'X', 'X'], [None, 'O', None]],
            [[None, 'O', None], [None, 'O', None], ['X', 'X', 'X']],
            [['X', None, None], ['X', 'O', None], ['X', None, 'O']],
            [[None, 'X', 'O'], [None, 'X', 'O'], [None, 'X', None]],
            [[None, None, 'X'], [None, 'O', 'X'], [None, None, 'X']],
            [['X', 'O', None], [None, 'X', 'O'], [None, None, 'X']],
            [[None, 'O', 'X'], [None, 'X', 'O'], ['X', None, None]]
        ]
        for case in x_winning_cases:
            game.board = case
            winner = game.get_winner()
            # Check that the winner is 'X'
            self.assertEqual(winner, 'X')
        o_winning_cases = [
            [['O', 'O', 'O'], [None, 'X', None], [None, 'X', None]],
            [[None, 'X', None], ['O', 'O', 'O'], [None, 'X', None]],
            [[None, 'X', None], [None, 'X', None], ['O', 'O', 'O']],
            [['O', None, None], ['O', 'X', None], ['O', None, 'X']],
            [[None, 'O', 'X'], [None, 'O', 'X'], [None, 'O', None]],
            [[None, None, 'O'], [None, 'X', 'O'], [None, None, 'O']],
            [['O', 'X', None], [None, 'O', 'X'], [None, None, 'O']],
            [[None, 'X', 'O'], [None, 'O', 'X'], ['O', None, None]]
        ]
        for case in o_winning_cases:
            game.board = case
            winner = game.get_winner()
            # Check that the winner is 'O'
            self.assertEqual(winner, 'O')

    def test_draw_detection(self):
        game = TicTacToeGame(HumanPlayer('X'), BotPlayer('O'))
        # Create a draw condition
        game.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        winner = game.get_winner()
        self.assertIsNone(winner)
        self.assertTrue(all(all(cell is not None for cell in row) for row in game.board))

    def test_invalid_move_detection(self):
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        game.board[0][0] = 'X'
        with self.assertRaises(ValueError):
         game.players[1].make_move(game, 0, 0)

if __name__ == '__main__':
    unittest.main()
