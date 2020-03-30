print('Введите числа')
Num = []
i = 0
a = float(input())
Num.append(a)
max = lower_max = Num[i]
while Num[i] != 0:
    a = float(input())
    Num.append(a)
    if Num[i] > max:
        lower_max = max
        max = Num[i]
    i += 1
print(lower_max)

