# You will be given a chess board (8x8). On the board there will be 3 types of symbols:
# ⦁	"." – empty square
# ⦁	"Q" – a queen
# ⦁	"K" – the king
# Your job is to find which queens can capture the king and print them. The moves that the queen can do is to move diagonally, horizontally and vertically (basically all the moves that all the other figures can do except from the knight). Beware that there might be queens that stand in the way of other queens and can stop them from capturing the king. For more clarification see the examples.
# Input
# ⦁	8 lines – the state of the board (each square separated by single space)
# Output
# ⦁	The positions of the queens that can capture the king as lists
# ⦁	If the king cannot be captured, print: "The king is safe!"
# ⦁	The order of output does not matter
# Constrains
# ⦁	There will always be exactly 8 lines
# ⦁	There will always be exactly one King
# ⦁	Only the 3 symbols described above will be present in the input

matrix = []
capture_list = []


for row in range(8):
    matrix.append(list((input().split( ))))
for row in range(8):
    for col in range(8):
        if matrix[row][col] == "K":
            row_k = row
            col_k = col



def is_inside(r, c):
    global is_Valid
    if 0 <= r < 8:
        if 0 <= c < 8:
            is_Valid = True
            return is_Valid
        else:
            is_Valid = False
            return is_Valid
    else:
        is_Valid = False
        return is_Valid



for pos in range(col_k-1, -1, -1):
    if matrix[row_k][pos] == "Q":
        capture_list.append([row_k, pos])
        break
for pos in range(col_k+1, 8):
    if matrix[row_k][pos] == "Q":
        capture_list.append([row_k, pos])
        break

for ro in range(row_k-1, -1, -1):
    if matrix[ro][col_k] == "Q":
        capture_list.append([ro, col_k])
        break
for ro in range(row_k+1, 8):
    if matrix[ro][col_k] == "Q":
        capture_list.append([ro, col_k])
        break

turn = 0
for ro in range(row_k-1, -1, -1):
    turn += 1
    if is_inside(ro, col_k - turn):
        if matrix[ro][col_k - turn] == "Q":
            capture_list.append([ro, col_k - turn])
            break
turn = 0
for ro in range(row_k-1, -1, -1):
    turn += 1
    if is_inside(ro, col_k + turn):
        if matrix[ro][col_k + turn] == "Q":
            capture_list.append([ro, col_k + turn])
            break
turn = 0
for ro in range(row_k+1, 8):
    turn += 1
    if is_inside(ro, col_k - turn):
        if matrix[ro][col_k - turn] == "Q":
            capture_list.append([ro, col_k - turn])
            break
turn = 0
for ro in range(row_k+1, 8):
    turn += 1
    if is_inside(ro, col_k + turn):
        if matrix[ro][col_k + turn] == "Q":
            capture_list.append([ro, col_k + turn])
            break

if len(capture_list) > 0:
    for el in capture_list:
        print(el)
else:
    print("The king is safe!")



