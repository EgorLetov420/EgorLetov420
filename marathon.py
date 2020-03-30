m_length = float(input('Введите длину марафона '))
km = float(input('Введите длину пробежки в первый день '))
progress = float(input('Введите в процентах увеличение длины пробежки за день '))
progress = progress / 100
day = 1        # L = km + km * progress * (day - 1)
L = km
while L < m_length:
    day += 1
    L = km + km * progress * (day - 1)
print(day)
