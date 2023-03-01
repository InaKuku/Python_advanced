# 5 lab
# FUNCTIONS ADVANCED

# Write a function called operate that receives an operator (&quot;+&quot;, &quot;-&quot;, &quot;*&quot; or &quot;/&quot;) as first argument and
# multiple numbers (integers) as additional arguments (*args). The function should return the result of the operator
# applied to all the numbers. For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division

from functools import reduce

def operate(operator, *args):
    return reduce(lambda x, y: eval (f"{x} {operator} {y}"), args)

print(operate("*", 3, 4))
