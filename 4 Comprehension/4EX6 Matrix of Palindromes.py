# 4 EXERCISE
# COMPREHENSION

# Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one
# in the examples below.
#  Rows define the first and the last letter: row 0  &#39;a&#39;, row 1  &#39;b&#39;, row 2  &#39;c&#39;, …
#  Columns + rows define the middle letter:
# o column 0, row 0  &#39;a&#39;, column 1, row 0  &#39;b&#39;, column 2, row 0  &#39;c&#39;, …
# o column 0, row 1  &#39;b&#39;, column 1, row 1  &#39;c&#39;, column 2, row 1  &#39;d&#39;, …
#
# Input
#  The numbers r and c stay at the first line at the input.
#  r and c are integers.

rows, cols = [int(v) for v in input().split()]

matrix = [[chr(row+97) + chr(col + 97) + chr(row+97) for col in range(row, cols + row)] for row in range (rows)]
print(*[' '.join(matrix[row]) for row in range(rows)], sep = "\n")

#matrix = []

# for row in range (rows):
#     matrix.append([])
#     for col in range (row, cols + row):
#         matrix[row].append(chr(row+97) + chr(col + 97) + chr(row+97))
# for row in range(rows):
#     print(' '.join(matrix[row]))
