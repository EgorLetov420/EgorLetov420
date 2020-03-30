try:
    N = int(input('Введите целое число '))  # Input integer number
    X = ((N + 1) % 2) + N + 1
    print(X)
except:
    print('Ошибка ввода')
