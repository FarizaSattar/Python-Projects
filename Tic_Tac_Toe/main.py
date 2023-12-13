# Tic Tac Toe

''' The code creates a text-based Tic Tac Toe game. '''

def print_board(board):
    # Function to print the Tic Tac Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Function to check if a player has won
    # Check rows for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns for a win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    # Initialize the board with empty spaces
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not game_over:
        # Take input for row and column from the current player
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

        if board[row][col] == ' ':
            # Place the player's symbol on the board
            board[row][col] = current_player
            print_board(board)

            # Check if the current player has won
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                game_over = True
            # Check for a tie if the board is full
            elif all(all(cell != ' ' for cell in row) for row in board):
                print("It's a tie!")
                game_over = True
            else:
                # Switch to the other player for the next turn
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already taken. Try again.")

    print("Game Over!")

# Start the game
tic_tac_toe()
