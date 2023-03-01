# 1 EXERCISE
# LISTS AS STACKS AND QUEUES

# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is
# balanced. A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing
# parenthesis that occurs after the former. There will be no interval symbols between the parentheses. You will be
# given three types of parentheses: (, {, and [.
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
# Input
#  On a single line you will receive a sequence of parentheses.
# Output
#  For each test case, print on a new line &quot;YES&quot; if the parentheses are balanced.
# Otherwise, print &quot;NO&quot;. Do not print the quotes.
# Constraints
#  1 ≤ len s ≤ 1000, where len s is the length of the sequence.
#  Each character of the sequence will be one of {, }, (, ), [, ].

parenthesis = list(input())
parenthesis_copy = parenthesis.copy()
new_list = []
counter_deleted_indexes = 0

for parenth_index in range (0, len(parenthesis)):
    if parenthesis[parenth_index] == ")":
        if parenthesis_copy[parenth_index - 1 - counter_deleted_indexes] == "(":
            new_list.append(parenthesis[parenth_index])
            new_list.append(parenthesis[parenth_index - 1])
            parenthesis_copy.pop(parenth_index - counter_deleted_indexes)
            parenthesis_copy.pop(parenth_index - 1 - counter_deleted_indexes)
            counter_deleted_indexes += 2
    elif parenthesis[parenth_index] == "]":
        if parenthesis_copy[parenth_index - 1 - counter_deleted_indexes] == "[":
            new_list.append(parenthesis[parenth_index])
            new_list.append(parenthesis[parenth_index - 1])
            parenthesis_copy.pop(parenth_index - counter_deleted_indexes)
            parenthesis_copy.pop(parenth_index - 1 - counter_deleted_indexes)
            counter_deleted_indexes += 2
    elif parenthesis[parenth_index] == "}":
        if parenthesis_copy[parenth_index - 1 - counter_deleted_indexes] == "{":
            new_list.append(parenthesis[parenth_index])
            new_list.append(parenthesis[parenth_index - 1])
            parenthesis_copy.pop(parenth_index - counter_deleted_indexes)
            parenthesis_copy.pop(parenth_index - 1 - counter_deleted_indexes)
            counter_deleted_indexes += 2
if len(new_list) == len(parenthesis):
    print("YES")
else:
    print("NO")

# example:
# {[()]}
