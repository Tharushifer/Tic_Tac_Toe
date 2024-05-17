def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return (move - 1) // 3, (move - 1) % 3
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        row, col = get_move()
        if board[row][col] == ' ':
            board[row][col] = players[current_player]
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = (current_player + 1) % 2
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    main()