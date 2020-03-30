coordinates_x = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
try:
    coordinate_x1, coordinate_y1 = input('Введите координаты 1-ой точки ').split()
    coordinate_x2, coordinate_y2 = input('Введите координаты 2-ой точки ').split()
    coordinate_1 = (coordinates_x[coordinate_x1], int(coordinate_y1))
    coordinate_2 = (coordinates_x[coordinate_x2], int(coordinate_y2))
    comparison_1 = (coordinate_1[0] % 2 == 0 and coordinate_1[1] % 2 == 0) or (coordinate_1[0] % 2 != 0 and coordinate_1[1] % 2 != 0)
    comparison_2 = (coordinate_2[0] % 2 == 0 and coordinate_2[1] % 2 == 0) or (coordinate_2[0] % 2 != 0 and coordinate_2[1] % 2 != 0)
    if comparison_1 == comparison_2:
        print('Цвета координат одинаковые ')
    else:
        print('Цвета координат разные ')
except:
    print('Ошибка ввода')
