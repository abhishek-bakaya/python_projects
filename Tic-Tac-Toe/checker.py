def check_space(board, position):
    return type(board[position]) == int
# --------------------------------------------------------------------

def check_full_board(board):
    for i in list(board.values()):
        if type(i) != str:
            return False
    return True
# --------------------------------------------------------------------

def check_win(board, player_markers):

    # Horizontal win
    for i in range(1, 10, 3):
        if board[i] == board[i+1] == board[i+2]:
            for player, marker in player_markers.items():
                if board[i] == marker:
                    return player
    
    # Vertical win
    for i in range(1, 4):
        if board[i] == board[i+3] == board[i+6]:
            for player, marker in player_markers.items():
                if board[i] == marker:
                    return player
    
    # Diagonal win
    if board[1] == board[5] == board[9]:
        for player, marker in player_markers.items():
            if board[1] == marker:
                return player
    
    elif board[3] == board[5] == board[7]:
        for player, marker in player_markers.items():
            if board[3] == marker:
                return player
    
    return None
