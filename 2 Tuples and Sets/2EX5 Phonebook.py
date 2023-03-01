# 2 EXERCISE
# TUPLES AND SETS

# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a &quot;-&quot;. If you receive a name that already
# exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of a
# contact by name and print its details in format "{name} -> {number}". In case the contact isn't found, print
# "Contact {name} does not exist."

command = input()

phone_dict = {}

while not command.isdigit():
    name, phone = command.split("-")
    phone_dict[name] = phone
    command = input()
else:
    command = int(command)
    for _ in range(command):
        command = input()
        if command in phone_dict:
            print(f"{command} -> {phone_dict[command]}")
        else:
            print(f"Contact {command} does not exist.")

# example:
# Adam-0888080808
# 2
# Mery
# Adam