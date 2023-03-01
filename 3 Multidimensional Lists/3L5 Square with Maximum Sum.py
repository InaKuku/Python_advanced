# 3 Lab
# MULTIDIMENSIONAL LISTS

# Write a program that reads a matrix from the console. On first line you will get matrix sizes in format "{rows},
# {columns}". On the next rows, you will get elements for each column separated with a ", ". Find the 2x2 top-
# left submatrix with biggest sum of its values. Print the matrix and the sum of its elements as shown in the examples.

from sys import maxsize

rows, columns = [int(v) for v in input().split(', ')]

matrix = []
max = - maxsize
position = None
result = 0

for i in range(rows):
    matrix.append([int(v) for v in input().split(", ")])

for row in range(rows - 1, -0, -1):
    for col in range(columns - 1, 0, -1):
       result = matrix[row][col] + matrix[row][col-1] + matrix[row-1][col] + matrix[row-1][col-1]
       if result >= max:
           max = result
           position = (row, col)

row, col = position
print(matrix[row-1][col-1], matrix[row-1][col])
print(matrix[row][col-1], matrix[row][col])
print(max)