# 3 Lab
# MULTIDIMENSIONAL LISTS

# Write a program that reads a number - N, representing the rows and columns of a matrix. On the next N lines, you
# will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol. Find the
# first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". You should
# start searching from the top left. If there is no such symbol print an error message "{symbol} does not occur
# in the matrix"

rows = int(input())

matrix = []
is_Found = False

for row in range(rows):
    matrix.append([v for v in list(input())])

symbol = input()

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == symbol:
            mtr = (row, col)
            is_Found = True
            break
    if is_Found:
        break
print(mtr if is_Found else f"{symbol} does not occur in the matrix")


