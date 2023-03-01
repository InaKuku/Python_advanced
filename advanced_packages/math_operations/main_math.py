from advanced_packages.math_operations.mapper import mapper

num1, operator, num2 = input().split()

num1 = float(num1)
num2 = float(num2)

print(mapper[operator](num1, num2) if mapper.get(operator) else "Invalid operator")

