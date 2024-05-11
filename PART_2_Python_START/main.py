'''
Операторы ветвления
if (','): # (Если условие выполняется)
    print(',')
else: # Если условие не выполняется
'''
#
# value = int(input('Введите число: '))
# if value > 10:
#     print (value, ">10")
# else:
#     print(value, '<10')

'''
# value == 10
# value != 10
# >= <=
'''
# доп условия
# value = int((input('Введит числов в интервале от 1 до 20: ')))
# if value != 20:
#     if value > 10:
#         print(value, 'Число находится в интервале от 11 до 19')
#     else:
#         print(value, 'меньше 10')
# else:
#     print(value, '= 20')
#
# years = 1988
# if years % 4 == 0:
#     if years % 100 != 0:
#         if years % 400 == 0:
#             print('Год', years, 'Високосный')
# else:
#     print('Год', years, 'не Високосный')
#
# if (years % 4 == 0) and (years % 100 != 0) or (years % 400 == 0):
#     print('Год', years, 'Високосный')
# else:
#     print('Год', years, 'не Високосный')


print("ДЗ 10.01.2024")
while(True):
    print('*'*11)
    print('Задание 1. Проверка на четность числа')
    print('Задание 2. Проверка кратности на 7')
    print('Задание 3. Найти максимальное число')
    print('Задание 4. Найти минимальное число')
    print('Задание 5. Показать выбранное действие')
    print('0 - выход')
    print('*'*11)
    value = int(input("Введи номер задания: "))
    if value == 1:
        var1 = int(input("Введите число для проверки: "))
        if var1 % 2 == 0:
            print(var1, "Even number")
        else:
            print(var1, "Odd Number")
    elif value == 2:
        var2 = int(input("Введите число для проверки: "))
        if var2 % 7 == 0:
            print(var2, "Number is multiple 7")
        else:
            print(var2, "Number is not multiple 7")
    elif value == 3:
        var3_1 = int(input("Введите число №1 для проверки: "))
        var3_2 = int(input("Введите число №2 для проверки: "))
        print(f'Максимальное число: {max(var3_1, var3_2)}')
    elif value == 4:
        var4_1 = int(input("Введите число №1 для проверки: "))
        var4_2 = int(input("Введите число №2 для проверки: "))
        print(f'Минимальное число: {min(var4_1, var4_2)}')
    elif value == 5:
        var5_1 = int(input("Введите число №1: "))
        var5_2 = int(input("Введите число №2: "))
        print('''№1 - Показать сумму двух чисел
№2 - Показать разницу двух числе
№3 - Показать среднеарифметическое
№4 - Показать произведение
№5 - Выход''')
        while(True):
            value_5 = int(input("Введите номер действия: "))
            if value_5 == 1:
                print(f'Сумма двух числе составляет {var5_1 + var5_2}')
            elif value_5 ==2:
                print(f'Разница двух числе составляет {var5_1 - var5_2}')
            elif value_5 == 3:
                print(f'Среднеарифметическое двух числе составляет {(var5_1 + var5_2)/2}')
            elif value_5 == 4:
                print(f'Произведение двух числе составляет {var5_1 * var5_2}')
            elif 0 <= value_5 > 5:
                print("Вы ввели неверно число!")
            elif value_5 == 5:
                break

    elif value == 0:
        break #Выход из цикла
    else:
        print('Вы ввели не верное задание')