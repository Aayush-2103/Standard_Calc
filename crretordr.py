def order(operator):
    default_order=['**', '^', '/', '//', '%', '*', '+', '-']
    correct_order = []
    for i in default_order:
        for j in operator:
            if i==j:
                correct_order.append(j)
    return correct_order