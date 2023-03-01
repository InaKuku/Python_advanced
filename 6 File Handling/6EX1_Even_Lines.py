# 6 Exercise
# File Handling

# Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before you
# print the result replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

import re

with open ("text.txt") as file:
    content = file.readlines()
    for line_numb in range(0, len(content)):
        if line_numb % 2 == 0:
            a_line = content[line_numb]
            a_line = re.sub('[-,.!?]', "@", a_line)
            a_line = a_line.split()
            a_line = a_line[::-1]
            a_line = " ".join(a_line)
            print(a_line)











# Longer code

# import re
#
# with open ("text.txt") as file:
#     content = file.readlines()
#     pattern = r"\-|\,|\.|\!|\?"
#     for line_numb in range(0, len(content)):
#         if line_numb % 2 == 0:
#             a_line = content[line_numb]
#             punct = re.finditer(pattern, a_line)
#             punct = [p.group(0) for p in punct]
#             for i in punct:
#                 a_line = a_line.replace(i, "@")
#             a_line = a_line.split()
#             a_line = a_line[::-1]
#             a_line = " ".join(a_line)
#             print(a_line)

