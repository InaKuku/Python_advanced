# Everybody remembers the old snake game. Now it is time to create your own.
#
# You will be given an integer n for the size of the snake territory with square shape. On the next n lines, you will receive the rows of the territory. The snake will be placed on a random position, marked with the letter 'S'. On random positions there will be food, marked with '*'. There might also be a lair on the territory. The lair has two burrows. They are marked with the letter - 'B'. All of the empty positions will be marked with '-'.
# Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
# Move commands will be: "up", "down", "left", "right".
# If the snake moves to a food, it eats the food and increases the food quantity with one.
# If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear. If the snake goes out of its territory, it loses, can't return back and the program ends. The snake needs at least 10 food quantity to win.
# When the snake has gone outside of its territory or has eaten enough food, the game ends.
# Input
# On the first line, you are given the integer n – the size of the square matrix.
# The next n lines holds the values for every row.
# On each of the next lines you will get a move command.
# Output
# On the first line:
# If the snake goes out of its territory, print: "Game over!"
# If the snake eat enough food, print: "You won! You fed the snake."
# On the second line print all food eaten: "Food eaten: {food quantity}"
# In the end print the matrix.
# Constraints
# The size of the square matrix will be between [2…10].
# There will always be 0 or 2 burrows, marked with - 'B'.
# The snake position will be marked with 'S'.
# The snake will always either go outside its territory or eat enough food.
# There will be no case in which the snake will go through itself.


rows =int(input())

matrix = []
movements =[]
b = []
is_Valid = True
food_quantity = 0

for row in range(rows):
    matrix.append(list(input()))
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "S":
            movements.append([row, col])
            matrix[row][col] = "."
        if matrix[row][col] == "B":
            b.append([row, col])

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


def eat_func(com, row, col):
    global food_quantity

    if com == "up":
        if check_valid(row-1, col):
            if matrix[row-1][col] =="*":
                food_quantity += 1
                matrix[row - 1][col] = "."
                movements.append([row-1, col])
            elif matrix[row-1][col] =="B":
                matrix[row - 1][col] = "."
                b.remove([row-1, col])
                movements.append(b[0])
                matrix[b[0][0]][b[0][1]] = "."
            else:
                movements.append([row - 1, col])
                matrix[row - 1][col] = "."
    elif com == "down":
        if check_valid(row+1, col):
            if matrix[row+1][col] =="*":
                food_quantity += 1
                matrix[row + 1][col] = "."
                movements.append([row + 1, col])
            elif matrix[row+1][col] =="B":
                matrix[row + 1][col] = "."
                b.remove([row+1, col])
                movements.append(b[0])
                matrix[b[0][0]][b[0][1]] = "."
            else:
                movements.append([row + 1, col])
                matrix[row + 1][col] = "."
    elif com == "left":
        if check_valid(row, col-1):
            if matrix[row][col-1] =="*":
                food_quantity += 1
                matrix[row][col-1] = "."
                movements.append([row, col-1])
            elif matrix[row][col-1] =="B":
                matrix[row][col-1] = "."
                b.remove([row, col-1])
                movements.append(b[0])
                matrix[b[0][0]][b[0][1]] = "."
            else:
                movements.append([row, col-1])
                matrix[row][col - 1] = "."
    elif com == "right":
        if check_valid(row, col+1):
            if matrix[row][col+1] =="*":
                food_quantity += 1
                matrix[row][col+1] = "."
                movements.append([row, col+1])
            elif matrix[row][col+1] =="B":
                matrix[row][col+1] = "."
                b.remove([row, col+1])
                movements.append(b[0])
                matrix[b[0][0]][b[0][1]] = "."
            else:
                movements.append([row, col + 1])
                matrix[row][col + 1] = "."
    if not is_Valid:
        return is_Valid

    return food_quantity




while food_quantity < 10:
    command = input()
    eat_func(command, movements[-1][-2], movements[-1][-1])
    if not is_Valid:
        print("Game over!")
        break
if is_Valid:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_quantity}")
if is_Valid:
    matrix[movements[-1][-2]][movements[-1][-1]] = "S"
for row in range(rows):
    print(f"{''.join(matrix[row])}")