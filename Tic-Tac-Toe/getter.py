from checker import check_space

def player_input(board, player, empty_spaces):
    position = None

    while position not in range(1, 10) or not check_space(board, position):

        try:
            position = int(input(f"\n{player}'s turn: ").strip())    
        except ValueError:
            print("Invalid input!!!")
        else:
            if position not in range(1, 10):
                print("Out of range!!!")
                continue
            
            if position not in empty_spaces:
                print("Already marked there.")

    return position
# --------------------------------------------------------------------

def replay():
    ready = None
    while ready not in ('y', 'n'):
        ready = input("\nPlay again? (y/n): ").lower().strip()

    return ready
