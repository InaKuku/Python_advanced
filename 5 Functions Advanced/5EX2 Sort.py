# 5 Exercise
# FUNCTIONS ADVANCED

# Write a program that receives a sequence of numbers (integers), separated by a single space. It should print a sorted
# list of numbers in ascending order. Use sorted().

data = [int(v) for v in input().split()]
print(list(sorted(data)))