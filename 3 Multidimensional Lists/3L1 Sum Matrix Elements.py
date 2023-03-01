# 3 Lab
# MULTIDIMENSIONAL LISTS

# Write a program that reads a matrix from the console and prints:
#  The sum of all matrix elements
#  The matrix itself
# On the first line, you will receive the matrix sizes in format &quot;{rows}, {columns}&quot;. On the next rows, you will get
# elements for each column separated with a ", ".

rows, columns = [int(v) for v in input().split(', ')]

matrix = []
result = 0

for i in range(rows):
    matrix.append([int(v) for v in input().split(', ')])
    result += sum(matrix[i])

print(result)
print(matrix)

# example:


