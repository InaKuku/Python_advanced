# 2 EXERCISE
# TUPLES AND SETS

# Write a program that reads a text from the console and counts the occurrences of each character in it. Print the
# results in alphabetical (lexicographical) order.

text = input()
count_dict = {}

text_tuple = tuple([v for v in text])

for a_letter in text_tuple:
    number = text_tuple.count(a_letter)
    if not a_letter in count_dict:
        count_dict[a_letter] = number

for key in sorted(count_dict):
    print(f"{key}: {count_dict[key]} time/s")

# example
# SoftUni rocks
