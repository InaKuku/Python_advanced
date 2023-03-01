# 4 LAB
# COMPREHENSION

# Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For example,
# the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the matrix sizes in format &quot;{rows}, {columns}&quot;. On the next rows, you will get
# elements for each column separated with a ", ".

rows = int(input())

matrix = [[int(v) for v in input().split(", ")] for row in range(rows)]

flattened = [num for row in matrix for num in row]

print(flattened)