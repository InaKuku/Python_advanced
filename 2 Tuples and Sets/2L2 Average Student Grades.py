# 2 LAB
# TUPLES AND SETS

# Write a program which reads names of students and their grades and adds them to the student record.
# On the first line you will receive the number of students – N. On the next N lines you will be receiving a student&#39;s
# name and his/ her grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point
# in the format: "{student's name} -> {grade1} {grade2} … {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

n = int(input())

dict_names = {}
val_formatted = []

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)
    if not name in dict_names:
        dict_names[name] = []
    dict_names[name].append(grade)

for key, value in dict_names.items():
    ave_value = sum(value)/len(value)
    for val in value:
        val = f'{val:.2f}'
        val_formatted.append(val)
    print(f"{key} -> {' '.join(str(v) for v in val_formatted)} (avg: {ave_value:.2f})")
    val_formatted = []

