# 3 Exercise
# MULTIDIMENSIONAL LISTS

# Chess is the oldest game, but it is still popular these days. For this task, we will use only one chess piece - the Knight.
# A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the
# same row, column, or diagonal. (Foe example it can move two squares
# horizontally, then one square vertically, or it can move one square
# horizontally then two squares vertically - i.e. in an "L" pattern.) 
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. Your
# task is to remove knights until there are no knights left that can attack one
# another.
# Input
#  On the first line, you will receive integer N - size of the board
#  On the next N lines, you will receive strings with &quot;K&quot; and &quot;0&quot;
#
# Output
#  Print a single integer with the minimum number of knights that need to be removed
# Constraints
#  The size of the board will be 0 < N  < 30
#  Time limit: 0.3 sec. Memory limit: 16 MB

rows = int(input())

matrix = []
knight_dict = {}
index_list = []
max = 0
max_Found = False
remove_counter = 0


for row in range(rows):
    matrix.append(list(input()))


def check_func(knight_position_row, knight_position_col):
    k_counter = 0
    if 0 <= knight_position_row - 2 <= rows - 1 and 0 <= knight_position_col - 1 <= rows - 1:
        knight_range_12_left = matrix[knight_position_row - 2][knight_position_col - 1]
        if knight_range_12_left == "K":
            k_counter += 1
    if 0 <= knight_position_row - 2 <= rows - 1 and 0 <= knight_position_col + 1 <= rows - 1:
        knight_range_12_right = matrix[knight_position_row - 2][knight_position_col + 1]
        if knight_range_12_right == "K":
            k_counter += 1
    if 0 <= knight_position_row - 1 <= rows - 1 and 0 <= knight_position_col + 2 <= rows - 1:
        knight_range_3_left = matrix[knight_position_row - 1][knight_position_col + 2]
        if knight_range_3_left == "K":
            k_counter += 1
    if 0 <= knight_position_row + 1 <= rows - 1 and 0 <= knight_position_col + 2 <= rows - 1:
        knight_range_3_right = matrix[knight_position_row + 1][knight_position_col + 2]
        if knight_range_3_right == "K":
            k_counter += 1
    if 0 <= knight_position_row + 2 <= rows - 1 and 0 <= knight_position_col + 1 <= rows - 1:
        knight_range_6_left = matrix[knight_position_row + 2][knight_position_col + 1]
        if knight_range_6_left == "K":
            k_counter += 1
    if 0 <= knight_position_row + 2 <= rows - 1 and 0 <= knight_position_col - 1 <= rows - 1:
        knight_range_6_right = matrix[knight_position_row + 2][knight_position_col - 1]
        if knight_range_6_right == "K":
            k_counter += 1
    if 0 <= knight_position_row + 1 <= rows - 1 and 0 <= knight_position_col - 2 <= rows - 1:
        knight_range_9_left = matrix[knight_position_row + 1][knight_position_col - 2]
        if knight_range_9_left == "K":
            k_counter += 1
    if 0 <= knight_position_row - 1 <= rows - 1 and 0 <= knight_position_col - 2 <= rows - 1:
        knight_range_9_right = matrix[knight_position_row - 1][knight_position_col - 2]
        if knight_range_9_right == "K":
            k_counter += 1
    return k_counter


if rows >= 5:
    while True:
        max_Found = False
        for row in range(rows):
            for col in range(rows):
                if matrix[row][col] == "K":
                    result = check_func(row, col)
                    if result > max:
                        max = result
                        position = (row, col)
                        max_Found = True
        if max_Found:
            row, col = position
            matrix[row][col] = 0
            remove_counter += 1
        if max > 0:
            max = 0
        else:
            print(remove_counter)
            break

else:
    print("0")






