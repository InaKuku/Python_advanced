matrix = []
movements = []
targets_list = []
targets_shot = []
is_Opened = True
are_Shot = False

for row in range(5):
    matrix.append(list(input().split(" ")))
for row in range(5):
    for col in range(5):
        if matrix[row][col] == "A":
            movements.append([row, col])
        elif matrix[row][col] == "x":
            targets_list.append([row, col])


def command_execution(com, row, col):
    global is_Opened
    global are_Shot

    if "move" in com:
        act, direction, steps = com.split(" ")
        steps = int(steps)

        if direction == "down":
            if row + steps < 5:
                for ro in range(row+1, row + steps+1):
                    if not matrix[ro][col] == ".":
                        is_Opened = False
                        break
                if is_Opened:
                    movements.append([row+steps, col])
                    matrix[row+steps][col] = "A"
                    matrix[row][col] = "."
        elif direction == "up":
            if row - steps >= 0:
                for ro in range(row-1, row-steps-1, -1):
                    if not matrix[ro][col] == ".":
                        is_Opened = False
                        break
                if is_Opened:
                    movements.append([row-steps, col])
                    matrix[row-steps][col] = "A"
                    matrix[row][col] = "."
        elif direction == "right":
            if col + steps < 5:
                for co in range(col + 1, col + steps+1):
                    if not matrix[row][co] == ".":
                        is_Opened = False
                        break
                if is_Opened:
                    movements.append([row, col + steps])
                    matrix[row][col+steps] = "A"
                    matrix[row][col] = "."
        elif direction == "left":
            if col - steps >= 0:
                for co in range(col - 1, col - steps -1, -1):
                    if not matrix[row][co] == ".":
                        is_Opened = False
                        break
                if is_Opened:
                    movements.append([row, col - steps])
                    matrix[row][col-steps] = "A"
                    matrix[row][col] = "."
        else:
            pass

    elif "shoot" in com:
        if "down" in com:
            if row + 1 < 5:
                for i in range(row+1, 5):
                    if matrix[i][col] == "x":
                        matrix[i][col] = "."
                        targets_shot.append([i, col])
                        targets_list.remove([i, col])
                        if len(targets_list) == 0:
                            are_Shot = True
                        break
        elif "up" in com:
            if row - 1 >= 0:
                for i in range(row-1, -1, -1):
                    if matrix[i][col] == "x":
                        matrix[i][col] = "."
                        targets_shot.append([i, col])
                        targets_list.remove([i, col])
                        if len(targets_list) == 0:
                            are_Shot = True
                        break
        elif "right" in com:
            if col + 1 < 5:
                for ico in range(col+1, 5):
                    if matrix[row][ico] == "x":
                        matrix[row][ico] = "."
                        targets_shot.append([row, ico])
                        targets_list.remove([row, ico])
                        if len(targets_list) == 0:
                            are_Shot = True
                        break
        elif "left" in com:
            if col - 1 >= 0:
                for ico in range(col-1, -1, -1):
                    if matrix[row][ico] == "x":
                        matrix[row][ico] = "."
                        targets_shot.append([row, ico])
                        targets_list.remove([row, ico])
                        if len(targets_list) == 0:
                            are_Shot = True
                        break

        else:
            pass

    else:
        pass

numbers_of_commands = int(input())
for num in range(numbers_of_commands):
    command = input()
    is_Opened = True
    command_execution(command, movements[-1][-2], movements[-1][-1])
    if are_Shot:
        break

if are_Shot:
    print(f"Training completed! All {len(targets_shot)} targets hit.")
else:
    print(f"Training not completed! {len(targets_list)} targets left.")

for i in range(len(targets_shot)):
    print(targets_shot[i])