import time
from random import randint

# less 1
def text_format(text, signature):
    """
    Функция, которая отображает на экран
    форматированный текст, указанный ниже:
    “Don't compare yourself with anyone in this world…
    if you do so, you are insulting yourself.”
                                            Bill Gates
    """

    new_text = ''
    text_counter = 0
    for i in text:
        if text_counter == 50:
            new_text += '\n'
            text_counter = 0
        else:
            new_text += i
            text_counter += 1
    new_text += '\n' + (50 - len(signature)) * ' '
    for j in signature:
        new_text += j
    return new_text


# less_2
def numbers(numb_one, numb_two):
    """
    Функция, которая принимает два числа
    в качестве параметра и отображает все четные числа
    между ними.
    """
    even_numbers = ''
    number_counter = 0
    for i in range(int(numb_one), int(numb_two) + 1):
        if i % 2 == 0:
            if number_counter != ((len(range(int(numb_one), int(numb_two)))) // 2):
                even_numbers += f'{i}, '
                number_counter += 1
            else:
                even_numbers += str(i)
    return even_numbers


# less 3
def squre(side_len, simbol, bool_meaning=False):
    """
    Функция, которая отображает пустой или
    заполненный квадрат из некоторого символа. Функция
    принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
        ■ если она равна True, квадрат заполненный;
        ■ если False, квадрат пустой.
    """
    if bool_meaning == 'y':
        bool_meaning = True
    else:
        bool_meaning = False
    if bool_meaning == True:
        for i in range(int(side_len)):
            for j in range(int(side_len)):
                print(simbol, end='\t')
            print('\n')
    else:
        for i in range(int(side_len)):
            if i == 0 or i == int(side_len) - 1:
                print((simbol + '  ') * int(side_len))
            else:
                print(simbol + (("  " + (" ") * int(len(simbol))) * (int(side_len) - 2)) + "  " + simbol)


# less 4
def min_of_five(n_one, n_two, n_three, n_foure, n_five):
    """
    Функция, которая возвращает минимальное
    из пяти чисел. Числа передаются в качестве параметров.
    """
    return min([n_one, n_two, n_three, n_foure, n_five])


# less 5
# var 1
def product_of_numbers(start, end):
    """
    Функция, которая возвращает произведение чисел в указанном диапазоне.
    Границы диапазона передаются в качестве параметров.
    Если границы диапазона перепутыны (например, 5 - верхняя граница, 25 -
    нижняя граница), они меняются местами
    """
    product = 1
    if int(start) > int(end):
        start, end = end, start
    for i in range(int(start), int(end) + 1):
        product *= i
    return product


# var 2
def product_of_numbers_2(param_of_product):
    product = 1
    range_of_cicle = sorted(param_of_product)
    for i in range(int(range_of_cicle[0]), int(range_of_cicle[1]) + 1):
        product *= i
    return product


# less 6
def number_of_digits(number):
    startTime = time.time()
    counter = 0
    for i in number:
        counter += 1
    endTime = time.time()
    return counter, "Время выполнения", endTime - startTime


def number_recursion(number, counter):
    counter = counter
    if number == '':
        return counter
    else:
        counter += 1
        return number_recursion(number[1:], counter)


def digits_index(nb):
    return len(nb)


def generate_number(choice, digits, rangeOfNumbers):
    if choice == '1':
        numb = input("Чтобы посчитать количество символов введите число - ")
    if choice == '2':
        numb_1 = [randint(0, int(digits)) for x in range(int(rangeOfNumbers))]
        numb = ''
        for i in numb_1:
            numb += str(i)
    return numb


def main_less_6():
    """
    Функция, которая считает количество
    цифр в числе. Число передаётся в качестве параметра. Из
    функции нужно вернуть полученное количество цифр.
    Например, если передали 3456, количество цифр будет 4.
    """
    choice = input("'1' для самостоятельнгого ввода, '2' для автоматической генерации - ")
    if choice == "1":
        digits = input("Введите число - ")
    if choice == "2":
        digits = input("Введите число для генерации - ")
        rangeOfNumbers = input("Длина генерации - ")
    numbOf = generate_number(choice, digits, rangeOfNumbers)
    # Функция №1
    print("Цикл for:", number_of_digits(numbOf))

    # Функция №2
    start_time = time.time()
    try:
        recurs = number_recursion(numbOf, counter=0)
        end_time = time.time()
    except Exception as e:
        end_time = time.time()
        if e:
            print("Метод рекурсии:", e, "время выполнения:", end_time - start_time)
        else:
            print("Метод рекурсии:", recurs, "время выполнения:", end_time - start_time)

    # Функция №3
    start_time = time.time()
    len_method = digits_index(numbOf)
    end_time = time.time()
    print("Метод Len():", len_method, "время выполнения:", end_time - start_time)


# less 7
def pallindrom(number):
    """
    Функция, которая проверяет является ли
    число палиндромом. Число передаётся в качестве параметра.
    Если число палиндром нужно вернуть из функции
    true, иначе false.
    «Палиндром» — это число, у которого первая часть
    цифр равна второй перевернутой части цифр. Например,
    123321—палиндром(первая часть 123, вторая 321, которая
    после переворота становится 123), 546645 — палиндром,
    а 421987 — не палиндром.
    """
    two = number[int(len(number) // 2):]
    two = two[::-1]
    return number[:int(len(number) // 2)] == two


def generate_palindrom():
    numb_1 = [randint(1, 10) for x in range(int(90000000))]
    numb = ''
    for i in numb_1:
        numb += str(i)
    numb += numb[::-1]
    return numb


# main
def main():
    while True:
        choice = (int(input("Введите номер задания (0 для выход) - ")))
        if choice == 0:
            break
        if choice == 1:
            print(text_format.__doc__)
            print(text_format(text=str(input("Введите текст - ")), signature=str(input("Введите подпись - "))))
        if choice == 2:
            print(numbers.__doc__)
            print(numbers(numb_one=input("Введите первое число - "), numb_two=input("Введите второе число - ")))
        if choice == 3:
            print(squre.__doc__)
            side_len = input("Введите длину стороны квадрата - ")
            simbol = input("Введите символ - ")
            bool_meaning = input("y' - закрашен, в другом случае - не закрашен\n")
            squre(side_len, simbol, bool_meaning)
        if choice == 4:
            print(min_of_five.__doc__)
            n_one = input("Введите число 1 - ")
            n_two = input("Введите число 2 - ")
            n_three = input("Введите число 3 - ")
            n_foure = input("Введите число 4 - ")
            n_five = input("Введите число 5 - ")
            print(min_of_five(n_one, n_two, n_three, n_foure, n_five))
        if choice == 5:
            print(product_of_numbers.__doc__)
            print(product_of_numbers(input("Нижняя граница - "), input("Верхняя граница - ")))  # var1
            param_of_product = input("Введите нижнюю и верхнюю границы, через пробел - ").split()  # var2
            print(product_of_numbers_2(param_of_product))
        if choice == 6:
            print(main_less_6.__doc__)
            main_less_6()
        if choice == 7:
            print(pallindrom.__doc__)
            print(pallindrom('123321'))  # input("Введите число для проверки на Палиндром - ")
            start_time = time.time()
            numb = generate_palindrom()
            numb = pallindrom(numb)
            end_time = time.time()
            print(numb, end_time - start_time)


if __name__ == "__main__":
    main()