
import random

def fill_board():
    pairs = [i // 2 + 1 for i in range(16)]
    random.shuffle(pairs)
    board = [pairs[i:i + 4] for i in range(0, 16, 4)]
    return [list(row) for row in board]


def show_board(board, reveal):
    for i in range(4):
        for j in range(4):
            if reveal[i][j]:
                print(board[i][j], end='  ')
            else:
                print('*', end='  ')
        print()
    print()

def card_location():
    valid_input = False
    while not valid_input:
        position = input("Enter the row (1 to 4) and col (1 to 4) position of the pair): ")
        try:
            row, col = map(int, position.split())  # Get user input for row and col as integers
            row -= 1
            col -= 1
            if not (0 <= row < 4) or not (0 <= col < 4):
                print("Invalid position.")
            else:
                valid_input = True
        except ValueError:
            print("Invalid input.")
    return row, col


def game(board):
    reveal = [[False] * 4 for i in range(4)]  # 4x4 matrix to track revealed cards
    pairs = 0

    while pairs < 8:  # Continue the game until 8 pairs are found
        show_board(board, reveal)

        row1, col1 = card_location()
        while not (0 <= row1 < 4) or not (0 <= col1 < 4) or reveal[row1][col1]:
            # Validate card location input and check if the card is already revealed
            if not (0 <= row1 < 4) or not (0 <= col1 < 4):
                print("Invalid position.")
            else:
                print("Card at this position already faced up. Select position again.")
            row1, col1 = card_location()

        reveal[row1][col1] = True
        show_board(board, reveal)

        row2, col2 = card_location()
        while not (0 <= row2 < 4) or not (0 <= col2 < 4) or reveal[row2][col2]:
            if not (0 <= row2 < 4) or not (0 <= col2 < 4):
                print("Invalid position.")
            else:
                print("Card at this position already faced up. Select position again.")
            row2, col2 = card_location()

        reveal[row2][col2] = True  # Mark the card as revealed
        show_board(board, reveal)

        if board[row1][col1] == board[row2][col2]:
            print("Pair match")
            pairs += 1
        else:
            print("Pair do not match. Select again!")
            reveal[row1][col1] = False  # Mark the cards as unrevealed
            reveal[row2][col2] = False

def main():
    while True:
        board = fill_board()
        game(board)
        input("Enter any key to continue...") # loops while entering any key

main()
