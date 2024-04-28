print("""
        ------------------------------------------------
                        Домашнее задание
        Курс: "Введение в язык программирования Python"
            Модуль 2. Операторы ветвлений. Часть 2
        ------------------------------------------------
                            
                            Задание 1
      
    Пользователь вводит с клавиатуры номер дня недели (1-7). 
    Необходимо вывести на экран названия дня недели. 
    Например, если 1, то на экране надпись понедельник, 2 - вторник и т.д.
                            
                            Задание 2
      
    Пользователь вводит с клавиатуры номер месяца 
    (1-12). Необходимо вывести на экран название месяца. 
    Например, если 1, то на экране надпись январь, 2 — февраль и т.д. 
                            
                            Задание 3
      
    Пользователь вводит с клавиатуры число. Если число 
    больше нуля нужно вывести надпись «Numberis positive», 
    если меньше нуля «Number is negative», если равно нулю 
    «Number is equal to zero»

                            Задание 4
      
    Пользователь вводит два числа. Определить, равны 
    ли эти числа, и, если нет, вывести их на экран в порядке 
    возрастания.      

    """
)

while True:
    try:
        number_lesson = int(input("Введите номер задания - "))
        if number_lesson == 0:
            break          
        if number_lesson == 1:
            while True:
                day_number = int(input('Введите номер дня недели (для выхода 0) - '))
                days_in_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье",]
                if day_number == 0:
                    break
                elif 0 < day_number > 7:
                    continue
                else:
                    print(days_in_week[int(day_number)-1])
        if number_lesson == 2:
            while True:
                month_number = int(input('Введите номер месяца (для выхода 0) - '))
                month_in_year = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
                if month_number == 0:
                    break
                elif 0 < month_number > 12:
                    continue
                else:
                    print(month_in_year[int(month_number)-1])
        if number_lesson == 3:
            input_number = int(input('Введите целое число - '))
            if input_number > 0:
                print('Numberis positive')
            elif input_number < 0:
                print('Number is negative')
            else:
                print('Number is equal to zero')
        if number_lesson == 4:
            number_1, number_2 = input('Введите два числа через пробел - ').split()
            if number_1 == number_2:
                print(f'Число {number_1} равно числу {number_2}')
            if number_1 != number_2:
                if number_1 > number_2:
                    number_1, number_2 = number_2, number_1
                print(f'Вы ввели числа {number_1} и {number_2} они не равны друг другу')
    except Exception as e:
        print(f'Вводи правильно. Ошибка {e}')