# 6 Exercise
# File Handling

# Create a program that will receive commands until the command &quot;End&quot;. The commands can be:
#  &quot;Create-{file_name}&quot; - Creates the given file with an empty content. If the file already exists, remove
# the existing text in it (as if the file is created again)
#  &quot;Add-{file_name}-{content}&quot; - Append the content and a new line after it. If the file does not exist,
# create it, and add the content
#  &quot;Replace-{file_name}-{old_string}-{new_string}&quot; - Open the file and replace all the
# occurrences of the old string with the new string. If the file does not exist, print: &quot;An error occurred&quot;
#  &quot;Delete-{file_name}&quot; - Delete the file. If the file does not exist, print: &quot;An error occurred&quot;

import os

command = input()

while not command == "End":

    if "Create" in command:
        act, file_name = command.split("-")
        open(file_name, "w")

    elif "Add" in command:
        act, file_name, content = command.split("-")
        with open(file_name, "a") as out_file:
            out_file.write(content + "\n")

    elif "Replace" in command:
        act, file_name, old_str, new_str = command.split("-")
        try:
            with open(file_name, "r") as file:
                content = file.read()
            with open(file_name, "w") as file:
                content = content.replace(old_str, new_str)
                file.write(content)
        except FileNotFoundError:
            print("An error occurred")
            command = input()
            continue

    elif "Delete" in command:
        act, file_name = command.split("-")
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command = input()
