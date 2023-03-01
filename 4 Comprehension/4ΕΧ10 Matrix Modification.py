# 4 EXERCISE
# COMPREHENSION

# Write a program that reads a matrix from the console. On the first line, you will get the matrix&#39;s rows. On next rows
# lines, you will get elements for each column, separated with space. You will be receiving commands in the following
# format:
#  Add {row} {col} {value} – Increase the number at the given coordinates with the value.
#  Subtract {row} {col} {value} – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print &quot;Invalid coordinates&quot;. A coordinate is valid if both of the given indexes
# are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.

rows = int(input())
matrix = [[int(v) for v in input().split()] for row in range(rows)]
command = input()

def check_func(matrix_row, matrix_col):
    if 0 <= matrix_row < rows and 0 <= matrix_col < rows:
        return True
    return False

while not command == "END":
    if "Add" in command:
        command_list = command.split()
        row, col, value = int(command_list[1]), int(command_list[2]), int(command_list[3])
        if check_func(row, col):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    if "Subtract" in command:
        command_list = command.split()
        row, col, value = int(command_list[1]), int(command_list[2]), int(command_list[3])
        if check_func(row, col):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    command = input()

else:
    for row in range(rows):
        print(*matrix[row])
