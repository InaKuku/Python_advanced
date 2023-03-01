# code by Yavor Lulchev - for debugging

def fill_dictionary():
    numbers_dictionary ={}
    while True:
        key = input()
        if key == "Search":
            break
        value = input()
        if value == "Search":
            break
        number = int(value)
        numbers_dictionary[key] = number
    return numbers_dictionary

def find_in_store(store):
    searched = input()

    while searched != "Remove":
        print(numbers_dictionary.get(searched, "Number does not exist in dictionary"))
        searched = input()

def remove_from_store(numbers_dictionary):
    line = input()
    while line != "End":
        searched = line
        if searched in numbers_dictionary:
            del numbers_dictionary[searched]
        else:
            print("Number does not exist in dictionary")
            line = input()
            continue
        print(numbers_dictionary)
        line = input()

numbers_dictionary = fill_dictionary()
find_in_store(numbers_dictionary)
remove_from_store(numbers_dictionary)