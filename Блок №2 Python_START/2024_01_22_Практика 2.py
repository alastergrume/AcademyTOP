import random
from time import time

"""Модуль Модуль 3. Циклы. Часть 2"""

"""Задание №1"""
number = int(input("Введите число - "))
for i in range(1, 10):
    print(f'{number} * {i} = {number * i}')

"""Задание №2"""
print("""
 Добрый День!
 Сегодня вы можете произвести конвертацию интресующей Вас валюты
 Прошу выбрать из достыпных:
 RUB - GBP - Введите 1
 RUB - USD - Введите 2
 RUB - EUR - Введите 3
 RUB - CNY - Введите 4
 Для выхода введите - 9
     """
      )
while True:
    try:
        currency_1 = float(input("Введите сумму для конвертации в формате *.* - "))
        if currency_1 == 9:
            break
        currency_2 = str(input("Введите наименование валюты - "))
        if currency_2 == "GBP":
            print(currency_1 * 111.50)
        if currency_2 == "USD":
            print(currency_1 * 87.97)
        if currency_2 == "EUR":
            print(currency_1 * 95.89)
        if currency_2 == "CNY":
            print(currency_1 * 12.18)
    except ValueError:
        print("Введено некорректное значение")

"""Задание 3"""



while True:
    # try:

    a = int(input("Введите левую границу диапазона - "))
    b = int(input("Введите правую границы диапазона - "))
    number = int(input("Введите число входящее в диапазон - "))
    if a < number < b:
        for i in range(a, b+1):
            if i == number:
                print(f'!{i}!', end=" ")
            else:
                print(i, end=" ")

        break
    else:
        print("Введено неверное значение")

"""Задание 4"""
start_time = time()
print("Угадай какое число я загадал")
print("Для выхода введи - 0"'\n')
hidden_number = random.randint(1, 500)
attempt = 0
while True:
    attempt += 1
    user_number = int(input("Введите число - "))
    if user_number < hidden_number:
        print(f'Ваше число меньше загаданного')
    if user_number > hidden_number:
        print(f'Ваше число ,больше загаданного')
    if user_number == hidden_number:
        print("Ты выиграл!")
        break
    if user_number == 0:
        print("Ты сдался!")
        break
end_time = time()
print(f"потратил {attempt} попыток, за {int(end_time-start_time)} секунд")