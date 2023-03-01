# Ezio is still learning how to make bombs. With their help, he will save civilization. We should help Ezio to make his perfect bombs.
#
# You will be given two sequences of integers, representing bomb effects and bomb casings.
# You need to start from the first bomb effect and try to mix it with the last bomb casing. If the sum of their values is equal to any of the materials in the table below – create the bomb corresponding to the value and remove both bomb materials. Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.
# Bombs:
# Datura Bombs: 40
# Cherry Bombs: 60
# Smoke Decoy Bombs: 120
# To fill the bomb pouch, Ezio needs three of each of the bomb types.
# Input
# On the first line, you will receive the integers representing the bomb effects, separated by ", ".
# On the second line, you will receive the integers representing the bomb casings, separated by ", ".
# Output
# On the first line, print:
# if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
# if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
# On the second line, print all bomb effects left:
# If there are no bomb effects: "Bomb Effects: empty"
# If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
# On the third line, print all bomb casings left:
# If there are no bomb casings: "Bomb Casings: empty"
# If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
# Then, you need to print all bombs and the count you have of them, ordered alphabetically:
# "Cherry Bombs: {count}"
# "Datura Bombs: {count}"
# "Smoke Decoy Bombs: {count}"
# Constraints
# All of the given numbers will be valid integers in the range [0, 120].
# There will be no cases with negative material.


from _collections import deque


bomb_effects  = [int(v) for v in input().split(", ")]
bomb_casings = [int(v) for v in input().split(", ")]

bomb_deq = deque(bomb_effects)

is_Done = False
datura = 0
cherry = 0
smoke = 0

# Datura Bombs: 40
# Cherry Bombs: 60
# Smoke Decoy Bombs: 120

while len(bomb_deq) > 0 and len(bomb_casings) > 0:
    if bomb_deq[0] + bomb_casings[-1] == 40:
        datura += 1
        bomb_deq.popleft()
        bomb_casings.pop()
    elif bomb_deq[0] + bomb_casings[-1] == 60:
        cherry += 1
        bomb_deq.popleft()
        bomb_casings.pop()
    elif bomb_deq[0] + bomb_casings[-1] == 120:
        smoke += 1
        bomb_deq.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5
    if datura >= 3 and cherry >= 3 and smoke >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        is_Done = True
        break

if not is_Done:
    print("You don't have enough materials to fill the bomb pouch.")
if len(bomb_deq) > 0:
    print(f"Bomb Effects: {', '.join([str(v) for v in bomb_deq])}")
else:
    print("Bomb Effects: empty")
if len(bomb_casings) > 0:
    print(f"Bomb Casings: {', '.join([str(v) for v in bomb_casings])}")
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {cherry}")
print(f"Datura Bombs: {datura}")
print(f"Smoke Decoy Bombs: {smoke}")