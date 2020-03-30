try:
    order = ['белое вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']  # restaurant's junk ordered by User
    old_dish = input('Введите блюдо, которое вы хотите исключить из заказа ')
    new_dish = input('Введите новое блюдо ')
    i = order.index(old_dish)
    order[i] = new_dish
    print(order)
except:
    print('Введено неправильное блюдо')

    