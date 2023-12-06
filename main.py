from player import HumanPlayer, BotPlayer
from tic_tac_toe_game import TicTacToeGame
import time
from pprint import pprint
import pandas as pd
import os


def get_player_type(symbol):
    while True:
        choice = input(f"Select player {symbol} type - Another player (2) or bot (1): ")
        if choice == '1':
            return BotPlayer(symbol)
        elif choice == '2':
            return HumanPlayer(symbol)
        else:
            print("Invalid choice. Please enter 1 for bot or 2 for another player.")

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
    player1 = get_player_type('X')
    player2 = get_player_type('O')

    game = TicTacToeGame(player1, player2)
    game_data = []
    move_id = 0
    game_id = time.time()
    inital_time = time.time()
    while True:
        game.print_board()
        if isinstance(game.players[game.current_player], HumanPlayer):
            row, col = get_human_move(game.players[game.current_player].symbol)
            try:
                game.players[game.current_player].make_move(game, row, col)
            except ValueError:
                print("Invalid move. Try again.")
                continue
        else:
            row, col = game.players[game.current_player].make_move(game)
        game.board[row][col] = game.players[game.current_player].symbol
        
        data = {}
        move_id += 1
        duration = time.time() - inital_time
        data['game_id'] = game_id
        data['move_id'] = move_id
        data['move_start_time'] = inital_time
        data['duration'] = duration
        data['move_end_time'] =  inital_time + data['duration'] 
        data['move'] = (row, col)
        data['player'] = game.players[game.current_player].symbol
        inital_time = duration + inital_time
        game_data.append(data)
        # pprint(game_data)
        winner = game.get_winner() 
        # data['winner'] = winner
        if winner or all(all(cell is not None for cell in row) for row in game.board):
            break
        game.current_player = 1 - game.current_player

    game.print_board()
    if winner:
        print(f'Player {winner} wins!')
    else:
        print("It's a draw!")

    game.log_game_result()
    game_df = pd.DataFrame(game_data)
    game_df['winner'] = winner
    if os.path.exists("./real_game_data.csv"):
        df = pd.read_csv("./real_game_data.csv")
        # print(df, game_df)
        pd.concat([df,game_df]).to_csv("./real_game_data.csv", index=False)
    else:
        game_df.to_csv("./real_game_data.csv", index=False)
    
if __name__ == '__main__':
    while True:
        start_game()
        try_again = input("Do you want to play again? (yes/no): ").lower()
        if try_again != 'yes':
            print("Thank you for playing. Goodbye!")
            break
