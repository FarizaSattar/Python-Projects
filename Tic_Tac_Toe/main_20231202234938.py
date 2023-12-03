# Tic Tac Toe

''' The code defines functions to manage a text-based Tic Tac Toe game where players take turns marking their 
symbol ('X' or 'O') on a 3x3 board, checking for a winner or a tie after each move until the game concludes. 
'''

def print_board(board):
    # Function to print the Tic Tac Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Function to check if a player has won
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not game_over:
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                game_over = True
            elif all(all(cell != ' ' for cell in row) for row in board):
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already taken. Try again.")

    print("Game Over!")

# Start the game
tic_tac_toe()
