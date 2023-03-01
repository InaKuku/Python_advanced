# 4 EXERCISE
# COMPREHENSION

# Using a list comprehension, write a program that receives numbers, separated by comma and space &quot;, &quot;, and
# prints all the positive, negative, even and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number

num_list = [int(v) for v in input().split(", ")]

print(f"Positive: {', '.join([str(d) for d in num_list if d >= 0])}")
print(f"Negative: {', '.join([str(d) for d in num_list if d < 0])}")
print(f"Even: {', '.join([str(d) for d in num_list if d % 2 == 0])}")
print(f"Odd: {', '.join([str(d) for d in num_list if d % 2 == 1])}")