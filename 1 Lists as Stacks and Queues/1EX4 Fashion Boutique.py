# 1 EXERCISE
# LISTS AS STACKS AND QUEUES

# You own a fashion boutique, and you receive a delivery of a huge box of clothes, represented as a sequence of
# integers. On the next line, you will be given an integer representing the capacity for one rack in your store.
# You must arrange the clothes in the store, and you use the racks to hang up every piece of clothing. You start from
# the last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for the purpose. Each
# piece of clothing has its value (an integer). You must sum their values, while you take them out of the box. If the
# sum becomes equal to the capacity of the current rack you must take a new one for the next clothes, if there are
# any left in the box. If the sum becomes greater than the capacity, do not hang the piece of clothing to the current
# rack. Take a new rack and then hang up the piece of clothing. In the end, print how many racks you have used to
# hang up the clothes.
# Input
#  On the first line you will be given a sequence of integers, representing the clothes in the box, separated by a
# single space.
#  On the second line, you will be given an integer, representing the capacity of a rack.
# Output
#  Print the number of racks, needed to hang up the clothes from the box.
# Constraints
#  The values of the clothes will be integers in the range [0,20]
#  There will never be more than 50 clothes in a box
#  The capacity will be an integer in the range [0,20]
#  None of the integers from the box will be greater than then the value of the capacity

clothes = [int(v) for v in input().split()]
capacity_of_rack = int(input())
clothes_full_stack = clothes.copy()
clothes_sum = 0
racks_counter = 1
for a_cloth_index in range (len(clothes_full_stack) - 1, -1, -1):
    clothes_sum +=  clothes_full_stack[a_cloth_index]
    if capacity_of_rack >= clothes_sum:
        clothes.pop()
    else:
        racks_counter += 1
        clothes_sum = clothes_full_stack[a_cloth_index]
        clothes.pop()
print(racks_counter)



