from setter import *
from getter import player_input, replay
from display import begin, display_board
from checker import check_full_board, check_win


def main():
    
    title = "TIC-TAC-TOE"
    players = ['Player-1', 'Player-2']
    player_scores = {'Player-1': 0, 'Player-2': 0, 'Draw': 0}
    player_markers = {'Player-1': None, 'Player-2': None}
    board = {x: x for x in range(1, 10)}

    game = 0
    winner = None

    ready = begin(title)
    while ready == 'y':
        
        empty_spaces = list(range(1, 10))
        turn = set_turn(players)
        set_player_marker(turn, player_markers)
        game += 1
        game_is_on = True

        while game_is_on:
            for i in range(2):

                display_board(title, game, player_markers, player_scores, board)
                position = player_input(board, turn[i], empty_spaces)
                empty_spaces.remove(position)
                place_marker(turn[i], board, position, player_markers)
                
                winner = check_win(board, player_markers)
                if winner in players:

                    player_scores[winner] += 1
                    display_board(title, game, player_markers, player_scores, board)
                    print(f"\n{winner} won.")
                    ready = replay()
                    board = reset_board()
                    game_is_on = False
                    break
                
                if check_full_board(board):
                    
                    player_scores['Draw'] += 1
                    display_board(title, game, player_markers, player_scores, board)
                    print("\nIt's a draw.")
                    ready = replay()
                    board = reset_board()
                    game_is_on = False
                    break

if __name__ == '__main__': main()