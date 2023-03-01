from _collections import deque

chocolates = [int(v) for v in input().split(", ")]
cups_of_milk = [int(v) for v in input().split(", ")]

milkshakes = 0
are_Done = False

milk_deq = deque(cups_of_milk)

while len(milk_deq) > 0 and len(chocolates) > 0:
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk_deq[0] <= 0:
        milk_deq.popleft()
        continue

    if milk_deq[0] == chocolates[-1]:
        milkshakes += 1
        milk_deq.popleft()
        chocolates.pop()
        if milkshakes == 5:
            are_Done = True
            break
    else:
        milk_deq.rotate(-1)
        chocolates[-1] -= 5

if are_Done:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if len(chocolates) > 0:
    print(f"Chocolate: {', '.join([str(v) for v in chocolates])}")
else:
    print("Chocolate: empty")
if len(milk_deq) > 0:
    print(f"Milk: {', '.join([str(v) for v in milk_deq])}")
else:
    print("Milk: empty")