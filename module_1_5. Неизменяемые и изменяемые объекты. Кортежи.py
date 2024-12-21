# Задание №2
immutable_var = 1, 2, 3, 'Порядковый номер'
immutable_var_2 = 1,2,[1,2,(3*2)]
print(immutable_var)
print(immutable_var_2)
# Задание №3
try:
    immutable_var[0] = 2
except TypeError as a:
    print('Ошибка при изменении кортежа:', a)
print(immutable_var)
# Задание №4
mutable_list = 'Катана', 'Топор', ['Саи', 'Нунчаки']
print(mutable_list)
mutable_list[2][0] = "Катана"
print(mutable_list)
