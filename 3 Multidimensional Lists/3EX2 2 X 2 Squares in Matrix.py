# 3 Exercise
# MULTIDIMENSIONAL LISTS

# Find the count of 2 x 2 squares with equal chars in a matrix.
# Input
#  On the first line, you will receive the matrix's dimensions in format "{row} {column}" - [1, 20]
#  On the next rows you will receive characters, separated by a single space
#
# © SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 2 of 8
#
# Output
#  Print the count of all square matrices you have found


rows, cols = [int(v) for v in input().split()]

matrix = []
counter = 0


for row in range(rows):
    matrix.append(input().split())

for row in range(rows - 1, 0, -1):
    for col in range(cols - 1, 0, - 1):
        if matrix[row][col] == matrix[row][col-1] and matrix[row][col-1] == matrix[row-1][col] and matrix[row-1][col] == matrix[row-1][col-1]:
            counter += 1

print(counter if counter > 0 else '0')

