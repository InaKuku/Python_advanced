# 5 lab
# FUNCTIONS ADVANCED

# Write a program that generates all the possible expressions and their results between a given list of numbers
# (integers) using only the + and - operators. Print them on the console as shown in the example.

def expression(nums, currrent_result = 0, current_expression = ""):
    if not nums:
        print(f"{current_expression}={currrent_result}")
        return
    expression(nums[1:], currrent_result + nums[0], f"{current_expression}+{nums[0]}")
    expression(nums[1:], currrent_result - nums[0], f"{current_expression}-{nums[0]}")

nums = [int(el) for el in input().split(", ")]
expression(nums)