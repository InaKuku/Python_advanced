# 5 Exercise
# FUNCTIONS ADVANCED

# Write a function called concatenate() that receives some strings, concatenates them, and returns the result.

def concatenate(*args):
    res = ""
    for v in args:
        res += v
    return res

print(concatenate("Soft", "Uni", "Is", "Great", "!"))