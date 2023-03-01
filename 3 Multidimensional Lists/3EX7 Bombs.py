# 3 Exercise
# MULTIDIMENSIONAL LISTS

# You will be given a square matrix of integers, each integer separated by a single space, and each row on a new line.
# Then on the last line of input you will receive indexes - coordinates to several cells separated by a single space, in
# the following format: row1,column1 row2,column2 row3,column3…
# On those cells there are bombs. You must detonate every bomb, in the order they were given. When a bomb
# explodes, it deals damage equal to its own integer value, to all the cells around it (in every direction and in all
# diagonals). One bomb can&#39;t explode more than once and after it does, its value becomes 0. When a cell&#39;s value
# reaches 0 or below, it dies. Dead cells can&#39;t explode.
# You must print the count of all alive cells and their sum. Afterwards, print the matrix with all its cells (including the
# dead ones).
# Input
#  On the first line, you are given the integer N - the size of the square matrix.
#  The next N lines holds the values for every row - N numbers separated by a space.
#  On the last line, you will receive the coordinates of the cells with the bombs in the format described
# above.
# Output
#  On the first line, you need to print the count of all alive cells in the format:
# &quot;Alive cells: {aliveCells}&quot;
#  On the second line, you need to print the sum of all alive cell in the format:
# &quot;Sum: {sumOfCells}&quot;
#  In the end print the matrix. The cells must be separated by a single space.
#
# Constraints
#  The size of the matrix will be between [0…1000].
#  The bomb coordinates will always be in the matrix.
#  The bomb&#39;s values will always be greater than 0.
#  The integers of the matrix will be in range [1…10000].

rows = int(input())


matrix = []
bomb_list = []
is_Valid = True
is_Bomb = False
life_counter = 0
all_life = 0

for row in range(rows):
    matrix.append([int(v) for v in input().split( )])

def check_valid(ro, co):
    if 0 <= ro < rows:
        if 0 <= co < rows:
            is_Valid = True
            return is_Valid
        else:
            is_Valid = False
            return is_Valid
    else:
        is_Valid = False
        return is_Valid


def bomb_explosion(power, row, col):
    global is_Bomb

    if check_valid(row-1, col):
        if matrix[row-1][col] > 0:
            matrix[row-1][col] -= power
    if check_valid(row-1, col+1):
        if matrix[row-1][col+1] > 0:
            matrix[row-1][col+1] -= power
    if check_valid(row, col+1):
        if matrix[row][col+1] > 0:
            matrix[row][col+1] -= power
    if check_valid(row+1, col+1):
        if matrix[row+1][col+1] > 0:
            matrix[row+1][col+1] -= power
    if check_valid(row+1, col):
        if matrix[row+1][col] > 0:
            matrix[row+1][col] -= power
    if check_valid(row+1, col-1):
        if matrix[row+1][col-1] > 0:
            matrix[row+1][col-1] -= power
    if check_valid(row, col-1):
        if matrix[row][col-1] > 0:
            matrix[row][col-1] -= power
    if check_valid(row-1, col-1):
        if matrix[row-1][col-1] > 0:
            matrix[row-1][col-1] -= power

line =input().split(" ")

for i_ind in range(len(line)):
    i_list = [int(v) for v in line[i_ind].split(",")]
    if i_list not in bomb_list:
        bomb_list.append(i_list)

for bomb_ind in range(len(bomb_list)):
    bomb_power = matrix[bomb_list[bomb_ind][-2]][bomb_list[bomb_ind][-1]]
    if bomb_power > 0:
        matrix[bomb_list[bomb_ind][-2]][bomb_list[bomb_ind][-1]] = 0
        bomb_explosion(bomb_power, bomb_list[bomb_ind][-2], bomb_list[bomb_ind][-1])

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] > 0:
            life_counter += 1
            all_life += matrix[row][col]

print(f"Alive cells: {life_counter}")
print(f"Sum: {all_life}")
for row in range(rows):
    print(' '.join(str(v) for v in matrix[row]))


