# 5 Exercise
# FUNCTIONS ADVANCED

# Write a recursive function called palindrome() which will receive a word and an index (always 0). Implement the
# function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a
# palindrome" if the word is not a palindrome using recursion. Submit only the function in the judge system.

def palindrome(word, index, new_word = "", args_list = []):

    if len(word) == 1 or len(word) == 0:
        return f"{args_list[0]} is a palindrome"

    if word[index] == word[len(word) - 1]:
        new_word = word.replace(word[index], "")
        new_word = word.replace(word[len(word) - 1], "")
        args_list.append(word)

    else:
        return f"{args_list[0]} is not a palindrome"

    return palindrome(new_word, index)


print(palindrome("ratar", 0))
print(palindrome("rater", 0))
print(palindrome("examples", 0))