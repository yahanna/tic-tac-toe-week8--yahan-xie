import csv
import os
from datetime import datetime

class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.players = [player1, player2]
        self.current_player = 0
        self.first_player = player1.symbol  # 记录首先移动的玩家
        self.first_moves = {player1.symbol: None, player2.symbol: None}  # 新增，用于记录每位玩家的首步

    def print_board(self):
        for row in self.board:
            print(' | '.join([str(cell) if cell else ' ' for cell in row]))
        print()

    def get_winner(self):
        # Check rows
        for row in self.board:
            if len(set(row)) == 1 and row[0] is not None:
                return row[0]

        # Check columns
        for i in range(3):
            column = [self.board[j][i] for j in range(3)]
            if len(set(column)) == 1 and column[0] is not None:
                return column[0]

        # Check diagonals
        top_left_to_bottom_right = [self.board[i][i] for i in range(3)]
        if len(set(top_left_to_bottom_right)) == 1 and top_left_to_bottom_right[0] is not None:
            return top_left_to_bottom_right[0]

        top_right_to_bottom_left = [self.board[i][2-i] for i in range(3)]
        if len(set(top_right_to_bottom_left)) == 1 and top_right_to_bottom_left[0] is not None:
            return top_right_to_bottom_left[0]

        return None

    def play_game(self):
        winner = None
        if self.first_moves[self.players[self.current_player].symbol] is None:
            self.first_moves[self.players[self.current_player].symbol] = (row, col)


        while winner is None:
            self.print_board()
            row, col = self.players[self.current_player].make_move(self.board)

            self.board[row][col] = self.players[self.current_player].symbol
            winner = self.get_winner()

            if winner is None and all(all(cell is not None for cell in row) for row in self.board):
                print("It's a draw!")
                self.print_board()
                return
            self.current_player = 1 - self.current_player

        print(f'Player {winner} wins!')
        self.print_board()

    def log_game_result(self):
        winner = self.get_winner()
        result = 'Draw' if winner is None else f'Player {winner}'
        winning_first_move = self.first_moves[winner] if winner else None
        log_data = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'player1_symbol': self.players[0].symbol,
            'player2_symbol': self.players[1].symbol,
            'first_player': self.first_player,
            'winner': result,
            'winning_first_move': winning_first_move  # 新增
        }
        self.write_log(log_data)

    @staticmethod
    def write_log(data):
        log_file = 'game_log1.csv'
        if len(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
        
        file_exists = os.path.isfile(log_file)

        with open(log_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
