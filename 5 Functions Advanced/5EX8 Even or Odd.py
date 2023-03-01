# 5 Exercise
# FUNCTIONS ADVANCED

# Create a function called even_odd() that can receive different amount of numbers and a command at the end.
# The command can be &quot;even&quot; or &quot;odd&quot;. Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.

def even_odd(*args):
    nums = [int(args[v]) for v in range(len(args) - 1)]
    if "odd" in args:
        return list(filter(lambda x: x % 2 == 1, nums))
    elif "even" in args:
        return list(filter(lambda x: x % 2 == 0, nums))

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))