# 1 EXERCISE
# LISTS AS STACKS AND QUEUES


# You have a fast food restaurant and most of the food that you&#39;re offering is previously prepared. You need to know
# if you will have enough food to serve lunch to all your customers.
# Write a program which checks the orders&#39; quantity. You also want to know who the client with the biggest order for
# that day is, because you want to give him a discount.
# First, you will be given the quantity of the food that you have for the day (an integer number). Next, you will be
# given a sequence of integers, each representing the quantity of an order. Keep the orders in a queue. Find the
# biggest order and print it. You will begin servicing your clients from the first one that came. Before each order,
# check if you have enough food left to complete it. If you have, remove the order from the queue and reduce the
# amount of food you have. If you succeeded in servicing all your clients, print: &quot;Orders complete&quot;. Otherwise,
# print: &quot;Orders left: {order1} {order2} .... {orderN}&quot;.
# Input
#  On the first line you will be given the quantity of your food - an integer in the range [0, 1000]
#  On the second line you will receive a sequence of integers, representing each order, separated by a single
# space
# Output
#  Print the quantity of biggest order
#  Print &quot;Orders complete&quot; if the orders are completed
#  If there are orders left, print them in the format given above
# Constraints
#  The input will always be valid

from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])
orders_full_list = orders.copy()
print(max(orders))
are_Completed = True



for an_order in orders_full_list:
    if food >= an_order:
        food -= an_order
        orders.popleft()
    else:
        print(f"Orders left:", end = " ")
        for i in range(0, len(orders)):
            print(f"{orders[i]}", end = " ")
        are_Completed = False
        break
if are_Completed:
    print("Orders complete")

#example:
# 499
# 57 45 62 70 33 90 88 76

