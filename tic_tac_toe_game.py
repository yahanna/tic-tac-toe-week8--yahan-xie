class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.players = [player1, player2]
        self.current_player = 0

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
