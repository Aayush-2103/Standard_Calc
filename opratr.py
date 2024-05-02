def operators(exp):
    symbols='/**-+%^!'
    # symbols='//**-+%^!'
    op=''
    sym=[]
    for i in range(len(exp)):
        if exp[i] in symbols:
            op+=exp[i]
        elif exp[i] not in symbols:
            sym.append(op)
            op=''
    operator=[]
    for i in sym:
        if i != '':
            operator.append(i)
    return operator