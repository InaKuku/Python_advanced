# 3 Exercise
# MULTIDIMENSIONAL LISTS

# Write a program that reads a matrix, from the console and perform certain operations with its elements. User input
# is provided in a similar way like in the problems above - first you read the dimensions and then the data.
# Your program should receive commands in format: &quot;swap {row1} {col1} {row2} {col2}&quot; where row1, row2,
# col1, col2 are coordinates in the matrix. A valid command starts with the "swap" keyword along with four valid
# coordinates (no more, no less).
#  If the command is valid, you should swap the values at the given indexes and print the matrix at each step
# (thus you will be able to check if the operation was performed correctly).
#  If the command is not valid (does not contain the keyword &quot;swap&quot;, has fewer or more coordinates entered
# or the given coordinates do not exist), print &quot;Invalid input!&quot; and move on to the next command.
# Your program should finish when the string "END" is entered.

rows, cols = [int(v) for v in input().split()]

matrix = []

for row in range(rows):
    matrix.append(input().split())

command = input()

while not command == "END":
    command = command.split()
    matrix_coord = []
    is_Valid = True
    if len(command) == 5:
        matrix_coord = [int(command[v]) for v in range(1, len(command))]
        if not 0 <= matrix_coord[0] <= rows - 1:
            is_Valid = False
        if not 0 <= matrix_coord[2] <= rows - 1:
            is_Valid = False
        if not 0 <= matrix_coord[1] <= cols - 1:
            is_Valid = False
        if not 0 <= matrix_coord[3] <= cols - 1:
            is_Valid = False
    else:
        is_Valid = False
    if not command[0] == 'swap':
        is_Valid = False


    if not is_Valid:
        print("Invalid input!")
    else:
        initial_row = matrix_coord[0]
        initial_col = matrix_coord[1]
        swap_row = matrix_coord[2]
        swap_col = matrix_coord[3]
        initial_values = matrix[initial_row][initial_col]
        matrix[initial_row][initial_col] = matrix[swap_row][swap_col]
        matrix[swap_row][swap_col] = initial_values
        for row in range(0, rows):
            print(*matrix[row])
    command = input()

