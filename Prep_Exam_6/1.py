# You are hired to create a program that implements SJF (Shortest Job First). It works by letting the shortest jobs to take the CPU, so jobs won't get frozen.
# On the first line you will be given the jobs as integers (clock-cycles needed to finish the job) separated by comma and space ", ". On the second line you will be given the index of the job that we are interested in and want to know how many cycles will pass until the job is done.
# The tasks that need the least amount of clock-cycles will be completed first.
# For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
# You have to print how many clock-cycles will pass until the task you are interested in is completed. For more clarifications, see the examples below.
# Input
# ⦁	On the first line you will receive numbers separated by ", "
# ⦁	On the second line you will receive the index of the task you are interested in
# Output
# ⦁	Single line: the clock-cycles that will pass until the task you are interested in is finished

jobs = [int(v) for v in input().split(", ")]
indx = int(input())

my_dict = {}
counter = 0

for ind, val in enumerate(jobs):
    my_dict[ind] = val

sorted_dict = sorted(my_dict.items(), key=lambda kvp: (kvp[1], kvp [0]))
for key, val in sorted_dict:
    counter += val
    if key == indx:
        break
print(counter)