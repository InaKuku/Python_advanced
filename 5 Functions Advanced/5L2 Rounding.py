# 5 lab
# FUNCTIONS ADVANCED

# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use
# round().

#print([round(float(v)) for v in input().split()])

nums = [float(v) for v in input().split()]
rounded = map(round(), nums)
print(list(rounded))