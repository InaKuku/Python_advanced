# 4 EXERCISE
# COMPREHENSION

# Write a program to flatten several lists of numbers, received in the following format:
#  String with numbers or empty strings separated by "|".
#  Values are separated by spaces (&#39; &#39;, one or several)
#  Order the output list from the last to the first received, and their values from left to right as shown below.

# str_input = input()
#
# # str_new = str_input.replace(" ", "")
# str_new = str_input.strip()
# str_list = str_new.split("|")
# str_list_rev = str_list[::-1]
#
# new_list = []
#
# for i_ind in range(0, len(str_list_rev)):
#     str_list_rev[i_ind] = str_list_rev[i_ind].strip()
#     for ind, letter in enumerate(str_list_rev[i_ind]):
#         if letter.isdigit():
#             if str_list_rev[i_ind][ind+1]:
#                 next_leter = str_list_rev[i_ind][ind+1]
#                 if next_leter.isdigit():
#
#
# transformed_str = ' '.join(str_list_rev)
#
# print(transformed_str)

sequence = input().split("|")

numbers = [[int(el) for el in seq.split()] for seq in sequence]

numbers.reverse()

numbers = [number for sequence in numbers for number in sequence]

print(' '.join([str(x) for x in numbers]))


