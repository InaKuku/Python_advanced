# You are playing a game and your goal is to collect 100 coins.
#
# On the first line, you will be given a number representing the size of the field with square shape. On the next few lines, you will be given a field with:
# One player randomly placed in it and marked with symbol "P"
# Numbers for coins placed at different positions of the field
# Walls marked with "X".
# After the field state, you will be given commands for the players movement. Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it.
# If the player goes out of the field or he hits a wall, he loses the game and his coins are reduced to 50% and rounded down to the next-lowest number. The program ends.
# Otherwise, the player has to collect at least 100 coins to win the game.
# For more clarifications see the examples below.
# Input
# Number representing the size of the field (matrix NxN)
# Matrix representing the field (each position separated by single space)
# On each of the next lines you will get a move command.
# Output
# If the player won the game, print: "You won! You've collected {total_coins} coins."
# If the player loses the game, print: "Game over! You've collected {total_coins} coins."
# Collected coins have to be rounded down to the next-lowest number.
# The field positions from which the player has collected coins as lists:
# "Your path:
# [{row_position1}{column_position1}]
# [{row_position2}{column_position2}]
# [{row_position3}{column_position3}]
# …"
# Constrains
# There will be no case in which in the field will be less than 100 coins.
# All of the given numbers will be valid integers in the range [0, 100].

from math import floor

rows =int(input())

coins = 0
matrix = []
movements =[]
movements_with_p_movements =[]
p_Found = False
p_Found_Again = False
is_Valid = True


for row in range(rows):
    matrix.append(input().split())
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "P":
            movements_with_p_movements.append([row, col])
            p_Found = True
            break
    if p_Found:
        break

def check_valid(ro, co):

    global is_Valid
    global p_Found_Again

    if 0 <= ro < rows:
        if 0 <= co < rows:
            if matrix[ro][co] == "X":
                is_Valid = False
                return is_Valid
            elif matrix[ro][co] == "P":
                p_Found_Again = True
                return p_Found_Again
            else:
                is_Valid = True
                return is_Valid
        else:
            is_Valid = False
            return is_Valid
    else:
            is_Valid = False
            return is_Valid


def commands_move(comm, row, col):

    global coins
    global is_Valid
    global movements
    global movements_with_p_movements
    global p_Found_Again

    if comm == "right":
        check_valid(row, col + 1)
        if is_Valid and not p_Found_Again:
            coins += int(matrix[row][col + 1])
            movements.append([row, col + 1])
            movements_with_p_movements.append([row, col + 1])
        elif is_Valid and p_Found_Again:
            movements_with_p_movements.append([row, col + 1])
            return p_Found_Again
    elif comm == "left":
        check_valid(row, col - 1)
        if is_Valid and not p_Found_Again:
            coins += int(matrix[row][col - 1])
            movements.append([row, col - 1])
            movements_with_p_movements.append([row, col - 1])
        elif is_Valid and p_Found_Again:
            movements_with_p_movements.append([row, col - 1])
            return p_Found_Again
    elif comm == "up":
        check_valid(row - 1, col)
        if is_Valid and not p_Found_Again:
            coins += int(matrix[row - 1][col])
            movements.append([row - 1, col])
            movements_with_p_movements.append([row - 1, col])
        elif is_Valid and p_Found_Again:
            movements_with_p_movements.append([row - 1, col])
            return p_Found_Again
    elif comm == "down":
        check_valid(row + 1, col)
        if is_Valid and not p_Found_Again:
            coins += int(matrix[row + 1][col])
            movements.append([row + 1, col])
            movements_with_p_movements.append([row + 1, col])
        elif is_Valid and p_Found_Again:
            movements_with_p_movements.append([row + 1, col])
            return p_Found_Again

    else:
        pass
    if is_Valid == False:
        return is_Valid


while True:
    command = input()
    commands_move(command, movements_with_p_movements[-1][-2], movements_with_p_movements[-1][-1])
    if is_Valid and not p_Found_Again:
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            print("Your path: ")
            for i_ind in range(0, len(movements)):
                print(movements[i_ind])
            break
    if not is_Valid:
        print(f"Game over! You've collected {floor(coins / 2)} coins.")
        print("Your path: ")
        for i_ind in range(0, len(movements)):
            print(movements[i_ind])
        break
    if p_Found_Again:
        p_Found_Again = False
