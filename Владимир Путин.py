wrong_user_fio = input('Введите ФИО в неправильном порядке(Иван Иванович Иванов) ')
list_fio = list(wrong_user_fio.split())
right_user_fio = list_fio[2] + ' ' + list_fio[0] + ' ' + list_fio[1]
print(right_user_fio)