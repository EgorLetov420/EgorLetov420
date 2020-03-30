num = input('Введите числа через ",": ').split(',')
max_num = float(num[0])
i = 0
j = len(num)
while i <= (j-1):
    if (float(num[i])) > max_num:
        max_num = float(num[i])
    i += 1
print(max_num)
