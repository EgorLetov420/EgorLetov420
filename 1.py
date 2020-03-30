R, K = input('Введите цену авокадо (раздельно) ').split()
R = int(R)
K = int(K)
N = int(input('Введите количество авокадо '))
Rub = N * R
Kop = N * K
if Kop >= 100:
    Rub += Kop // 100
    Kop = Kop % 100
if Kop < 10:
    Kop = '0' + str(Kop)
print('Вы потратили', Rub, 'рублей', Kop,'копеек')