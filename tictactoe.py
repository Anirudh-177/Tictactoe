import random


# We create and print the board
# It will print the string in the board[i] and | etc
def display_board(row, col):
    print(' Available  \n ' +
          row[7] + '|' + row[8] + '|' + row[9] + '         ' + col[7] + '|' + col[8] + '|' + col[9] + '\n ' +
          row[4] + '|' + row[5] + '|' + row[6] + '         ' + col[4] + '|' + col[5] + '|' + col[6] + '\n ' +
          row[1] + '|' + row[2] + '|' + row[3] + '         ' + col[1] + '|' + col[2] + '|' + col[3] + '\n')


# Placing the marker
def place_marker(avail, board, marker, position):
    board[position] = marker
    avail[position] = ' '


# Function that checks if there is any win
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


# Choose randomly a player
def random_player():
    return random.choice((-1, 1))


# Check if the position that has been chosen is available
def space_check(board, position):
    return board[position] == ' '


# Checks if the board is full and returns a True if its full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Takes the players choice
def player_choice(board, player):
    pchoice = int(input(' Please Player %s choose your next move (1-9).' % (player)))

    while space_check(board, pchoice) == False:
        pchoice = int(input(' You cannot move to this position, please try an another one.'))
    return pchoice


# Asks the player if they want to play again
def replay():
    return input(' Do you want to play again? Type Yes or No: ').lower().startswith('y')

    #######################
    # Setting up the game #
    #######################


while True:
    # It prints 100 lines to "update" the boards on the screen
    print('\n' * 100)
    print(' Welcome to Tic Tac Toe!\n\n')

    # Global variables
    # Reset the board
    theBoard = [' '] * 10
    # A list with the available moves
    available = [str(num) for num in range(0, 10)]
    # player[1] == "X" player[2] == "O"
    players = [0, 'X', 'O']

    rdmplr = random_player()
    player = players[rdmplr]
    print(' For this round, Player %s will go first!\n' % (player))

    game_on = True
    while game_on:
        display_board(available, theBoard)
        position = player_choice(theBoard, player)
        place_marker(available, theBoard, player, position)

        if win_check(theBoard, player):
            display_board(available, theBoard)
            print(' Congratulations Player ' + player + ' you WON!\n')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(available, theBoard)
                print(' Its a draw.')
                break
            else:
                rdmplr *= -1
                player = players[rdmplr]
                print('\n' * 100)

    if not replay():
        break

