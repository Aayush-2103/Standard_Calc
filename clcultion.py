def calculation(numbers, correct_order, operator):

    for i in range(len(correct_order)):
        if correct_order[i] == '**' or correct_order[i] == '^':
            index = operator.index(correct_order[i])
            ans = numbers[index] ** numbers[index+1]
            numbers.pop(index)
            numbers.pop(index)
            numbers.insert(index, ans)
            operator.pop(index)

        elif correct_order[i] == '/':
            index = operator.index(correct_order[i])
            ans = numbers[index] / numbers[index+1]
            numbers.pop(index)
            numbers.pop(index)
            numbers.insert(index, ans)
            operator.pop(index)

        elif correct_order[i] == '//':
            index = operator.index(correct_order[i])
            ans = numbers[index] // numbers[index+1]
            numbers.pop(index)
            numbers.pop(index)
            numbers.insert(index, ans)
            operator.pop(index)

        elif correct_order[i] == '%':
            index = operator.index(correct_order[i])
            ans = numbers[index] % numbers[index+1]
            numbers.pop(index)
            numbers.pop(index)
            numbers.insert(index, ans)
            operator.pop(index)

        elif correct_order[i] == '*':
            index = operator.index(correct_order[i])
            ans = numbers[index] * numbers[index+1]
            numbers.pop(index)
            numbers.pop(index)
            numbers.insert(index, ans)
            operator.pop(index)

        elif correct_order[i] == '+':
            index = operator.index(correct_order[i])
            ans = numbers[index] + numbers[index+1]
            numbers.pop(index)
            numbers.pop(index)
            numbers.insert(index, ans)
            operator.pop(index)

        elif correct_order[i] == '-':
            index = operator.index(correct_order[i])
            ans = numbers[index] - numbers[index+1]
            numbers.pop(index)
            numbers.pop(index)
            numbers.insert(index, ans)
            operator.pop(index)
        
    return ans