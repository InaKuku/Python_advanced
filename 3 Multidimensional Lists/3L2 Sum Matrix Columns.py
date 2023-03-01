# 3 Lab
# MULTIDIMENSIONAL LISTS

# Write a program that reads a matrix from the console and prints the sum for each column on separate lines. On the
# first line, you will get matrix sizes in format &quot;{rows}, {columns}&quot;. On the next rows, you will get elements for
# each column separated with a single space.

rows, columns = [int(v) for v in input().split(', ')]

matrix = []
result = 0

for i in range(rows):
    matrix.append([int(v) for v in input().split()])

for col in range(columns):
    for row in range(rows):
        result += matrix[row][col]
    print(result)
    result = 0
