# 1 LAB
#LISTS AS STACKS AND QUEUES

# Write a program which keeps track of people who are getting water from a dispenser and the amount of water left
# at the end.
# On the first line you will receive the starting quantity of water in a dispenser. Then on the next few lines you will be
# given the names of some people who want to get water (each on separate line) until you receive the command
# &quot;Start&quot;. Add those people in a queue. Finally, you will receive some commands until the command &quot;End&quot;:
# - {liters} - Litters that the current person in the queue wants to get. Check if there is enough water in the
# dispenser for that person.
# o If there is enough water, print &quot;{person_name} got water&quot; and remove him/her from the
# queue.
# o Otherwise, print &quot;{person} must wait&quot; and remove the person from the queue without
# reducing the water in the dispenser.
#
# - refill {liters} - add the given litters in the dispenser.
# At the end print how many litters of water have left in the format: &quot;{left_liters} liters left&quot;.


from collections import deque

quantity = int(input())
command = input()

dict = deque()
while not command == "Start":
    dict.append(command)
    command = input()
else:
    while not command == "End":
        command = input()
        if command.isdigit():
            command = int(command)
            if quantity >= command:
                quantity -= command
                print(f"{dict.popleft()} got water")
            else:
                print(f"{dict.popleft()} must wait")
        elif 'refill' in command:
            quantity += int(command.split()[1])
    else:
        print(f"{quantity} liters left")

# example
# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End
