# 4 LAB
# COMPREHENSION

# Using a comprehension write a program that receives a text and removes all the vowels from it, case insensitive.
# Print the new text string after removing the vowels. The vowels that should be considered are "a", "o", "u", "e", "i".

data = list(input())
vowels_list = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]

new_string = [letter for letter in data if not letter in vowels_list]

print(''.join(new_string))


