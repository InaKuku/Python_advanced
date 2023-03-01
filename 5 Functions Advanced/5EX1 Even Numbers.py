# 5 Exercise
# FUNCTIONS ADVANCED

# Write a program that receives a sequence of numbers (integers), separated by a single space. It should print a list of
# only the even numbers. Use filter().

data = [int(v) for v in input().split()]
print(list(filter(lambda x: x % 2 == 0, data)))