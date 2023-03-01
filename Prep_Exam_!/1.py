# On the first line, you will receive a sequence of pizza orders. Each order contains a different number of pizzas, separated by comma and space ", ". On the second line, you will receive a sequence of employees with pizza-making capacities (how much pizzas an employee could make), separated by comma and space ", ".
# Your task is to check if all pizza orders are completed.
# To do that, you should take the first order and the last employee and see:
# If the number of pizzas in the order is less than or equal to the employee's pizza making capacity, the order is completed. Remove both the order and the employee.
# If the number of pizzas in the order is greater than the employee's pizza making capacity, the remaining pizzas from the order are going to be made by the next employees until the order is completed.
# If there are no more employees to finish the order, consider it not completed.
# The restaurant does not take orders for more than 10 pizzas at once.
# If an order is invalid (less than or equal to 0), you need to remove it before it is taken by an employee.
# You should keep track of the total pizzas that are being made.
# Input
# On the first line you will be given a sequence of pizza orders each represented as a number – integers separated by comma and space ", "
# On the second line you will be given a sequence of employees with pizza-making capacities – integers separated by comma and space ", "
# Output
# If all orders are successfully completed, print:
# All orders are successfully completed!
# Total pizzas made: {total count}
# Employees: {left employees joined by ", "}
# Otherwise, if you ran out of employees and there are still some orders left print:
# Not all orders are completed.
# Orders left: {left orders joined by ", "}
# Constraints
# You will always have at least one order and at least one employee
# All integers will be in range [-100, 100]

from collections import deque

orders = [int(v) for v in input().split(", ")]
employees = [int(v) for v in input().split(", ")]

order_deq = deque(orders)
pizza_counter = 0
out_of_Employees = False

for order in orders:
    if 1 <= order <= 10:
        if len(employees) > 0:
            if employees[len(employees) -1] >= order:
                pizza_counter += order
                order_deq.popleft()
                employees.pop()

            else:
                while order > 0:
                    if order >= employees[len(employees) - 1]:
                        pizza_counter += employees[len(employees) - 1]
                    else:
                        pizza_counter += order
                    order -= employees[len(employees) - 1]
                    employees.pop()
                    if len(employees) == 0:
                        out_of_Employees = True
                        if order > 0:                  #ако е нула
                            order_deq[0] = order

                        break
                else:
                    order_deq.popleft()

        else:
            out_of_Employees = True
    else:
        order_deq.popleft()

    if out_of_Employees:
        break


if out_of_Employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(v) for v in order_deq)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza_counter}")
    print(f"Employees: {', '.join(str(v) for v in employees)}")