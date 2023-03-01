# 1 EXERCISE
# LISTS AS STACKS AND QUEUES

# On a circle road there are N petrol pumps. Petrol pumps are numbered 0 to (N−1) (both inclusive). For each petrol
# pump you will receive two pieces of information:
# - the amount of petrol that petrol pump will give
# - the distance from that petrol pump to the next petrol pump (kilometers)
#
# © SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 4 of 10
# Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps.
# Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at
# each of the petrol pumps. The truck will move one kilometer for each liter of the petrol.
# Input
#  On the first line you will receive the N-number petrol pumps
#  On the next N-lines you will receive the amount of petrol that petrol pump will give and the distance
# between that petrol pump and the next petrol pump, separated by single space
# Output
#  An integer which will be the smallest index of the petrol pump from which you can start the tour
# Constraints
#  1 ≤ N ≤ 1000001
#  1 ≤ Amount of petrol, Distance ≤ 1000000000

from collections import deque

number_pumps = int(input())
distance_list = deque()
petrol_list = deque()
counter_petrol = 0

for petrol_pump in range (0, number_pumps):
    command = [int(v) for v in input().split()]
    amount_of_petrol, distance = command[0], command[1]
    petrol_list.append(amount_of_petrol)
    distance_list.append(distance)

for pump_index in range (0, number_pumps):
    counter_petrol += petrol_list[pump_index]
    if counter_petrol >= distance_list[pump_index]:
        counter_petrol -= distance_list[pump_index]
        petrol_list_copy = petrol_list.copy()
        petrol_list_copy.rotate(-(pump_index + 1))
        distance_list_copy = distance_list.copy()
        distance_list_copy.rotate(-(pump_index + 1))
        for i in range (0, len(petrol_list) - 1):
            counter_petrol += petrol_list_copy[i]
            if counter_petrol >= distance_list_copy[i]:
                counter_petrol -= distance_list_copy[i]
            else:
                i -= 1
                counter_petrol = 0
                break
        if i == len(petrol_list) - 2:
            print(pump_index)
            break
    else:
        counter_petrol = 0

#example:
# 3
# 1 5
# 10 3
# 3 4