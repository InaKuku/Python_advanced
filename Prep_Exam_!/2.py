# Two players bare-handedly throw small sharp-pointed missiles known as darts at a round target known as a dartboard. Who is going to win this game?
# You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
# 1	2	3	4	5	6	7
# 24	D	D	D	D	D	8
# 23	D	T	T	T	D	9
# 22	D	T	B	T	D	10
# 21	D	T	T	T	D	11
# 20	D	D	D	D	D	12
# 19	18	17	16	15	14	13
#
# Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player. The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero or less wins the game.
# You are going to receive the information for every throw on a separate line. The coordinate information of a hit will be in the format: "({row}, {column})".
# If a player hits outside the dartboard, he does not score any points.
# If a player hits a number, it is deducted from his total.
# If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted from his total.
# If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted from his total.
# "B" is the bullseye. If a player hits it, he wins the game, and the program ends.
# For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are deducted from his total.
# Your job is to find who won the game and with how many turns.
# Input
# The name of the first player and the name of the second player, separated by ", "
# 7 lines – the dartboard (separated by single space)
# On the next lines - the coordinates in the format: "({row}, {column})"
# Output
# You should print only one line containing the winner and his count of throws:
# "{name} won the game with {count_turns} throws!"
# Constrains
# There will always be exactly 7 lines
# There will always be a winner
# The points will be in range [1, 24]
# The coordinates will be in range [0, 100]


names = input().split(", ")

res_list = [501, 501]
matrix = []
turn_counter = 1
throw_counter_1 = 0
throw_counter_2 = 0
winner = ""
is_Found = False

for _ in range(7):
    matrix.append(input().split())

def check(rb):
    global is_Found
    global winner
    for res in rb:
        if res <= 0:
            winner = names[rb.index(res)]
            is_Found = True
            return winner

def result_normal(row, col):

    global turn_counter
    global is_Found
    global winner
    global throw_counter_1
    global throw_counter_2

    if not matrix[row][col] == "B":
        if turn_counter % 2 == 1:
            if matrix[row][col] == "D":
                res_list[0] -= 2 * (int(matrix[row][0]) + int(matrix[0][col]) + int(matrix[row][6]) + int(matrix[6][col]))
            elif matrix[row][col] == "T":
                res_list[0] -= 3 * (int(matrix[row][0]) + int(matrix[0][col]) + int(matrix[row][6]) + int(matrix[6][col]))
            turn_counter += 1
            throw_counter_1 += 1
        else:
            if matrix[row][col] == "D":
                res_list[1] -= 2 * (int(matrix[row][0]) + int(matrix[0][col]) + int(matrix[row][6]) + int(matrix[6][col]))
            elif matrix[row][col] == "T":
                res_list[1] -= 3 * (int(matrix[row][0]) + int(matrix[0][col]) + int(matrix[row][6]) + int(matrix[6][col]))
            turn_counter += 1
            throw_counter_2 += 1
    else:
        is_Found = True
        if turn_counter % 2 == 1:
            winner = names[0]
            throw_counter_1 += 1
        else:
            winner = names[1]
            throw_counter_2 += 1
        return winner
    return check(res_list)

def result_edges(a_row, a_col):

    global turn_counter
    global throw_counter_1
    global throw_counter_2

    if turn_counter % 2 == 1:
        res_list[0] -= int(matrix[a_row][a_col])
        turn_counter += 1
        throw_counter_1 += 1
    else:
        res_list[1] -= int(matrix[a_row][a_col])
        turn_counter += 1
        throw_counter_2 += 1
    return check(res_list)



while True:
    a = input()
    roandco = a.replace('(', "").replace(')', '')
    roandco = roandco.split(", ")
    row, col = [int(v) for v in roandco]
    if 0 <= row < 7:
        if 0 <= col < 7:
            if row == 0 or row == 6:
                result_edges(row, col)
            elif col == 0 or col == 6 and not row == 0 and not row == 6:
                result_edges(row, col)
            else:
                result_normal(row, col)
            if is_Found:
                break

        else:
            if turn_counter % 2 == 1:
                throw_counter_1 += 1
                turn_counter += 1
            else:
                throw_counter_2 += 1
                turn_counter += 1
    else:
        if turn_counter % 2 == 1:
            throw_counter_1 += 1
            turn_counter += 1
        else:
            throw_counter_2 += 1
            turn_counter += 1


if winner == names[0]:
    print(f"{winner} won the game with {throw_counter_1} throws!")
else:
    print(f"{winner} won the game with {throw_counter_2} throws!")
