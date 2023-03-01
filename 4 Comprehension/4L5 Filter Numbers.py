# 4 LAB
# COMPREHENSION

# You will be given two lines of input - a start integer and an end integer. Print all the numbers in the given range
# (inclusive) that are divisible by any of the numbers from 2 to 10. Use comprehensions for this problem.

start = int(input())
end = int(input())

a_list = [num for num in range(start, end + 1) if [n for n in range(2, 11) if num % n == 0]]

print(list(set(a_list)))