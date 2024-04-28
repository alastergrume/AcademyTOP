# # Операции сравнения
# if("1" == 1):
#     print("Все правильно")
# else:
#     print("Не верно")
#
# # == - проверка на True (Истина)
# # != - False
# # > - Больше чем
# # > - Меньше чем
# # <= - Меньше или равно
# # >= - Больше или равно
#
# #Логические выражения
# var1 = True
# var2 = False
# print(var1 and var2)
# # and - логическое умножение, истино, если 2 выражения истино.
# print(var1 or var2)
# # or - Логическое сложение, истино, если одно из элементов истино.
# print(not var1)
# # not - логическое отрицание
#
# # ------Пример №1-------
# time = int(input("Введите время в часах: "))
# ticket = False
# money = True
# print((money or ticket) and not luggage and time > 6) # T and T and (зависит от вводимого занчения времени либо T либо F)
# luggage = False
#
# # ------Пример №2-------
# year = int(input("введите год для проверки"))
#
# if year % 4 == 0 and year % 100 !=0: #or year % 400 == 0:
#     print(year, "Високосный год!")
# else:
#     print(year, "не високосный год!")

# Блок №2 - Исключения
a, b = input().split()

try:
    print(int(a)/int(b))
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
# Блок try ищет ошибки, но позволяет отработать программе.
