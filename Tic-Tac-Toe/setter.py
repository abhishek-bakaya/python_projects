from random import choice

def set_turn(players):

    first_turn = choice(players)
    second_turn = [player for player in players if player != first_turn][0]
    print(f"\n{first_turn} goes first!!!\n")

    return (first_turn, second_turn)
# --------------------------------------------------------------------

def set_player_marker(turn, player_markers):
    
    first_turn, second_turn = turn
    
    markers = ['X', 'O']
    while player_markers[first_turn] not in markers:
        player_markers[first_turn] = input(f"{first_turn}, pick a marker (X or O): ").upper().strip()
    else:
        player_markers[second_turn] = [marker for marker in markers\
        if marker != player_markers[first_turn]][0]
# --------------------------------------------------------------------

def reset_board():
    board = {x: x for x in range(1, 10)}
    return board
# --------------------------------------------------------------------

def place_marker(player, board, position, player_markers):
    board[position] = player_markers[player]
