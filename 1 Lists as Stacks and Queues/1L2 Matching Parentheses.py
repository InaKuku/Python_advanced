# 1 LAB
# LISTS AS STACKS AND QUEUES

# You are given an algebraic expression with parentheses. Scan through the string and extract each set of
# parentheses.
# Print the result back on the console.

nums = input()
parentheses_indexes = []

for ind in range(0, len(nums)):
    if nums[ind] == "(":
        parentheses_indexes.append(ind)
    elif nums[ind] == ")":
        print(nums[parentheses_indexes.pop():ind + 1])

# example
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
