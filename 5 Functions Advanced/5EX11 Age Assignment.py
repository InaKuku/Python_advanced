# 5 Exercise
# FUNCTIONS ADVANCED

# Create a function called age_assignment that receives different number of names and then different number of
# key-value pairs. The key will be a single letter (first letter of a name), and the value a number (age). For each name,
#
# © SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 1 of 1
# find its first letter in the key-value pairs and assign the age to the person&#39;s name. At the end return a dictionary
# with all the names and ages as shown in the example. Submit only the function in the judge system.

def age_assignment(*args, **kwargs):
    names = []
    name_age_dict = {}
    for i in args:
        names.append(i)
    for key, value in kwargs.items():
        for name in names:
            name_in_letters = list(name)
            if name_in_letters[0] == key:
                name_age_dict[name] = value

    return name_age_dict



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))