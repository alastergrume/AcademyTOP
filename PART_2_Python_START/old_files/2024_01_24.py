#     # """ПРАКТИЧЕСКОЕ ЗАДАНИЕ
#     # ВВЕДЕНИЕ В ЯЗЫК Python
#     # Модуль 3. Циклы. Част. 4
#     # """
#
#
# lenght_line = int(input("Введите длину стороны - "))
# for i in range(lenght_line):
#     print('*', end=' ')
#     for j in range(lenght_line):
#         print('*', end=' ')
#     print('')
#
# height_line = int(input("Введите высоту стороны A - "))
# width_line = int(input("Введите длину стороны B - "))
# for i in range(height_line-1):
#     print('*', end=' ')
#     for j in range(width_line-1):
#         print('*', end=' ')
#     print('')
#
#
# lenght_line = int(input("Введите длину стороны - "))
# for i in range(lenght_line):
#     if i == 0 or i == lenght_line-1:
#         print('* ' * lenght_line)
#     else:
#         print('* ' + '  '*(lenght_line-2) + '*')
#
#
# height_line = int(input("Введите высоту стороны A - "))
# width_line = int(input("Введите длину стороны B - "))
# for i in range(height_line):
#     if i == 0 or i == height_line-1:
#         print('* ' * (width_line))
#     else:
#         print('* ' + '  ' * (width_line-2) + '*')
#
#
#
#     """Домашнее задание
#     Курс: «Введение в язык
#     программирования Python
#     Модуль 3. Циклы. Часть 4"""
#
#     '''Задание 1'''
#
# value1 = int(input("Введите первое число для проверки - "))
# value2 = int(input("Введите второе число для проверки - "))
#
# for value in range(value1, value2+1):
#     k=0
#     if value == 1 or value == 2 or value == 3:
#         print(value)
#     if value > 3:
#         for i in range(2, int(value/2)+1):
#             if value % i == 0:
#                 k = False
#                 break
#             else:
#                 k=True
#     if k:
#         print(value)
#
#
#     '''Задание 2'''
#
#
#
# for i in range(1, 11):
#     print('-' * 100)
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i*j}', end="   ")
#         if j == 10:
#             print(end="\n")
#

number_i = int(input("Введите число - "))
number_j = int(input("Введите число - "))

for i in range(number_i, number_j+1):

    b = 0
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}', end="  |  ")
        b += len(str(f'{i} * {j} = {i * j}  |  '))
        if j == 10:
            print(end="\n")
    # print(b)
    print('-' * b)


