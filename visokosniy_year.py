year = int(input('Введите год '))
starting_point = 2000
days_v = 366     # The number of days in a leap year
days = 365     # The number of days in a normal year
comparison = (starting_point - year) % 4
if comparison == 0:
    print('В ', year, ' году - ', days_v, 'дней')
else:
    print('В ', year, ' году - ', days, 'дней')