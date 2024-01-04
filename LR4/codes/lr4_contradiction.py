import sympy
from itertools import product
from sympy.logic.boolalg import truth_table
from sympy.abc import x, y

p, q = sympy.symbols("p q")

# Defining logical expressions
expr = ~(p | ~p)

table = truth_table(expr, [p, p])
contradiction = True
for t in table:
    # printing the truth table
    print("{0} -> {1}".format(*t))
    if t[1] == True:
        contradiction = False
        break

if contradiction:
    print("The statement is a contradiction.")
else:
    print("The statement is not a contradiction.")
