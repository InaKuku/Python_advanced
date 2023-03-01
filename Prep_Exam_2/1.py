from _collections import deque

customers = [int(v) for v in input().split(", ")]
drivers = [int(v) for v in input().split(", ")]

customers_deq = deque(customers)
total_time = 0

while len(customers_deq) > 0 and len(drivers) > 0:
    if customers_deq[0] <= drivers[-1]:
        total_time += customers_deq[0]
        customers_deq.popleft()
        drivers.pop()
    else:
        drivers.pop()

else:
    if len(customers_deq) == 0:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time} minutes")
    else:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join([str(v) for v in customers_deq])}")