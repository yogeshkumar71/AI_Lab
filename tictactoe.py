import random
board = [" " for _ in range(9)]
WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]
def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()
def check_winner():
    """
    Recheck the board using every winning combination.
    Returns:
        'X' -> X wins
        'O' -> O wins
        'Draw' -> board is full
        None -> game continues
    """
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if " " not in board:
        return "Draw"

    return None
def human_move():
    while True:
        try:
            position = int(input("Enter your position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Choose a number from 1 to 9.")
            elif board[position] != " ":
                print("That position is already occupied.")
            else:
                board[position] = "X"
                break

        except ValueError:
            print("Please enter a number.")


def ai_move():
    empty_positions = [
        i for i in range(9)
        if board[i] == " "
    ]
    position = random.choice(empty_positions)
    board[position] = "O"

    print(f"AI chose position {position + 1}")


def main():
    print("TIC-TAC-TOE")
    print("You are X, AI is O")

    while True:
        display_board()
        human_move()
        result = check_winner()

        if result is not None:
            display_board()

            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")

            break
        ai_move()
        result = check_winner()

        if result is not None:
            display_board()

            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")

            break
if __name__ == "__main__":
    main()
