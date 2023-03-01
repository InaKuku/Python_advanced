# 1 LAB
#LISTS AS STACKS AND QUEUES

# Write a program which reads an input consisting of a name and adds it to a queue until "End" is received. If you
# receive "Paid", print every customer's name, and empty the queue. Otherwise, you will receive a client and you
# should add them to the queue. When you receive "End", you must print the count of the remaining people in the
# queue in the format: "{count} people remaining.".


from _collections import deque

name = input()
dict = deque()
while not name == "End":
   if name == "Paid":
       while len(dict) > 0:
           print(dict.popleft())
   else:
       dict.append(name)
   name = input()
else:
    print(f"{len(dict)} people remaining.")


# example:
# George
# Peter
# William
# Paid
# Michael
# Oscar
# Olivia
# Linda
# End