


def numbers_searching(*args):
    args = list(args)
    args.sort()
    args_copy = args.copy()
    duplicates = []
    final_list = []
    missing_num = 0

    for indx in range(len(args)-1, -1, -1):
        if args[indx] == args[indx-1]:
            duplicates.append(args[indx])
            del args_copy[indx]

    duplicates = set(duplicates)
    duplicates_llst = list(duplicates)
    duplicates_llst.sort()

    turn = args_copy[0]
    for num_index in range(1, len(args_copy)):
        turn += 1
        if not args_copy[num_index] == turn:
            missing_num = turn
            turn += 1
    final_list.append(missing_num)
    final_list.append(duplicates_llst)
    return final_list




print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))