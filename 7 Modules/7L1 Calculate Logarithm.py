# 7 Lab
# Modules

# Write a program that prints the calculated logarithm of any given number
# Input
#  On the first line you will receive the number (an integer)
#  On the second line you will receive a number, which is the base of the logarithm. It can be either a number
# or the word &quot;natural&quot;
# The output should be formatted to the 2 nd decimal digit

from math import log

num = int(input())
base = input()

if base == "natural":
    print(f"{log(num):.2f}")
else:
    print(f"{log(num, int(base)):.2f}")