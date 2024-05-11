'''
Операторы ветвления
if (','): # (Если условие выполняется)
    print(',')
else: # Если условие не выполняется
'''

value = int(input('Введите число: '))
if value > 10:
    print (value, ">10")
else:
    print(value, '<10')

'''
# value == 10
# value != 10
# >= <=
'''
доп условия
value = int((input('Введит числов в интервале от 1 до 20: ')))
if value != 20:
    if value > 10:
        print(value, 'Число находится в интервале от 11 до 19')
    else:
        print(value, 'меньше 10')
else:
    print(value, '= 20')

years = 1988
if years % 4 == 0:
    if years % 100 != 0:
        if years % 400 == 0:
            print('Год', years, 'Високосный')
else:
    print('Год', years, 'не Високосный')

if (years % 4 == 0) and (years % 100 != 0) or (years % 400 == 0):
    print('Год', years, 'Високосный')
else:
    print('Год', years, 'не Високосный')