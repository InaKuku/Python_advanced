# First you will be given a sequence of integers representing males. Afterwards you will be given another sequence of integers representing females.
# You have to start from the first female and try to match it with the last male.
# If their values are equal, you have to match them and remove both of them. Otherwise you should remove only the female and decrease the value of the male by 2.
# If someone’s value is equal to or below 0, you should remove him/her from the records before trying to match him/her with anybody.
# Special case - if someone’s value divisible by 25 without remainder, you should remove him/her and the next person of the same gender.
# You need to stop matching people when you have no more females or males.
# Input
# On the first line of input you will receive the integers, representing the males, separated by a single space.
# On the second line of input you will receive the integers, representing the females, separated by a single space.
# Output
# On the first line of output - print the number of successful matches:
# "Matches: {matchesCount}"
# On the second line - print all males left:
# If there are no males: "Males left: none"
# If there are males: "Males left: {maleN}, … , {male3}, {male2}, {male1}"
# On the third line - print all females left:
# If there are no females: "Females left: none"
# If there are females: "Females left: {female1}, {female2}, {female3},…, {femaleN}"
# Constraints
# All of the given numbers will be valid integers in the range [-100, 100].


from _collections import deque

males = [int(v) for v in input().split()]
females = [int(v) for v in input().split()]

fem_deq = deque(females)
match_counter = 0
is_Valid = False

def check_valid(fem, mal):

    global is_Valid

    if fem > 0 and mal > 0:
        is_Valid = True
        return is_Valid
    else:
        is_Valid = False
        return is_Valid


while len(males) > 0 and len(fem_deq) > 0:
    if check_valid(fem_deq[0], males[-1]):
        if fem_deq[0] % 25 == 0:
            fem_deq.popleft()
            if len(fem_deq) > 0:
                fem_deq.popleft()
                if len(fem_deq) == 0:
                    break
                else:
                    continue
            else:
                break
        if males[-1] % 25 == 0:
            males.pop()
            if len(males) > 0:
                males.pop()
                if len(males) == 0:
                    break
                else:
                    continue
            else:
                break

        if fem_deq[0] == males[-1]:
            match_counter += 1
            fem_deq.popleft()
            males.pop()
        else:
            fem_deq.popleft()
            males[-1] -= 2

    elif not is_Valid:
        if fem_deq[0] <= 0:
            fem_deq.popleft()
        else:
            males.pop()


print(f"Matches: {match_counter}")
if len(males) > 0:
    males = males[::-1]
    print(f"Males left: {', '.join([str(v) for v in males])}")
else:
    print("Males left: none")
if len(fem_deq) > 0:
    print(f"Females left: {', '.join([str(v) for v in fem_deq])}")
else:
    print("Females left: none")

