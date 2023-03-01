# 2 EXERCISE
# TUPLES AND SETS

# Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m, which
# represent the lengths of two separate sets. On the next n + m lines you will receive n numbers, which are the
# numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that appear in
# both and print them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -&gt; {3, 5}

n, m = [int(v) for v in input().split()]

numbers_1 = set()
numbers_2 = set()

for _ in range(n):
    numbers_1.add(input())
for _ in range(m):
    numbers_2.add(input())
common = numbers_1 & numbers_2
[print(common_number) for common_number in common]

#example:
# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5