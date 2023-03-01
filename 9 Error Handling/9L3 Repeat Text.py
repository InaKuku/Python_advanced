# 9 Lab
# ERROR HANDLING

# Write a program that receives text on the first line and times (to repeat the text) that must be an integer. If the user
# passes non-integer type for the times variable, handle the exception and print a message
# "Variable times must be an integer".

some_text = input()

try:
    times = int(input())
    print(times * some_text)
except ValueError:
    print("Variable times must be an integer")
