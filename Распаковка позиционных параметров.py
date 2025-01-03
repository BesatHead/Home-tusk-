def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params()
print_params (1, 18, True)
print_params (1, 'Строка',[1, 2, 3])

values_list = [777, 'Пример', False]
values_dict = {'a': 66, 'b': 'Словарь', 'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)
