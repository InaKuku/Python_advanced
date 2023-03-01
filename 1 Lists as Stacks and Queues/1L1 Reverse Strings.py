# 1 LAB
#LISTS AS STACKS AND QUEUES

# Write program that:
#  Reads an input string
#  Reverses it using a stack
#  Prints the result back on the console


str_input = list(input())
str_reversed = []

while len(str_input) > 0:
    str_reversed.append(str_input.pop())

print(f"{''.join(str_reversed)}")

#example:
# I Love Python
