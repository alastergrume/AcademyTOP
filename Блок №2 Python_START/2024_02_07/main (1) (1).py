# # ------------- Модули -----------------
# import random
# print(random.randint(1, 100))
#
#
# # второй вариант вызова
#
# from random import randint
# import math
# def sin(x):
#     if 2 * x == pi:
#         return 0.999999
#     else:
#         return None
# pi = 3.14
#
# print(f"один {math.sin(math.pi/2)}")
# print(f"два {sin(pi/2)}")
#
#
#
# print(randint(1, 100))
#
# # Некторые библиотеки невозможно подключить без указаия ее методов, функций и констант в коде.
#
# print(math.pi, math.sin(50)) # вывод констант из библиотеки


# -------------- Практическое задание -------------------

# Написать программу «успеваемость». Пользователь вводит 10 оценок студента. Оценки от 1 до 12. Реализовать меню для пользователя:
# ■ Вывод оценок (вывод содержимого списка);
# ■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
# ■ Выходит ли стипендия (стипендия выходит, если
# средний балл не ниже 10.7);
# ■ Вывод отсортированного списка оценок: по возрастанию или убыванию.

import def1_vivod as vivod
from def3_perez import perez as p
from def2_srBall import *
import def4_zap

def menu():
    print('Программа "Успеваемость"')
    print('1. Вывод оценок:')
    print('2. Выходит ли стипендия:')
    print('3. Пересдача экзамена:')
    print('4. Заполнить оценки')
    print('0. Выход:')

# MAIN

spisok = [0 for i in range(10)]
def4_zap.zap(spisok)
while True:

    menu()
    value = int(input('Введите номер меню - '))
    if value == 1:
        vivod.vivod(spisok)
    elif value == 2:
        srballStep(spisok)
    elif value == 3:
        p.perez(spisok)
    else:
        break

print("*" * 11, '\nДо новых встреч')
