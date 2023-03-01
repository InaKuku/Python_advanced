# 5 Exercise
# FUNCTIONS ADVANCED

# On the first line you will receive a command - "Odd" or "Even". On the second line you will receive a sequence of
# numbers (integers), separated by a single space.
#  If the command is "Odd", print the sum of the Odd numbers multiplied by the count of all numbers.
#  If the command is "Even", print the sum of the Even numbers multiplied by the count of all numbers.

command = input()
data = [int(v) for v in input().split()]

if command == "Odd":
    odd_nums = [v for v in data if v % 2 == 1]
    print(sum(odd_nums) * len(data))
elif command == "Even":
    even_nums = [v for v in data if v % 2 == 0]
    print(sum(even_nums) * len(data))