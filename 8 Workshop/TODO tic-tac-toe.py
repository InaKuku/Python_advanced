# Code of Ines Ivanova
# For debugging !!!

@@ -6,4 +6,62 @@ def get_row_col(pos): #file: workshop/tic_tac_toe/core/helpers.py


def print_current_board_state(board):
    [print(f"| {' | '.join(el)} |") for el in board]
    [print(f"| {' | '.join(el)} |") for el in board]


def is_board_full(board):
    is_full = True
    for row in board:
        if " " in row:
            is_full = False
    return is_full


def is_row_winner(board):
    for row in board:
        if row.count('X') == len(row) or row.count('O') == len(row):
            return True
    return False


def is_col_winner(board):
    is_found = False

    first = [board[0][0], board[1][0], board[2][0]]
    second = [board[0][1], board[1][1], board[2][1]]
    third = [board[0][2], board[1][2], board[2][2]]

    if first.count('X') == len(board) or first.count('O') == len(board):
        is_found = True
    elif second.count('X') == len(board) or second.count('O') == len(board):
        is_found = True
    elif third.count('X') == len(board) or third.count('O') == len(board):
        is_found = True
    return is_found


def is_primary_diagonal_winner(board):
    current_values = []
    for row in range(len(board)):
        current_values.append(board[row][row])
    if current_values.count("X") == len(board) or current_values.count("O") == len(board):
        return True
    return False


def is_second_diagonal_winner(board):
    current_values = []
    n = len(board)
    for i in range(len(board)):
        current_values.append(board[n-i-1][i])

    if current_values.count("X") == len(board) or current_values.count("O") == len(board):
        return True
    return False


def is_winner(board):
    if is_row_winner(board) or is_col_winner(board) \
            or is_primary_diagonal_winner(board) or is_second_diagonal_winner(board):
        return True
    return False
  33  workshop/tic_tac_toe/core/logic.py


@@ -1,5 +1,10 @@    #file: workshop/tic_tac_toe/core/logic.py
from workshop.tic_tac_toe.core.validators import is_position_in_range, is_place_available
from workshop.tic_tac_toe.core.helpers import get_row_col, print_current_board_state
from workshop.tic_tac_toe.core.helpers import (
    get_row_col,
    print_current_board_state,
    is_winner,
    is_board_full
)


def play(players, board, turns):
@@ -8,17 +13,21 @@ def play(players, board, turns):
    while True:
        current_player_name = turns[current_turn_count%2]
        position = int(input(f"{current_player_name} choose a free position: "))
        if is_position_in_range(position):
            if is_place_available(board, position):
                row, col = get_row_col(position)
                board[row][col] = players[current_player_name]
                print_current_board_state(board)
            # check if there is a winner
            # check if there is not a winner if the board is full
            a = 5
        else:
            # Read new position for the same player
            pass
        if current_turn_count >= 3:
            if is_position_in_range(position):
                if is_place_available(board, position):
                    row, col = get_row_col(position)
                    board[row][col] = players[current_player_name]
                    print_current_board_state(board)
                    if is_winner(board):
                        print(f"{current_player_name} wins")
                        exit(0)
                    if is_board_full(board):
                        print("Game over! No winner!")
                        exit(0)
            else:
                # Read new position for the same player
                pass

        current_turn_count += 1


@@ -0, 0 + 1, 55 @ @                           #file: workshop/tic_tac_toe/test_cases.txt
# winner on a row
Peter
John
X
1
4
2
5
7
6

# winner on a col
Peter
John
X
1
2
4
5
7

# winner on a diagonal
Peter
John
X
1
4
5
6
9

# winner on second diagonal
Peter
John
X
3
1
5
2
7


# no winner board is full
Peter
John
X
1
4
2
5
7
8
6
3
9