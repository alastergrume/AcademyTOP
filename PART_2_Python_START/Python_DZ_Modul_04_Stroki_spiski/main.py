import random

def HomeWork1_Lessone_List():
    print('''Задание 1
    
    Пользователь вводит с клавиатуры строку. Проверьте
    является ли введенная строка палиндромом. Палинодром - слово,
    которое читается одинаково слева направо и справа налево.
    Например, кок; А роза упала на лапу Азора; доход; А буду я у дуба.
        ''')

    print('''Задание 2
    
    Пользователь вводит с клавиатуры некоторый текст,
    после чего пользователь вводит список зарезервированных
    слов. Необходимо найти в тексте все зарезервированные
    слова и изменить их регистр на верхний. Вывести на
    экран измененный текст.
        ''')

    print('''Задание 3
    Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный
    результат''')


# Python_PZ_Modul__03_Cikly_c_5
def HomeWork2_Lessone_List():
    print('''
    Задание 1
Пользователь вводит число. Определить количество
цифр в этом числе, посчитать их сумму и среднее арифметическое. Определить количество нулей в этом числе.
Общение с пользователем организовать через меню.
    Задание 2
Написать программу, которая выводит на экран
шахматную доску с заданным размером клеточки. Например, три,
***---***---***---***---
***---***---***---***---
***---***---***---***---
---***---***---***---***
---***---***---***---***
---***---***---***---***
    Задание 3
Написать программу, которая проверяет пользователя
на знание таблицы умножения. Программа выводит на
экран два числа, пользователь должен ввести их произведение. Разработать несколько уровней сложности (от-
1личаются сложностью и количеством вопросов). Вывести
пользователю оценку его знаний.
    Задание 4
Вывести на экран ромб из звездочек.'''
          )


# Задание №1
def find_polindrop(word):
    new_word = ''
    for i in word:
        if i.isalpha():
            new_word += i.lower()
    if new_word == new_word[::-1]:
        return f'Выражение "{word}" является Полиндромом'
    else:
        return f'Выражение "{word}" не является Полиндромом'


# Задание №2
def cheked_text_2(user_text, user_reserve_text):
    new_text = ''
    new_text_list = ''
    # Делаем строку без знаков препинания, но с пробелами
    for word in user_text:
        if word.isspace():
            new_text += word
        if not word.isalpha():
            new_text += ' '
        else:
            new_text += word
    # Переводим созданные строки в список и сверяем с зарезервированныеми словами, формируем новый список
    for i in new_text.split():
        if i.lower() in user_reserve_text.split():
            new_text_list += i.upper() + ' '
        else:
            new_text_list += i + ' '
    # Этот цикл бежит по user_text обнаруживает сомвол препинаиния, и добавляет в total_spisok
    step = 0
    totalText = ''
    for a in user_text:
        if a.isalpha() or a.isspace():
            totalText += new_text_list[step]
            step += 1
        else:
            totalText += a

    return f'Преобразованный текст: {totalText}'


# Задание №3
def numb_offers(queryText):
    offers = 0
    for i in queryText:
        if i == '.':
            offers += 1
        if i == '!':
            offers += 1
        if i == '?':
            offers += 1
    return f"Количество предложений - {offers}"


def HomeWork2_Lesson1(numbers):
    """Пользователь вводит число. Определить количество
    цифр в этом числе, посчитать их сумму и среднее арифметическое. Определить количество нулей в этом числе.
    Общение с пользователем организовать через меню.
    """

    amount_of_numbers = 0  # Колчество знаков в числе
    zero_in_numbers = 0  # Количество нолей в числе
    sum_of_numbers = 0  # Сумма чисел
    for number in str(numbers):
        amount_of_numbers += 1
        if number == "0":
            zero_in_numbers += 1
        sum_of_numbers += int(number)
    average = sum_of_numbers / amount_of_numbers  # Среднееарифметическое
    return amount_of_numbers, sum_of_numbers, average, zero_in_numbers


def HomeWork2_Lesson2():
    """
    Задание 2
Написать программу, которая выводит на экран
шахматную доску с заданным размером клеточки. Например, три,
***---***---***---***---
---***---***---***---***
***---***---***---***---
---***---***---***---***
***---***---***---***---
---***---***---***---***
    """
    counter = 0
    for i in range(0, 6):
        if i % 2 != 0:
            counter = 3
        for j in range(0, 24):
            if counter <= 2:
                print("*", end=" ")
            if counter >= 3:
                print("-", end=" ")
            counter += 1
            if counter == 6:
                counter = 0
            if j == 23:
                print(end="\n")
                counter = 0


def HomeWork2_Lesson3():
    #    """
    # Написать программу, которая проверяет пользователя
    # на знание таблицы умножения. Программа выводит на
    # экран два числа, пользователь должен ввести их произведение.
    # Разработать несколько уровней сложности (отличаются сложностью и количеством вопросов).
    # Вывести пользователю оценку его знаний.
    # """
    #
    while True:
        try:
            print("""
            Уровни сложности:
                1. Легкий
                2. Средний
                3. Сложный
                0. Выход
            """)
            level = int(input('Введите уровен сложности - '))
            if level == 0:
                break
            if level == 1:
                print("Уровень сложности - Легкий (до 2-х выигрышей)")
                start_of_range = 2
                end_of_range = 4
                number_of_move = 3
            if level == 2:
                print("Уровень сложности - Средний (до 6-ти выигрышей)")
                start_of_range = 4
                end_of_range = 7
                number_of_move = 6
            if level == 3:
                print("Уровень сложности - Сложный (до 10-ти выигрышей)")
                start_of_range = 7
                end_of_range = 9
                number_of_move = 10
        except Exception:
            print("Попробуй ещё раз")

        victory = 0
        failer = 0
        while victory < number_of_move:
            print(f'Побед - {victory}, Проигрышей - {failer}')
            try:
                first_number = random.randint(start_of_range, end_of_range)
                second_number = random.randint(start_of_range, end_of_range)
                python_answer = first_number * second_number
                student_answer = int(input((f"Сколько будет {first_number} * {second_number} ? (Выход - 0) Твой ответ - > ")))
                if student_answer == 0:
                    break
                if python_answer == student_answer:
                    victory += 1
                if python_answer != student_answer:
                    failer += 1
            except Exception:
                print("Давай начнем сначала!")
                victory = 0
                failer = 0
        try:
            if student_answer == 0:
                break
            print(f'Твой балл - {victory / failer}!')
            print(f'Побед - {victory}, Поигрышей - {failer}')
        except ZeroDivisionError:
            print("Ты выиграл!")
            print(f'Ты набрал максимальное количество баллов!')
            print(f'Побед - {victory}, Поигрышей - {failer}')

        choice = input("Сыграем ещё - 1. Выход - 0. Твой ответ - > ")
        if choice == 0:
            break
        if choice == 1:
            continue



def menu_of_lessons_in_HomeWork_1():
    while True:
        try:
            lesson = int(input('Введите номер задания (для выхода 0) - '))
            if lesson > 3 or 0 > lesson:
                print("Только три задания и выход!")
            elif lesson == 1:
                print('Проверка работоспособности фукнции:')
                print(find_polindrop('кок'))
                print(find_polindrop('А роза упала на лапу Азора'))
                print(find_polindrop('доход'))
                print(find_polindrop('А буду я у дуба'))
                while True:
                    word = input("Введите ваше строковое выражение для проверки (Число для выхода!) - ")
                    if word.isdigit():
                        break
                    else:
                        print(find_polindrop(word))
            elif lesson == 2:
                user_text = input("Введите текст - ")
                user_reserve_text = input("Введите зарезервированные слова - ")
                print(cheked_text_2(user_text, user_reserve_text))
            elif lesson == 3:
                print(numb_offers(input("Введите текст - ")))
            elif lesson == 0:
                break
        except ValueError:
            print("Вводить нужно номер задания цифрой!")


def menu_of_lessons_in_HomeWork_2():
    while True:
        try:
            lesson = int(input('Введите номер задания (для выхода 0) - '))
            if lesson > 3 or 0 > lesson:
                print("Только три задания и выход!")
            elif lesson == 1:
                print("""
    1. Определить количество знаков в числе?
    2. Посчитать сумму?
    3. Посчитать среднеарифметическое?
    4. Определить количество нолей?
    0. Выход
    """)
                number = (int(input("Введите число - ")))
                while True:
                    try:
                        user_choice = (int(input("Сделайте Ваш выбор - ")))
                        response = HomeWork2_Lesson1(number)
                        if lesson > 4 or 0 > lesson:
                            print("Только четыре задания и выход!")
                        if user_choice == 0:
                            break
                        if user_choice == 1:
                            print(f'Количество знаков в числе - {response[0]}')
                        if user_choice == 2:
                            print(f'Сумма чисел составляет - {response[1]}')
                        if user_choice == 3:
                            print(f'Среднеарифметическое всех знаков числа - {response[2]}')
                        if user_choice == 4:
                            print(f'Количество нолей в числе - {response[3]}')
                    except ValueError:
                        print("Вводить нужно номер задания цифрой!")
            elif lesson == 2:
                print(HomeWork2_Lesson2())
            elif lesson == 3:
                print(HomeWork2_Lesson3())
            elif lesson == 0:
                break
        except ValueError:
            print("Вводить нужно номер задания цифрой!")


def main():
    while True:
        try:
            lessonPart = int(input("Введите номер домашнего задания (для выхода 0) - "))
            if lessonPart < 0 or lessonPart > 2:
                print("Всегда два домашних задания, попробуй ещё раз")
            if lessonPart == 1:
                HomeWork1_Lessone_List()
                menu_of_lessons_in_HomeWork_1()
            if lessonPart == 2:
                HomeWork2_Lessone_List()
                menu_of_lessons_in_HomeWork_2()
            if lessonPart == 0:
                break

        except ValueError:
            print("Вводить нужно номер задания цифрой!")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
