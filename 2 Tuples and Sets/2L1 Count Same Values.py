# 2 LAB
# TUPLES AND SETS

# You will be given numbers separated by a space. Write a program which prints the number of occurrences of each
# number in the format "{number} - {count} times".

numbers = tuple([float(v) for v in input().split()])
count_dict = {}

for num in numbers:
    num_count = numbers.count(num)
    count_dict[num] = num_count

for key in count_dict.items():
    print(f"{key[0]} - {key[1]} times")

# example
# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
