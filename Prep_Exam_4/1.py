# Maria wants to make a firework show for the wedding of her best friend.
# We should help her to make the perfect firework show.
#
# First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another sequence of integers representing explosive power.
# You need to start from the first firework effect and try to mix it with the last explosive power. If the sum of their values is:
# divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
# divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
# divisible by both 3 and 5 – create Crossette firework and remove both materials
# Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix the same explosive power with the next firework effect.
# If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
# When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive power, you need to stop mixing.
# To make the perfect firework show, Maria needs 3 of each of the firework types.
# Input
# On the first line, you will receive the integers representing the firework effects, separated by ", ".
# On the second line, you will receive the integers representing the explosive power, separated by ", ".
# Output
# On the first line, print:
# if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
# if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
# On the second line, print all firework effects left if there are any:
# "Firework Effects left: {effect1}, {effect2}, (…)"
# On the third line, print all explosive fillings left if there are any:
# " Explosive Power left: {filling1}, {filling2}, (…)"
# Then, you need to print all fireworks and the amount you have of them:
# "Palm Fireworks: {count}"
# "Willow Fireworks: {count}"
# "Crossette Fireworks: {count}"
# Constraints
# All the given numbers will be integers in the range [-100, 100].
# There will be no cases with empty sequences.

from collections import deque

firework = deque([int(v) for v in input().split(", ")])
power = [int(v) for v in input().split(", ")]

palm_counter = 0
will_counter = 0
cross_counter = 0


while palm_counter < 3 or will_counter < 3 or cross_counter < 3:
    if len(firework) > 0 and len(power) > 0:
        if firework[0] > 0 and power[-1] > 0:
            fp_sum = firework[0] + power[-1]
            if fp_sum % 3 == 0 and not fp_sum % 5 == 0:
                palm_counter += 1
                firework.popleft()
                power.pop()
            elif fp_sum % 5 == 0 and not fp_sum % 3 == 0:
                will_counter += 1
                firework.popleft()
                power.pop()
            elif fp_sum % 5 == 0 and fp_sum % 3 == 0:
                cross_counter += 1
                firework.popleft()
                power.pop()
            else:
                firework[0] -= 1
                firework.append(firework[0])
                firework.popleft()

        else:
            if firework[0] <= 0:
                firework.popleft()
            if power[-1] <= 0:
                power.pop()
    else:
        if len(firework) == 0:
            print("Sorry. You can't make the perfect firework show.")
        elif len(power) == 0:
            print("Sorry. You can't make the perfect firework show.")
        if len(firework) > 0:
            firework = ', '.join(str(v) for v in firework)
            print(f"Firework Effects left: {firework}")
        if len(power) > 0:
            power = ', '.join(str(v) for v in power)
            print(f"Explosive Power left: {power}")
        print(f"Palm Fireworks: {palm_counter}")
        print(f"Willow Fireworks: {will_counter}")
        print(f"Crossette Fireworks: {cross_counter}")
        break
else:
    if palm_counter >= 3 and will_counter >= 3 and cross_counter >= 3:
        print("Congrats! You made the perfect firework show!")
        if len(firework) > 0:
            firework = ', '.join(str(v) for v in firework)
            print(f"Firework Effects left: {firework}")
        if len(power) > 0:
            power = ', '.join(str(v) for v in power)
            print(f"Explosive Power left: {power}")
        print(f"Palm Fireworks: {palm_counter}")
        print(f"Willow Fireworks: {will_counter}")
        print(f"Crossette Fireworks: {cross_counter}")


