# 3 Exercise
# MULTIDIMENSIONAL LISTS

# We receive the size of the field in which our miner moves. The field is always a square. After that, we will receive
# the commands, which represent the directions, in which the miner should move. The miner starts from position - &#39;s&#39;.
# The commands will be: left, right, up and down. If the miner has reached the edge of the field and the next
# command indicates that he has to get out of the field, he must remain on his current possition and ignore the
# current command. The possible characters that may appear on the screen are:
#  * - a regular position on the field.
#  e - the end of the route.
#  c - coal
#  s - the place where the miner starts
# When the miner finds a coal, he collects it and replaces it with &#39;*&#39;. Keep track of the count of the collected
# coals. If the miner collects all of the coals in the field, the program stops and you have to print the following
# message: &quot;You collected all coals! ({rowIndex}, {colIndex})&quot;.
# If the miner steps at &#39;e&#39;, the game is over (the program stops) and you have to print the following message:
# &quot;Game over! ({rowIndex}, {colIndex})&quot;.
# If there are no more commands and none of the above cases had happened, you have to print the following
# message: &quot;{remainingCoals} coals left. ({rowIndex}, {colIndex})&quot;.
# Input
#  Field size - an integer number.
#  Commands to move the miner - an array of strings separated by &quot; &quot;.
#  The field: some of the following characters (*, e, c, s), separated by whitespace (&quot; &quot;);
# Output
#  There are three types of output:
# o If all the coals have been collected, print the following output: &quot;You collected all coals!
# ({rowIndex}, {colIndex})&quot;
# o If you have reached the end, you have to stop moving and print the following line: &quot;Game over!
# ({rowIndex}, {colIndex})&quot;
# o If there are no more commands and none of the above cases had happened, you have to print the
# following message: &quot;{totalCoals} coals left. ({rowIndex}, {colIndex})&quot;
#
# Constraints
#  The field size will be a 32-bit integer in the range [0 … 2 147 483 647].
#  The field will always have only one &#39;s&#39;.
#  Allowed working time for your program: 0.1 seconds.
#  Allowed memory: 16 MB.

rows = int(input())
commands_list = input().split(" ")

matrix = []
movements = []
coal_list = []
coal_counter = 0
is_Valid = True
coal_Taken = False
is_e = False

for row in range(rows):
    matrix.append(list((input().split( ))))
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "s":
            movements.append([row, col])
        elif matrix[row][col] == "c":
            coal_list.append([row, col])

def check_valid(r, c):
    global is_Valid

    if 0 <= r < rows:
        if 0 <= c < rows:
            is_Valid = True
            return is_Valid
        else:
            is_Valid = False
            return is_Valid
    else:
        is_Valid = False
        return is_Valid


def command_execute(com, row, col):
    global coal_counter
    global coal_Taken
    global is_e

    if com == "up":
        if check_valid(row-1, col):
            movements.append([row-1, col])
            if matrix[row-1][col] == "c":
                matrix[row - 1][col] = "*"
                coal_counter += 1
                coal_list.remove([row-1, col])
                if len(coal_list) == 0:
                    coal_Taken = True
                    return coal_Taken
            elif matrix[row-1][col] == "e":
                is_e = True
                return is_e
    elif com == "down":
        if check_valid(row+1, col):
            movements.append([row+1, col])
            if matrix[row+1][col] == "c":
                matrix[row + 1][col] = "*"
                coal_counter += 1
                coal_list.remove([row+1, col])
                if len(coal_list) == 0:
                    coal_Taken = True
                    return coal_Taken
            elif matrix[row+1][col] == "e":
                is_e = True
                return is_e
    elif com == "left":
        if check_valid(row, col-1):
            movements.append([row, col-1])
            if matrix[row][col-1] == "c":
                matrix[row][col-1] = "*"
                coal_counter += 1
                coal_list.remove([row, col-1])
                if len(coal_list) == 0:
                    coal_Taken = True
                    return coal_Taken
            elif matrix[row][col-1] == "e":
                is_e = True
                return is_e
    elif com == "right":
        if check_valid(row, col+1):
            movements.append([row, col+1])
            if matrix[row][col+1] == "c":
                matrix[row][col+1] = "*"
                coal_counter += 1
                coal_list.remove([row, col+1])
                if len(coal_list) == 0:
                    coal_Taken = True
                    return coal_Taken
            elif matrix[row][col+1] == "e":
                is_e = True
                return is_e

for command in commands_list:
    command_execute(command, movements[-1][-2], movements[-1][-1])
    if coal_Taken:
        print(f"You collected all coals! ({movements[-1][-2]}, {movements[-1][-1]})")
        break
    if is_e:
        print(f"Game over! ({movements[-1][-2]}, {movements[-1][-1]})")
        break
if not coal_Taken and not is_e:
    print(f"{len(coal_list)} coals left. ({movements[-1][-2]}, {movements[-1][-1]})")
