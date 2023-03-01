# 4 EXERCISE
# COMPREHENSION

# Using a nested list comprehension, write a program that reads NxN matrix, finds its diagonals, prints them and their
# sum as shown below.

rows = int(input())

matrix = [[int(v) for v in input().split(", ")] for row in range(rows)]

first_diag = [matrix[row][row] for row in range(rows)]
sec_diag = [matrix[row][rows - row - 1] for row in range(rows)]

print(f"First diagonal: {', '.join(str(v) for v in first_diag)}. Sum: {sum(first_diag)}")
print(f"Second diagonal: {', '.join(str(v) for v in sec_diag)}. Sum: {sum(sec_diag)}")