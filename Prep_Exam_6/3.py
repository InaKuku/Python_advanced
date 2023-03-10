# Write function called best_list_pureness which will receive a list of numbers and a number K. You have to rotate the list K times (last becomes first) to find the variation of the list with the best pureness (pureness is calculated by summing all the elements in the list multiplied by their indices). For example, in the list [4, 3, 2, 6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26. At the end the function should return a string containing the highest pureness and the amount of rotations that were made to find this pureness in the following format: "Best pureness {pureness_value} after {count_rotations} rotations". If there is more than one highest pureness, take the first one.
# Note: Submit only the function in the judge system
# Input
# ⦁	There will be no input, just parameters passed to your function
# Output
# ⦁	There is no expected output
# ⦁	The function should return a string in the following format: "Best pureness {pureness_value} after {count_rotations} rotations"

from _collections import deque
from sys import maxsize

def best_list_pureness(*t):

    deq_nums = deque(t[0])
    num = t[1]

    max = - maxsize
    steps = 0
    max_step = 0
    value = 0

    for ind, val in enumerate(deq_nums):
        value += ind * val
    if value > max:
        max = value
        max_step = steps
    for _ in range(num):
        deq_nums.rotate(1)
        value = 0
        for ind, val in enumerate(deq_nums):
            value += ind*val
        steps += 1
        if value > max:
            max = value
            max_step =  steps
    return f"Best pureness {max} after {max_step} rotations"

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)




test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)