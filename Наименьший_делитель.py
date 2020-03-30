Num = int(input('Введите натуральное число больше 2 '))
i = 2
while i <= Num:
    if Num % i == 0:
        print(i)
        break
    else:
        i += 1
