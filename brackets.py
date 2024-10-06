#using stacks the code will understand which expression to solve first
from Calc import solve

def calculate(exp):
    #if expression has parenthesis
    if ('(' or ')') in exp:
        #first we will check if brackets are balanced or not
        n=len(exp)
        bracket = []
        for i in range(n):
            if exp[i]=='(':
                bracket.append(exp[i])

            elif exp[i]==')':
                if bracket:
                    bracket.pop()

                else:
                    return 'Check your expression.'
                    
        else:
            if bracket:
                return 'Check your expression.'
                

        #now when expression has balanced parenthesis we proceed to find the expressions within brackets
        while ('(' or ')') in exp:
            end = exp.index(')')
            start = exp[:end][::-1].index('(')
            
            expression = exp[:end][::-1][:start][::-1]
            answer = solve(expression)

            index = exp.index(expression)-1
            #new expression
            new_exp = exp[:index]+str(answer)+exp[2+index+len(expression):]
            exp = new_exp

        return solve(exp)

    else:             #expression doesn't have parenthesis
        return solve(exp)
    
while True:
    exp = input('Enter expression:- ')
    print('Answer:- ', calculate(exp))

    if input('Do you wanna continue? (y/n)') == 'n':
        break