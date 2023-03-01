# 5 lab
# FUNCTIONS ADVANCED

# Write a function called multiply that can receive any amount of numbers (integers) as different parameters and
# returns the result of the multiplication of all of them. Submit only your function in the Judge system.

# def multiply(*args):
#     res = 1
#     for arg in args:
#         res *= arg
#     return res

from functools import reduce

def multiply(*args):
    return reduce(lambda x, y: x * y, args)

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))