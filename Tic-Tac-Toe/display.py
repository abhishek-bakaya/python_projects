from os import system

def cls():
    _ = system('cls')
# --------------------------------------------------------------------

def begin(title):
    ready = None
    cls()

    print(f"{title}\n\n" +
          "How to play:\n" +
          "-The first turn will be chosen randomly between the two players.\n" +
          "-You will be displayed the positions in the grid.\n" +
          "-You have to enter the position where you want to mark.\n\n")

    while ready not in ('y', 'n'):
        ready = input("Are you ready? (y/n): ").lower().strip()
    
    return ready
# --------------------------------------------------------------------

def display_board(title, game, player_markers, player_scores, board):

    cls()
    print(f" {title}" +
          f"\t\t\t\tGame: {game}\n\n\t" +
          f"\t\t\t\tPlayer-1 ({player_markers['Player-1']}): {player_scores['Player-1']}\n\t" +
          f"\t\t\t\tPlayer-2 ({player_markers['Player-2']}): {player_scores['Player-2']}\n\t" +
          f"\t\t\t\tDraw\t    : {player_scores['Draw']}")
    

    print(f"  {board[1]} | {board[2]} | {board[3]}\n-------------\n" +
          f"  {board[4]} | {board[5]} | {board[6]}\n-------------\n" +
          f"  {board[7]} | {board[8]} | {board[9]}")