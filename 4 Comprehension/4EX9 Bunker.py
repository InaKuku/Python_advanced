# 4 EXERCISE
# COMPREHENSION

# Using a comprehension, write a program that finds the number of given items in a bunker and their average
# quality.
# On the first line, you will be given all item categories present in the bunker, then you will be given a number (n). On
# the next &quot;n&quot; lines, you will be given different items in the following format:
# &quot;{category} - {item_name} - quantity:{item_quantity};quality:{item_quality}&quot;
#
# © SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 5 of 5
# Store that information, you will need it later. After you receive all the inputs, print the total amount of items (sum
# the quantities) in the format:
#
# &quot;Count of items: {count}&quot;
#
# After that, print the average quality of all items in the following format, formatted to the second digit:
#
# &quot;Average quality: {quality sum/categories count}&quot;
#
# Finally, print all categories with the items on separate lines in the format:
# &quot;{category} -&gt; {item1}, {item2}, …&quot;.

categories = input().split(", ")
n = int(input())

cat_dict = {a_category: {} for a_category in categories}
quality_counter = 0
quantity_counter = 0

for _ in range(n):
    a_category, item, others = input().split(" - ")
    quantity, quality = others.split(";")
    quantity, quantity_value = quantity.split(":")
    quantity_value = int(quantity_value)
    quality, quality_value = quality.split(":")
    quality_value = int(quality_value)
    for key, value in cat_dict.items():
        if key == a_category:
            if not value:
                cat_dict[a_category] = {item: {quantity: 0, quality: 0}}
            else:
                for k, val in value.items():
                    if not item in k:
                        cat_dict[a_category].update({item: {quantity: 0, quality: 0}})
                        break
            cat_dict[a_category][item][quantity] += quantity_value
            cat_dict[a_category][item][quality] += quality_value
            quality_counter += quality_value
            quantity_counter += quantity_value
            break
print(f"Count of items: {quantity_counter}")
print(f"Average quality: {quality_counter/len(categories):.2f}")
for key, values in cat_dict.items():
    key_list = []
    for k, val in values.items():
        key_list.append(k)
    print(f"{key} -> {', '.join(key_list)}")