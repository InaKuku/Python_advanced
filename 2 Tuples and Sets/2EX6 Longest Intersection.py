# 2 EXERCISE
# TUPLES AND SETS

# Write a program that finds the longest intersection. You will be given a number N. On the next N lines you will be
# given two ranges in the format: &quot;{first start},{first end}-{second start},{second end}&quot;. Find the
# intersection of these two ranges and save the longest one of all N intersections. At the end print the numbers that
# are included in the longest intersection and its length in the format: &quot;Longest intersection is [{longest
# intersection}] with length {length longest intersection}&quot;
# Note: in each range, there will always be intersection. If there are two equal intersections, print the first one.

from sys import maxsize

n = int(input())

intersect_set = set()
longest_set = set()
max = -maxsize


for _ in range(n):
    intersect_input_1, intersect_input_2 = input().split("-")
    range1_start, range1_end = [int(v) for v  in intersect_input_1.split(",")]
    range2_start, range2_end = [int(v) for v in intersect_input_2.split(",")]
    set1 = set()
    set2 = set()

    for i in range(range1_start, range1_end + 1):
        set1.add(i)

    for j in range(range2_start, range2_end + 1):
        set2.add(j)

    intersect_set = set1 & set2
    if len(intersect_set) > max:
        max = len(intersect_set)
        longest_set = intersect_set

print(f"Longest intersection is {list(longest_set)} with length {max}")

# example:
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
