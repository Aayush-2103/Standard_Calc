#calculator.py
from numbr import numbers_sort
from opratr import operators
from crretordr import order
from clcultion import calculation

def solve(expression):
    numbers = numbers_sort(expression)
    operator = operators(expression)
    correct_order = order(operator)
    answer = calculation(numbers, correct_order, operator)

    return answer