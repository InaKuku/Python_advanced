# Maria is opening a cupcake shop. Help her manage her inventory to improve stock availability.
#
# Write a function called stock_availability which receives:
# an inventory list of boxes with different kinds of cupcake flavours
# "delivery" or "sell" as second parameter
# there might or might not be any other parameters – numbers or strings at the end
#
# In case of "delivery"  to the shop was delivered new boxes with diferent kinds of cupcakes:
# You should add the boxes at the end of the inventory list
# There will be always at least one box delivered
# In case of "sell" Maria has a client and she is selling different boxes with cupcakes:
# If there is a number as another parameter, it means that Maria has sold that many boxes with cupcakes and you should remove them from the beginning of the inventory list
# If there is/are string/s as another parameter/s, it means that Maria has sold ALL cupcake boxes of the ordered flavour/s. Beware that not everything the buyer has ordered might be in stock, so you should check if the order is valid.
# If there are no other parameters, it means that Maria has sold only the first box of cupcakes and you should remove  it of the inventory list
# For more clarifications, see the examples below.
# Input
# There will be no input
# Parameters will be passed to your function
# Output
# The function should return a new inventory list
# All commands will be valid

from collections import deque

def stock_availability(inventory_list, act, *args):
    if act == "delivery":
        inventory_list.extend(args)
    elif act == "sell":
        if len(args) == 0:
            if len(inventory_list) > 0:
                del inventory_list[0]
        else:
            if isinstance(args[0], int):
                if len(inventory_list) >= args[0]:
                    del inventory_list[0:args[0]]
            elif isinstance(args[0], str):
                args_deq = deque(args)
                while len(args_deq) > 0:
                    if args_deq[0] in inventory_list:
                        inventory_list_copy = inventory_list.copy()
                        for i in inventory_list_copy:
                            if i == args_deq[0]:
                                inventory_list.remove(i)
                    args_deq.popleft()


    return inventory_list


print(stock_availability(["choco", "vanilla", "banana", "vanilla", "banana"], "sell", "vanilla", "banana"))
