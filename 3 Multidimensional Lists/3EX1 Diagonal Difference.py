# 3 Exercise
# MULTIDIMENSIONAL LISTS

# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).

rows = int(input())

matrix = []
d1 = 0
d2 = 0

for row in range(rows):
    matrix.append([int(v) for v in input().split()])

    d1 += matrix[row][row]
    d2 += matrix[row][rows - row - 1]

print(abs(d1 - d2))