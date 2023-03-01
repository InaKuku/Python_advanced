# 4 LAB
# COMPREHENSION

# Write program that receives a list of characters separated by ", " and creates a dictionary with each character as a
# key and its ASCII value as a value. Try solving that problem using comprehensions.

letters = input().split(", ")

print ({letter: ord(letter) for letter in letters})
