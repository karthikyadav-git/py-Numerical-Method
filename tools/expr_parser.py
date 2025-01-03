#! /bin/python3

from sympy import sympify

expr = input("Enter a mathematical expression: ")
parsed_expr = sympify(expr)
print(f"Parsed Expression: {parsed_expr}")
