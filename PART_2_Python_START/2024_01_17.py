"""--------------Циклы Часть №1 Практическое задание----------------"""

# print(""" Задание №1""")

# a, b = input("Введите два числа -> ").split()
# for i in range(int(a), int(b) + 1):
#     print(i, end=" ")


# print("\n""""Задание №2""")

# a, b = input("Введите два числа -> ").split()
# for i in range(int(a), int(b) + 1):
#     if i % 2 != 0:
#         print(i, end=" ")

# print("\n""""Задание №3""")

# a, b = input("Введите два числа -> ").split()
# for i in range(int(a), int(b) + 1):
#     if i % 2 == 0:
#         print(i, end=" ")

print("\n""""Задание №4""")

a, b = input("Введите два числа -> ").split()
if a < b:
   a, b = b, a
for i in range(int(a), int(b) -1, -1):
    print(i, end=" ")

print("\n""""Задание №5""")

a, b = input("Введите два числа -> ").split()
if a < b:
   a, b = b, a
for i in range(int(a), int(b) -1, -1):
   if i % 2 != 0:
       print(i, end=" ")

"""--------------- Циклы Часть №1 Домашнее задание ----------------"""
# print('\n''Задание №1')

# a, b = input("Введите два числа -> ").split()
# for i in range(int(a), int(b) + 1):
#     if i % 7 == 0:
#         print(i, end=" ")

# print('Задание №1')

# a, b = input("Введите два числа -> ").split()
# numb_1 = ' '
# numb_2 = ' '
# numb_3 = ' '
# numb_4 = ' '
# for i in range(int(a), int(b)+1):
#     numb_1 += str(i) + ' '
#     numb_2 += str((int(b) + int(a)) - i)+' ' # обнуляем первое значение, для этого добавляем к большему значению меньшее, как бы приводя диапазон в границы, с которых задается интервал
#     if i % 7 == 0:
#         numb_3 += str(i)+' '
#     if i % 5 == 0:
#         numb_4 += str(i)+' '
# print('\n',numb_1, end=' ')
# print('\n',numb_2, end=' ')
# print('\n',numb_3, end=' ')
# print('\n',numb_4, end=' ')

# '''Блиц'''
# price = int(input('Введите стоимость манадрин'))
# weight = 1
# st_t = 0
# while (weight <= 10) :
#         st_t = price * weight
#         if (st_t <= 1000):
#                 print(st_t)
#         else:
#                 break
#         weight += 1




