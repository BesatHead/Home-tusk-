#Задание №2
my_dict = {'Nikolay': 1996, 'Sergey': 1987, 'Leonid': 1993}
print('Словарь:', my_dict)
print('Год рождения:', my_dict['Sergey'])
a = my_dict.pop('Leonid')
my_dict.update({'Anatoly': 1988,
                'Yulia': 1969})
print('Отсутсвующее значение:', my_dict.get('Leonid'))
print('Удаленное значение:',a)
print('Обновленный словарь:', my_dict)
#Задание №3
print('') # Для разделения заданий в выводе. Удобство чтения.
my_set = {1,2,3,4,2,3,4,4,5,'яблоко','груша','дыня','яблоко','апельсин','дыня'}
print('Множество:',my_set)
my_set.add(6)
my_set.add('ананас')
my_set.remove(5)
print('Обновленное множество:',my_set)