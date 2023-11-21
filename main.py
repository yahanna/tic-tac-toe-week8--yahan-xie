#make move method accept rows and columus as argumengts
#make it possible to simulate the player's movement without a human input 
from player import HumanPlayer, BotPlayer
from tic_tac_toe_game import TicTacToeGame

def get_human_move(symbol):
    while True:
        try:
            move = input(f"{symbol}, enter your move (row, column): ")
            row, col = move.split(",")
            row, col = int(row.strip()), int(col.strip())
            return row, col
        except ValueError:
            print("Please enter two numbers separated by a comma. For example: 1,2")
        except IndexError:
            print("Please enter two numbers separated by a comma. For example: 1,2")

def start_game():
    player1 = HumanPlayer('X')
    choice = input("Play against another player (2) or bot (1)? ")
    player2 = BotPlayer('O') if choice == '1' else HumanPlayer('O')

    game = TicTacToeGame(player1, player2)

    while True:
        game.print_board()
        if isinstance(game.players[game.current_player], HumanPlayer):
            row, col = get_human_move(game.players[game.current_player].symbol)
            try:
                game.players[game.current_player].make_move(game.board, row, col)
            except ValueError:
                print("Invalid move. Try again.")
                continue
        else:
            row, col = game.players[game.current_player].make_move(game.board)
        game.board[row][col] = game.players[game.current_player].symbol

        winner = game.get_winner()
        if winner or all(all(cell is not None for cell in row) for row in game.board):
            break

        game.current_player = 1 - game.current_player

    game.print_board()
    if winner:
        print(f'Player {winner} wins!')
    else:
        print("It's a draw!")

if __name__ == '__main__':
    while True:
        start_game()
        try_again = input("Do you want to play again? (yes/no): ").lower()
        if try_again != 'yes':
            print("Thank you for playing. Goodbye!")
            break
