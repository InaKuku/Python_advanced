# 3 Lab
# MULTIDIMENSIONAL LISTS

# Write a program that finds the sum of matrix primary diagonal. On the first line, you will receive an integer N – the
# size of the square matrix. The next N lines holds the values for every row – N numbers, separated by a single space

n = int(input())

matrix = []
diagonal = 0

for row in range(n):
    matrix.append([int(v) for v in input().split()])
    diagonal += matrix[row][row]

print(diagonal)
