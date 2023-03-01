# 3 Exercise
# MULTIDIMENSIONAL LISTS

# Browsing through GitHub, you come across an old JS Basics teamwork game. It is about very nasty bunnies that
# multiply extremely fast. There&#39;s also a player that has to escape from their lair. You really like the game, so you
# decide to port it to Python because that&#39;s your language of choice. The last thing that is left is the algorithm that
#
# decides if the player will escape the lair or not.
#
# First, you will receive a line holding integers N and M, which represent the rows and columns in the lair. Then you
# receive N strings that can consists only of &quot;.&quot;, &quot;B&quot;, &quot;P&quot;. The bunnies are marked with &quot;B&quot;, the player is marked with
# &quot;P&quot;, and everything else is free space, marked with a dot &quot;.&quot;. They represent the initial state of the lair. There will be
#
# © SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 2 of 8
# only one player. Then you will receive a string with commands such as LLRRUUDD - where each letter represents
# the next move of the player (Left, Right, Up, Down).
# After every step, each of the bunnies spread to the up, down, left and right (neighboring cells marked as &quot;.&quot; changes
# their value to &quot;B&quot;). If the player moves to a bunny cell or a bunny reaches the player, the player has died. If the
# player goes out of the lair without encountering a bunny, the player has won.
# When the player dies or wins, the game ends. All the activities for this turn continue (e.g. all the bunnies spread
# normally), but there are no more turns. There will be no stalemates where the moves of the player end before he
# dies or escapes.
# Finally, print the final state of the lair with every row on a separate line. On the last line, print either &quot;dead: {row}
# {col}&quot; or &quot;won: {row} {col}&quot;. Row and col are the coordinates of the cell where the player has died or the
# last cell he has been in before escaping the lair.
# Input
#  On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
#  On the next N lines, each row is received in the form of a string. The string will contain only &quot;.&quot;, &quot;B&quot;, &quot;P&quot;. All
# strings will be the same length. There will be only one &quot;P&quot; for all the input
#  On the last line, the directions are received in the form of a string, containing &quot;R&quot;, &quot;L&quot;, &quot;U&quot;, &quot;D&quot;
# Output
#  On the first N lines, print the final state of the bunny lair
#  On the last line, print the outcome - &quot;won:&quot; or &quot;dead:&quot; + {row} {col}
# Constraints
#  The dimensions of the lair are in range [3…20]
#  The directions string length is in range [1…20]


rows, columns = [int(v) for v in input().split(" ")]


matrix = []
movements = []
bunnies = []
is_Done = False
is_Valid = True
is_Winner = True

for row in range(rows):
    matrix.append(list(input()))
for row in range(rows):
    for col in range(columns):
        if matrix[row][col] == "P":
            movements.append([row, col])
        elif matrix[row][col] == "B":
            bunnies.append([row, col])

def check_valid(r, c):
    global is_Valid

    if 0 <= r < rows:
        if 0 <= c < columns:
            is_Valid = True
            return is_Valid
        else:
            is_Valid = False
            return is_Valid
    else:
        is_Valid = False
        return is_Valid

def check_winner(r, c):
    global is_Winner

    if 0 <= r < rows:
        if 0 <= c < columns:
            is_Winner = False
            return is_Winner
        else:
            is_Winner = True
            return is_Winner
    else:
        is_Winner = True
        return is_Winner

def multiply_bunnies():
    global is_Done
    global is_Valid

    bunnies_copy = bunnies.copy()

    for position in bunnies_copy:
        ro, co = position[-2], position[-1]
        if check_valid(ro-1, co):
            if matrix[ro-1][co] == "P":
                matrix[ro - 1][co] = "B"
                is_Done = True
            elif matrix[ro-1][co] == ".":
                matrix[ro-1][co] = "B"
                bunnies.append([ro-1, co])

        if check_valid(ro+1, co):
            if matrix[ro+1][co] == "P":
                matrix[ro + 1][co] = "B"
                is_Done = True
            elif matrix[ro+1][co] == ".":
                matrix[ro+1][co] = "B"
                bunnies.append([ro+1, co])

        if check_valid(ro, co-1):
            if matrix[ro][co-1] == "P":
                matrix[ro][co - 1] = "B"
                is_Done = True
            elif matrix[ro][co-1] == ".":
                matrix[ro][co-1] = "B"
                bunnies.append([ro, co-1])

        if check_valid(ro, co+1):
            if matrix[ro][co+1] == "P":
                matrix[ro][co + 1] = "B"
                is_Done = True
            elif matrix[ro][co+1] == ".":
                matrix[ro][co+1] = "B"
                bunnies.append([ro, co+1])

    if is_Done:
        return is_Done


def execute_command(com, row, col):
    global is_Valid
    global bunnies_deq
    global is_Winner

    if com == "U":
        if not check_winner(row-1, col):
            if matrix[row-1][col]==".":
                matrix[movements[-1][-2]][movements[-1][-1]] = "."
                matrix[row-1][col] = "P"
                movements.append([row-1, col])
                multiply_bunnies()
            elif matrix[row - 1][col] == "B":
                multiply_bunnies()
                movements.append([row - 1, col])
                is_Done = True
                return is_Done
        else:
            is_Winner = True
            return is_Winner

    if com == "D":
        if not check_winner(row+1, col):
            if matrix[row+1][col]==".":
                matrix[movements[-1][-2]][movements[-1][-1]] = "."
                matrix[row+1][col] = "P"
                movements.append([row+1, col])
                multiply_bunnies()
            elif matrix[row + 1][col] == "B":
                multiply_bunnies()
                movements.append([row + 1, col])
                is_Done = True
                return is_Done
        else:
            is_Winner = True
            return is_Winner

    if com == "L":
        if not check_winner(row, col-1):
            if matrix[row][col-1]==".":
                matrix[movements[-1][-2]][movements[-1][-1]] = "."
                matrix[row][col-1] = "P"
                movements.append([row, col-1])
                multiply_bunnies()
            elif matrix[row][col-1] == "B":
                multiply_bunnies()
                movements.append([row, col - 1])
                is_Done = True
                return is_Done
        else:
            is_Winner = True
            return is_Winner

    if com == "R":
        if not check_winner(row, col + 1):
            if matrix[row][col + 1] == ".":
                matrix[movements[-1][-2]][movements[-1][-1]] = "."
                matrix[row][col + 1] = "P"
                movements.append([row, col + 1])
                multiply_bunnies()
            elif matrix[row][col + 1] == "B":
                multiply_bunnies()
                movements.append([row, col + 1])
                is_Done = True
                return is_Done
        else:
            is_Winner = True
            return is_Winner

    return is_Winner

commands = list(input())

for a_letter in commands:
    execute_command(a_letter, movements[-1][-2], movements[-1][1])
    if is_Winner:
        matrix[movements[-1][-2]][movements[-1][-1]] = "."
        multiply_bunnies()
        break
    elif is_Done:
        break

for row in range(rows):
    print(''.join(matrix[row]))
if is_Winner:
    print(f"won: {movements[-1][-2]} {movements[-1][-1]}")
elif is_Done:
    print(f"dead: {movements[-1][-2]} {movements[-1][-1]}")