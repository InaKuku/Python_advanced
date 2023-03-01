# 4 LAB
# COMPREHENSION

# Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. Use
# nested comprehension for that problem.
# On the first line, you will receive the matrix sizes in format &quot;{rows}, {columns}&quot;. On the next rows, you will get
# elements for each column separated with a ", ".

rows = int(input())

matrix = [[int(v) for v in input(). split(", ") if int(v) % 2 == 0] for row in range(rows)]

print(matrix)

