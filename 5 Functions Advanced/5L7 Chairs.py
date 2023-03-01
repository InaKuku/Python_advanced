# 5 lab
# FUNCTIONS ADVANCED

# Write a program that receives names on the first line (separated by comma and space &quot;, &quot;) and number of chairs
# on the second line (an integer). Find all the ways to fit those people on the chairs. Print each combination on a
# separate line.
# Note: In the example below, &quot;Peter, George&quot; is same as &quot;George, Peter&quot;, so we only print the first combination

# from itertools import combinations
# comb_list = list(combinations(input().split(", "), int(input())))
# for x, y in comb_list:
#     print(x, y, sep=", ")

def combinations(names, count, current_names = []):
    if len(current_names) == count:
        print(", ".join(current_names))
        return

    for i in range(len(names)):
        current_names.append(names[i])
        combinations(names[i+1:], count, current_names)
        current_names.pop()

names = input().split(", ")
n = int(input())
combinations(names, n)
