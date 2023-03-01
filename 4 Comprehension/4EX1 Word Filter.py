# 4 EXERCISE
# COMPREHENSION

# Using a comprehension, write a program that receives some text, separated by space, and take only those words,
# whose length is even. Print each word on a new line.

str_list = input().split()

even_len_list = [a_word for a_word in str_list if len(a_word) % 2 == 0]

for a in even_len_list:
    print(a)
