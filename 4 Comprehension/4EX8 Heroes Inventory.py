# 4 EXERCISE
# COMPREHENSION

# Using a comprehension, write a program that receives a hero&#39;s names and items that need to be added in their
# inventory (item name and item cost). Print the total amount of items with their total cost for each hero.
# Input
#  On the first line, you will receive the names of the heroes separated by comma and space &quot;, &quot;
#  On the next lines until the command "End", you will be given items with their cost in the following format:
# &quot;{name}-{item}-{cost}&quot;. If an item already exists in the hero&#39;s inventory - ignore it.
# Output
#  For each hero, print his name, the total items and the total cost of the items in the format: "{name} -&gt;
# Items: {items_count}, Cost: {items_cost}"

names = input().split(", ")
command = input()

items_dict = {}
price_dict = {}

for name in names:
    items_dict[name] = []
    price_dict[name] = []

while not command == "End":
    name, item, price = command.split("-")
    for key, value in items_dict.items():
        if key == name:
            if not item in value:
                items_dict[name].append(item)
                price_dict[name].append(int(price)) #it can be float
    command = input()

print(*[f"{key} -> Items: {len(value)}, Cost: {sum(price_dict[key])}" for key, value in items_dict.items()], sep='\n')