# You will be given a string. Then, you will be given an integer N for the size of the field with square shape. On the next N lines, you will receive the rows of the field. The player will be placed on a random position, marked with "P". On random positions there will be letters. All of the empty positions will be marked with "-".
# Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it, concatеnates it to the initial string and the letter disappears from the field. If he tries to move outside of the field, he is punished - he loses the last letter in the string, if there are any, and the player’s position is not changed.
# At the end print all letters and the field.
# Input
# On the first line, you are given the initial string
# On the second line, you are given the integer N - the size of the square matrix
# The next N lines holds the values for every row
# On the next line you receive a number M
# On the next M lines you will get a move command
# Output
# On the first line the final state of the string
# In the end print the matrix
# Constraints
# The size of the square matrix will be between [2…10]
# The player position will be marked with "P"
# The letters on the field will be any letter except for "P"
# Move commands will be: "up", "down", "left", "right"

whole_str = input()
rows = int(input())

matrix = []
movements = []
p_Found = False

for row in range(rows):
    matrix.append(list(input()))
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "P":
            movements.append([row, col])
            matrix[row][col] = "-"
            p_Found = True
            break
    if p_Found:
        break

def check_valid(ro, co):

    global is_Valid

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

def commands_move(comm, row, col):

    global is_Valid
    global movements
    global whole_str

    if comm == "right":
        check_valid(row, col + 1)
        if is_Valid:
            if matrix[row][col + 1].isalpha():
                whole_str += matrix[row][col + 1]
                matrix[row][col + 1] = "-"
            movements.append([row, col + 1])
    elif comm == "left":
        check_valid(row, col - 1)
        if is_Valid:
            if matrix[row][col - 1].isalpha():
                whole_str += matrix[row][col - 1]
                matrix[row][col - 1] = "-"
            movements.append([row, col - 1])
    elif comm == "up":
        check_valid(row-1, col)
        if is_Valid:
            if matrix[row-1][col].isalpha():
                whole_str += matrix[row-1][col]
                matrix[row-1][col] = "-"
            movements.append([row -1, col])
    elif comm == "down":
        check_valid(row+1, col)
        if is_Valid:
            if matrix[row+1][col].isalpha():
                whole_str += matrix[row+1][col]
                matrix[row+1][col] = "-"
            movements.append([row+1, col])
    else:
        pass
    if not is_Valid:
        whole_str = whole_str[:-1]


turns = int(input())

for _ in range(turns):
    command = input()
    is_Valid = True
    commands_move(command, movements[-1][-2], movements[-1][-1])

print(whole_str)
matrix[movements[-1][-2]][movements[-1][-1]] = "P"
for row in range(rows):
    print(''.join(matrix[row]))