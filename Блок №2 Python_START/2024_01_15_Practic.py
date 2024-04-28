"""Задание №1"""
day_time = (60**2)*24
while True:
    time_in_second = int(input("Введите время в секундах прошедшее с начала дня = "))
    print('#1. Посчитать сколько часов осталось до полуночи?')
    print('#2. Посчитать сколько минту осталось до полуночи?')
    print('#3. Посчитать сколько секунд осталось до полуночи?')
    print('#4. Выход')
    value = int(input('Выберите действие = '))
    if value == 1:
        print(f'До полуночи осталось {(day_time - time_in_second)/60**2} часов')
    if value == 2:
        print(f'До полуночи осталось {(day_time - time_in_second)/60} минут')
    if value == 3:
        print(f'До полуночи осталось {(day_time - time_in_second)} секунд')
    if value == 4:
        break

"""Задание №2"""
while True:
    diametr = int(input("Введите диаметр окружности = "))
    print('#1. Посчитать окружность?')
    print('#2. Посчитать периметр?')
    print('#3. Выход')
    value = int(input('Выберите действие = '))
    if value == 1:
        print(f'Площадь окружности {(2*3.14*(diametr/2))**2}')
    if value == 2:
        print(f'Периметр окружности {(3.14*(diametr/2))**2}')
    if value == 3:
        break

"""Задание №3"""
while True:
    price_gamepad = int(input("Введите цену приставки = "))
    kol_vo_gamepad = int(input("Введите количество приставок= "))
    diskont = int(input("Введите размер скидки = "))
    print('#1. Посчитать общую сумму заказа?')
    print('#2. Посчитать стоимость одной приставки с диконтом?')
    print('#3. Выход')
    value = int(input('Выберите действие = '))
    if value == 1:
        print(f'Общая сумма заказа {price_gamepad*kol_vo_gamepad}')
    if value == 2:
        print(f'Цена приставки со скидкой {(price_gamepad - ((price_gamepad * diskont) / 100))}')
    if value == 3:
        break

"""Задание №4"""

while True:
    razmer_faila = int(input("Введите размер файла в гигабайтах = "))
    speed = int(input("Введите скорость интернет соединения, Gb/s = "))

    print('#1. Посчитать за сколько часов скачается файл?')
    print('#2. Посчитать за сколько минут скачается файл?')
    print('#3. Посчитать за сколько секунд скачается файл?')
    print('#4. Выход')
    value = int(input('Выберите действие = '))
    if value == 1:
        print(f'Файл скачается за {(((razmer_faila*1024)*1024)/speed)/60**2} часов')
    if value == 2:
        print(f'Файл скачается за {(((razmer_faila*1024)*1024)/speed)/60} минут')
    if value == 3:
        print(f'Файл скачается за {(((razmer_faila*1024)*1024)/speed)} секунд')
    if value == 4:
        break

"""Задание №5"""

while True:
    print('#25. Выход')
    houre = int(input("Который час? = "))

    if 0 <= houre < 6:
        print(f'Good Night')
    elif 6 <= houre < 13:
        print(f'Good Morning')
    elif 13 <= houre < 17:
        print(f'Good Day')
    elif 17 <= houre < 24:
        print(f'Good Evening')
    else:
        break

