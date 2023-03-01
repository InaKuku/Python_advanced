# 1 EXERCISE
# LISTS AS STACKS AND QUEUES

# You have an empty sequence. You will receive an integer – N. On the next N lines you will receive queries. Each
# query is one of these four types:
# "1 x" – Push the element x into the stack.
# "2" – Delete the element at the top of the stack.
# "3" – Print the maximum element in the stack.
# "4" – Print the minimum element in the stack.
# After you go through all the queries, print the stack from the top to the bottom in the following format:
# "{n}, {n 1 }, {n 2 } …, {n n }"
# Constraints
#  It is guaranteed that each query is valid
#  1 ≤ N ≤ 105
#  1 ≤ x ≤ 109
#  1 ≤ type ≤ 4

number_of_commands = int(input())
nums_stack = []

for a_command in range(0, number_of_commands):
    actual_command = input()
    if "1" in actual_command:
        actual_command = actual_command.split()
        number = int(actual_command[1])
        nums_stack.append(number)
    elif "2" in actual_command:
        if len(nums_stack) > 0:
            nums_stack.pop()
    elif "3" in actual_command:
        if len(nums_stack) > 0:
            print(max(nums_stack))
    elif "4" in actual_command:
        if len(nums_stack) > 0:
            print(min(nums_stack))
nums_stack = nums_stack[::-1]
print(f"{', '.join(str(v) for v in (nums_stack))}")

#example:
# 10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4


