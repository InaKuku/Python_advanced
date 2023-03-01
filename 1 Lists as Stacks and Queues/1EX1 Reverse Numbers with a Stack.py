# 1 EXERCISE
# LISTS AS STACKS AND QUEUES

# Write a program that reads from the console a string with N integers, separated by a single space, and reverses
# them using a stack. Print the reversed integers on one line, separated by a single space.

num_list = input().split()
reversed_list = []

while len(num_list) > 0:
    reversed_list.append(num_list.pop())
print(f"{' '.join(reversed_list)}")

# 1 2 3 4 5