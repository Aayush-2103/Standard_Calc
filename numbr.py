def numbers_sort(exp):
    digit='.0123456789'
    # symbols='//**-+%^!'
    symbols='/**-+%^!'
    n=''
    i=0

    while i < len(exp):
        if exp[i] in digit:
           n+=exp[i]

        elif exp[i] == ' ':
            i+=1
            continue
        
        elif exp[i] in symbols:
            if exp[i+1] in digit:
                n+=' '

            elif exp[i+1] in symbols:
                n+=' '
                i+=1

            elif exp[i+1] == ' ':
                n+=' '
                i+=1
                continue

        else:
            n=0
            break

            
        i+=1

    if n!=0:
        num_str=n.split(' ')
        num=[]
        for i in num_str:
            if '.' in i:
                num.append(float(i))

            else:
                num.append(int(i))
            
        return num
    
    else:
        return 0