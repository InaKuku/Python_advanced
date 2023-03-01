# 2 EXERCISE
# TUPLES AND SETS

# You will receive a number N. On the next N lines, you will be receiving names. You must sum the ascii values of each
# letter in the name and integer divide it to the number of the current row (starting from 1). Save the result to a set
# of either odd or even numbers, depending on if the devised number is an odd or even. After that, sum the values of
# each set.
#  If the sums of the two sets are equal, print the union values, separated by ", ".
#  If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values,
# separated by ", ".
#  If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric different
# values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set

from math import floor

n = int(input())
odd_set = set()
even_set = set()
common_set = set()

for number_of_row in range(1, n + 1):
    name = input()
    ascii_num = 0
    for a_letter in name:
        ascii_num += ord(a_letter)
    name_num = floor(ascii_num / number_of_row)
    if name_num % 2 == 0:
        even_set.add(name_num)
    else:
        odd_set.add(name_num)
if sum(even_set) == sum(odd_set):
    common_set = odd_set | even_set
elif sum(even_set) < sum(odd_set):
    common_set = odd_set - even_set
elif sum(even_set) > sum(odd_set):
    common_set = odd_set ^ even_set
print(f"{', '.join([str(v) for v in common_set])}")