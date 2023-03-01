# 1 EXERCISE
# LISTS AS STACKS AND QUEUES

# Somewhere in the future, there is a robotics factory. The current project is assembly line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is
# free it should take a product for processing and log his name, product and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each second (so
# the first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot
# to take it, it should be queued at the end of the line again.
# The robots are standing on the line in the order of their appearance.
# Input
#  On the first line, you will receive the names of the robots and their processing times in the format
# &quot;robotName-processTime;robotName-processTime;robotName-processTime...&quot;
#  On the second line, you will get the starting time in format &quot;hh:mm:ss&quot;
#  Next, until the &quot;End&quot; command, you will get a product on each line.
# Output
#  Every time a robot takes a product, you should print: &quot;{robotName} - {product} [hh:mm:ss]&quot;

from _collections import deque

str_rob = input().split(";")
start_time = input()
command = input()
product_list = []
while not command == "End":
    product_list.append(command)
    command = input()

start_time_list = []
robots_list = []
processing_list = []
robots_start_time_list = []
available_robots = deque()
product_list_copy = product_list.copy()
product_list_copy = deque(product_list_copy)
plus_a_second = 0

def convert_into_second(hours_and_minutes_and_seconds):
    h, m, s = [int(i) for i in hours_and_minutes_and_seconds.split(':')]

    return 3600 * h + 60 * m + s


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d:%02d" % (hour, minutes, seconds)

start_time_in_seconds = convert_into_second (start_time)

if len(str_rob) <= len(product_list):
    for i_index in range (0, len(str_rob)):
        robot, processing_time = str_rob[i_index].split("-")
        processing_time = int(processing_time)
        robots_list.append(robot)
        processing_list.append(processing_time)
        robots_start_time = start_time_in_seconds + 1 + i_index
        robots_start_time_list.append(robots_start_time)
        print(f"{robot} - {product_list[i_index]} [{convert(robots_start_time)}]")
        product_list_copy.popleft()
    if len(str_rob) < len(product_list):
        plus_a_second = robots_start_time
        for time_index in range (0, len(robots_start_time_list)):
            robots_start_time_list[time_index] += processing_list[time_index]
        while len(product_list_copy) > 0:
            plus_a_second += 1
            if plus_a_second > robots_start_time + 1:
                product_list_copy.rotate(-1)
            for in_index in range(0, len(robots_start_time_list)):
                if robots_start_time_list[in_index] == plus_a_second:
                    duplicate = plus_a_second
                    available_robots.append(robots_list[in_index])
            for lai_index in range(0, len(available_robots)):
                print(f"{available_robots[lai_index]} - {product_list_copy[0]} [{convert(duplicate + lai_index)}]")
                product_list_copy.popleft()
                robots_start_time_list[robots_list.index(available_robots[lai_index])] += processing_list[robots_list.index(available_robots[lai_index])] + lai_index
                plus_a_second += 1

else:
    for i_index in range (0, len(product_list)):
        robot, processing_time = str_rob[i_index].split("-")
        robots_list.append(robot)
        processing_list.append(processing_time)
        robots_start_time = start_time_in_seconds + 1 + i_index
        print(f"{robot} - {product_list[i_index]} [{convert(robots_start_time)}]")

