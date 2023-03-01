# Write a function called list_manipulator which receives a list of numbers as first parameter and different amount of other parameters. The second parameter might be "add" or "remove". The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
# In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers and return the new list
# In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
# In case of "remove" and "beginning"
# If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
# If there are no other parameters, remove only the first element of the list.
# Finaly, return the new list
# In case of "remove" and "end"
# If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
# Otherwise if there are no other parameters, remove only the last element of the list.
# Finaly, return the new list
# For more clarifications, see the examples below.
# Input
# There will be no input
# Parameters will be passed to your function
# Output
# The function should return the new list of numbers


def list_manipulator(num_list, *args):

    is_Valid = True
    args_num_list = []

    if "add" in args:
        if isinstance(args[-1], int):
            for ind in range(len(args) - 1, -1, -1):
                if isinstance(args[ind], int):
                    args_num_list.append(args[ind])
            is_Valid = True
        else:
            is_Valid = False
        if "beginning" in args:
            if is_Valid:
                for arg_ind in range(0, len(args_num_list)):
                    num_list.insert(0, args_num_list[arg_ind])
        elif "end" in args:
            if is_Valid:
                num_list.extend(args_num_list[::-1])
        return num_list
    elif "remove" in args:
        if isinstance(args[-1], int):
            for ind in range(len(args) - 1, -1, -1):
                if isinstance(args[ind], int):
                    args_num_list.append(args[ind])
            is_Valid = True
        else:
            is_Valid = False
        if "beginning" in args:
            if is_Valid:
                if len(args_num_list) > 1:
                    num = sum(args_num_list)
                else:
                    num = args_num_list[0]
                num_list = num_list[num:]
            else:
                del num_list[0]
                is_Valid = True
        elif "end" in args:
            if is_Valid:
                if len(args_num_list) > 1:
                    num = sum(args_num_list)
                else:
                    num = args_num_list[0]
                num_list = num_list[:-num]
            else:
                del num_list[-1]
                is_Valid = True
        return num_list


    if not is_Valid:
        return num_list



print(list_manipulator([1,2,3,4,5,6,7,8,9,10,11,12,12,14,15], "remove", "end", 2, 3))