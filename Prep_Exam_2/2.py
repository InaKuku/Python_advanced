
rows = int(input())
bombs_num = int(input())

matrix = []
is_Valid = True

for _ in range(rows):
    matrix.append([0 for el in range(rows)])



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



def count_bombs(ro, co):
    counter = 0

    if check_valid(ro-1, co):
        if matrix[ro-1][co] == "*":
            counter += 1
    if check_valid(ro-1, co+1):
        if matrix[ro-1][co+1] == "*":
            counter += 1
    if check_valid(ro, co+1):
        if matrix[ro][co+1] == "*":
            counter += 1
    if check_valid(ro+1, co+1):
        if matrix[ro+1][co+1] == "*":
            counter += 1
    if check_valid(ro+1, co):
        if matrix[ro+1][co] == "*":
            counter += 1
    if check_valid(ro+1, co-1):
        if matrix[ro+1][co-1] == "*":
            counter += 1
    if check_valid(ro, co-1):
        if matrix[ro][co-1] == "*":
            counter += 1
    if check_valid(ro-1, co-1):
        if matrix[ro-1][co-1] == "*":
            counter += 1
    return counter


for _ in range(bombs_num):
    bomb = input()
    bo = bomb.replace("(", "").replace(")", "")
    bomb = bo.split(", ")
    bomb = [int(v) for v in bomb]
    bombrow, bombcol = bomb
    if check_valid(bombrow, bombcol):
        if matrix[bombrow][bombcol] == 0:
            matrix[bombrow][bombcol] = "*"

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == 0:
            matrix[row][col] = count_bombs(row, col)

for row in range(rows):
    print(*matrix[row])