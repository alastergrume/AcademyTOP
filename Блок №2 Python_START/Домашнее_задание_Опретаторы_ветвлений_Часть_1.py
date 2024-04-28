print("Домашнее задание Модуль 2. Операторы ветвлений Часть 1")
while(True):
    print('*'*11)
    print('Задание 1. Вывод на экран сумму трех чисел или произведение числа')
    print('Задание 2. Вывод на экран максимум из трех чисел, минимум из трех числе, или среднеарифметическое')
    print('Задание 3. Перевод метров в мили, дюймы, ярды')
    print('0 - выход')
    print('*'*11)
    try:
        value = int(input("Введи номер задания: "))
        if value == 1:
            while True:
                a = int(input("Введите число №1 > "))
                b = int(input("Введите число №2 > "))
                c = int(input("Введите число №3 > "))
                print("№ 1 - Сумма трех чисел")
                print("№ 2 - Произведение трех чисел")
                print("№ 0 - Выход")
                number1 = int(input("Введите номер задания - "))
                if number1 == 1:
                    print(f'Сумма трех чисел = {a+b+c}')
                elif number1 == 2:
                    print(f'Произведение трех чисел = {a*b*c}')
                elif number1 == 0:
                    break
                else:
                    print("Вы ввли некорктное значение")
        elif value == 2:
            while True:
                    a = int(input("Введите число №1 > "))
                    b = int(input("Введите число №2 > "))
                    c = int(input("Введите число №3 > "))
                    print("Задание 1 - Найти максимум из трех чисел")
                    print("Задание 2 - Найти минимум из трех чисел")
                    print("Задание 3 - Найти среднеарифметическое трех чисел")
                    print("0 - Выход")
                    number2 = int(input("Введите номер задания"))
                    if number2 == 1:
                        print(f'Максимум из трех чисел {max(a, b, c)}')
                    elif number2 == 2:
                        print(f'Минимум из трех чисел {min(a, b, c)}')
                    elif number2 == 3:
                        print(f'Среднеарифметическое трех чисел {sum(a, b, c)/3}')
                    elif number2 == 0:
                        break
                    else:
                        print("Вы ввли некорктное значение")
        elif value == 3:
            while True:
                lenght = int(input("Введите количество метров > "))
                print("Что нужно сделать?")
                print("Введите 1 - Перевести метры в мили")
                print("Введите 2 - Перевсти метры в дюймы")
                print("Введите 3 - Перевести метры в ярды")
                print("0 - Выход")
                number3 = int(input("Введите номер задания"))
                if number3 == 1:
                    print(f'В {number3} метрах {lenght/1609.344} миль')
                elif number3 == 2:
                    print(f'В {number3} метрах {lenght*39.37} дюймов')
                elif number3 == 3:
                    print(f'В {number3} метрах {lenght*1.0936132983377} ярдов')
                elif number3 == 0:
                        break
                else:
                    print("Вы ввли некорктное значение")
        elif value == 0:
            break #Выход из цикла
        else:
            print('Вы ввели не верное задание')
    except ValueError:
        print("Введите целое число!")