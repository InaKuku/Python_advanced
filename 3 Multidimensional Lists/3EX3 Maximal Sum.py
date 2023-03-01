from sys import maxsize

rows, columns = [int(v) for v in input().split()]

matrix = []
max = - maxsize
position = None
result = 0

for i in range(rows):
    matrix.append([int(v) for v in input().split()])

for row in range(rows - 1, 1, -1):
    for col in range(columns - 1, 1, -1):
       result = matrix[row][col] + matrix[row][col-1] + matrix[row][col-2] + matrix[row-1][col] + matrix[row-1][col-1] + matrix[row-1][col-2] + matrix[row-2][col] + matrix[row-2][col-1] + + matrix[row-2][col-2]
       if result >= max:
           max = result
           position = (row, col)

row, col = position
print(f"Sum = {max}")
print(matrix[row-2][col-2], matrix[row-2][col-1], matrix[row-2][col])
print(matrix[row-1][col-2], matrix[row-1][col-1], matrix[row-1][col])
print(matrix[row][col-2], matrix[row][col-1], matrix[row][col])
