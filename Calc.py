#calculator.py
from numbr import numbers_sort
from opratr import operators
from crretordr import order
from clcultion import calculation

expression = input('Enter you arithmatic operation:- ')

numbers = numbers_sort(expression)
operator = operators(expression)
correct_order = order(operator)
answer = calculation(numbers, correct_order, operator)

print(answer)


"""
OVERVIEW:- 
Abbhi tak toh code bohut solid h....lekin there are some bugs. Like agr user ne galti se koi galat operator diya toh uska error statement kaise aayega woh krna h. And operation mein brackets wala feature bhi add krna h and many more other scientific operations bhi.

ek aur bug mila mujhe. like 
1@2+1 ko mera program 12+1 soch kr 13 output diya.
"""