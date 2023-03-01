# 2 LAB
# TUPLES AND SETS

# There is a party at SoftUni. Many guests are invited and there are two types of them: Regular and VIP. When a guest
# comes, check if he/she exists in any of the two reservation lists.
# All reservation codes are 8 characters long and all VIP numbers will start with a digit.
# On the first line you will receive the number of guests – N. On the next N lines you will be receiving their reservation
# codes. After that, you will be receiving guests, who came to the party, until you read the &quot;END&quot; command.
# In the end, print the number of the guests who did not come to the party and their reservation numbers. The VIP
# guests must be first.
# Both the VIP and the Regular guests must be sorted in ascending order.

n = int(input())
guests_nums = set()
guests_present = set()

for _ in range(n):
    guests_nums.add(input())
command = input()
while not command == "END":
    guests_present.add(command)
    command = input()
guests_not_present = guests_nums - guests_present
print(len(guests_not_present))
[print(guest) for guest in sorted(guests_not_present)]