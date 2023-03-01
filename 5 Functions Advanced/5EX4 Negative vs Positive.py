# 5 Exercise
# FUNCTIONS ADVANCED

# You will receive a sequence of numbers (integers), separated by a single space. Separate the negative numbers
# from the positive. Find the total sum of the negatives and positives, replace the negative number with its absolute
# value and print the following:
#
#  On the first line print the sum of the negatives
#  On the second line print the sum of the positives
#  On the third line:
# o If the absolute negative number is bigger than the positive number:
# "The negatives are stronger than the positives"
# o If the positive number is bigger than the absolute negative number:
# "The positives are stronger than the negatives"

data = [int(v) for v in input().split()]
negative = [v for v in data if v < 0]
absolute = [abs(v) for v in data if v < 0]
positive = [v for v in data if v >= 0]
print(sum(negative))
print(sum(positive))
if sum(absolute) > sum(positive):
    print("The negatives are stronger than the positives")
elif sum(positive) > sum(absolute):
    print("The positives are stronger than the negatives")