def numbers_sort(exp):
    digit='.0123456789'
    symbols='//**-+%^!'
    n=''
    i=0
    while i < len(exp):
        if exp[i] in digit:
           n+=exp[i]
        elif exp[i] in symbols:
            if exp[i+1] in digit or exp[i+1] == ' ':
                n+=' '
            elif exp[i+1] in symbols:
                n+=' '
                i+=1
        i+=1
    num_str=n.split(' ')
    num=[]
    for i in num_str:
        num.append(float(i))
    return num