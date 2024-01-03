#created by Afia Mushtaq
#Superior University Lahore
#AICP_internship_task_5


# Initialize the board
board = [
    ['','',''],
    ['','',''],
    ['','',''],
]

# To display the board
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# To check if a player won
def check_win(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
            return True
    return False

# To check if the board is full
def is_board_full():
    for row in board:
        if '' in row:
            return False
    return True

# To get a player move
def get_player_move():
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

# To play the Tic Tac Toe game
def play_tic_tac_toe():
    players = ['X', 'O']
    current_player = 0

    while not check_win(players[current_player]) and not is_board_full():
        display_board()

        player_symbol = players[current_player]
        print(f"Player {player_symbol}'s turn")

        row, col = get_player_move()
        board[row][col] = player_symbol

        current_player = (current_player + 1) % 2

    display_board()

    if check_win(players[current_player]):
        winner = players[current_player]
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

# Start the game
play_tic_tac_toe()
