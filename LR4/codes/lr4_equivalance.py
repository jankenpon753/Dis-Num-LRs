import sympy

# Define symbolic variables
p, q = sympy.symbols("p q")

# Define your logical expressions. Here we enter the logical expressions we want to check equivalance of.
# Here for testing, De Morgan's theorem is used.
expr1 = ~(p & q)
expr2 = ~p | ~q

# Check for logical equivalence: Simplifying the logical expressions and then storing the boolean value in a variable.
equivalent = sympy.simplify_logic(expr1) == sympy.simplify_logic(expr2)
# From the previous statement, we get if the expressions are logically equivalant.
if equivalent:
    print("The expressions are logically equivalent.")
else:
    print("The expressions are not logically equivalent.")
