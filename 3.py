
def math_operations(*args, **kwargs):
    turn = 0

    for num_index in range(len(args)):
        if turn == 0:
            kwargs["a"] += args[num_index]
            turn = 1
        elif turn == 1:
            kwargs["s"] -= args[num_index]
            turn = 2
        elif turn == 2:
            turn = 3
            try:
                kwargs["d"] = kwargs["d"] / args[num_index]
            except ZeroDivisionError:
                pass
        elif turn == 3:
            kwargs["m"] *= args[num_index]
            turn = 0
    return kwargs

print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))