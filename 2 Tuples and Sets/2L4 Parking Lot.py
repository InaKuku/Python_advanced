# 2 LAB
# TUPLES AND SETS

# Write a program that:
#  Records a car number for every car that enters the parking lot
#  Removes a car number when the car leaves the parking lot
# On the first line you will receive the number of commands - N. On the next N lines you will receive the direction and
# car&#39;s number in the format: &quot;{direction}, {car_number}&quot;. The direction could only be &quot;IN&quot; or &quot;OUT&quot;. Print
# the car numbers which are still in the parking lot. If the parking lot is empty print &quot;Parking Lot is Empty&quot;.
# NOTE: The order in which we print the result does not matter.

n = int(input())

cars = set()

for _ in range (n):
    act, car_number = input().split()
    if "IN" in act:
        cars.add(car_number)
    elif "OUT" in act:
        if car_number in cars:
            cars.remove(car_number)

if len(cars) == 0:
    print("Parking Lot is Empty")
else:
    [print(car) for car in cars]