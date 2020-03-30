Num = int(input('Введите число '))
if Num > 0:
    i = 1
    comparison = Num - i
    output = ''
    while comparison > 1:
        if Num % comparison != 0:
            i += 1
            comparison = Num - i
        else:
            output = 'число составное'
            break
    if output == '':
        output = 'число простое'
    print(output)
else:
    print('Ошибка ввода')
