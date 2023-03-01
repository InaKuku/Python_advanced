# 4 EXERCISE
# COMPREHENSION

# Using a list comprehension, write a program that receives some text, separated by comma and space &quot;, &quot;, and
# prints on the console each string with its length in the following format:
#
# "{first_str} -> {first_str_len}, {second_str} -> {second_str_len},…"

print(', '.join([f"{a_word} -> {len(a_word)}" for a_word in input().split(", ")]))