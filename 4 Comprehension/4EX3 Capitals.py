# 4 EXERCISE
# COMPREHENSION

# Using a dictionary comprehension, write a program which receives country names on the first line, separated by
# comma and space &quot;, &quot;, and their corresponding capital cities on the second line (again separated by comma and
# space &quot;, &quot;). Print each country with their capital on a separate line in the following format:
#
# &quot;{country} -&gt; {capital}&quot;
#
# Hints
#  You can use the zip() function to zip the two lists into tuple pairs.

countries = input().split(", ")
capitals = input().split(", ")

my_dict = {countries[c_index]: capitals[c_index] for c_index in range (len(countries))}

print(*[f"{key} -> {value}" for key, value in my_dict.items()], sep = "\n")

