# 3 Exercise
# MULTIDIMENSIONAL LISTS

# You are tasked to visualize a snake&#39;s zigzag path in a rectangular matrix with size N x M.
# The snake is represented by a string. It starts moving from the top-left corner to the right. When the snake reaches
# the end of the row, it slithers its way down to the next row and turns left. The moves are repeated to the very end.
# The first cell is filled with the first symbol of the snake, the second cell is filled with the second symbol, etc. The
# snake is as long as it takes to fill the path completely - if you reach the end of the string representing the snake,
# start again at the first symbol. After you fill the matrix with the snake&#39;s path, you should print it.
# Input
# The input data consists of exactly two lines:
#  On the first line, you will receive the dimensions N x M of the field in format: &quot;{rows} {columns}&quot;.
#  On the second line you will receive the string representing the snake
# Output
#  You should print the snake&#39;s zigzag path of size N x M (rows x columns)
#
# © SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 2 of 8
#
# Constraints
#  The dimensions N and M of the matrix will be integers in the range [1 … 12]
#  The snake will be a string with length in the range [1 … 20] and will not contain any whitespace
# characters

from math import ceil

rows, cols = [int(v) for v in input().split()]
data = list(input())

matrix = []
counter = 0

if rows * cols > len(data):
    data = (ceil((rows * cols) / len(data))) * data

for row in range(rows):
    matrix.append([])
    for col in range (cols):
        matrix[row].append(data[counter])
        counter += 1

for row in range (rows):
    if row % 2 == 1:
        matrix[row] = matrix[row][::-1]

for i in range(rows):
    print(f"{''.join(matrix[i])}")
