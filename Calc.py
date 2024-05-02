#calculator.py
from numbr import numbers_sort
from opratr import operators
from crretordr import order
from clcultion import calculation

while True:
    expression = input('Enter you arithmatic operation:- ')

    numbers = numbers_sort(expression)
    operator = operators(expression)
    correct_order = order(operator)
    answer = calculation(numbers, correct_order, operator)

    print('Ans:- ', answer)

    if input('Do you want to continue? (y/n) ') == 'n':
        break
