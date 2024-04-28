'''
    Курс: «Введение в язык
    программирования Python
    Модуль 3. Строки. Списки. Часть 1
    Задание 1
    Пользователь вводит с клавиатуры строку. 
    Произведите поворот строк и полученный результат выведите
    на экран.
    Задание 2
    Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба
    количества на экран.
    Задание 3
    Пользователь вводит с клавиатуры строку и символ
    для поиска. Посчитайте сколько раз в строке встречается
    искомый символ. Полученное число выведите на экран.
    Задание 4
    Пользователь вводит с клавиатуры строку и слово
    для поиска. Посчитайте сколько раз в строке встречается
    искомое слово. Полученное число выведите на экран.
    Задание 5
    Пользователь вводит с клавиатуры строку, слово для
    поиска, слово для замены. Произведите в строке замену
    одного слова на другое. Полученную строку отобразите
    на экране
'''


def lessonOne(my_string):
    return f'\nВаша перевенутая строка - > {my_string[::-1]}'



def lessonTwo(my_string):
    elem_isalfa = 0
    elem_isdigit = 0
    for elem in my_string:
        if elem.isalpha():
            elem_isalfa += 1
        elif elem.isdigit():
            elem_isdigit += 1
    return f'''
Колчество букв в стрке = {elem_isalfa} 
Количество цифр в строке = {elem_isdigit} 
    '''


def lessonThree(my_string, resserv_elem):
    elem_in_string = 0
    for elem in my_string:
        if elem == resserv_elem:
            elem_in_string += 1
    return f'Знак {resserv_elem} встречается в строке - > {elem_in_string} раз'


def lessonFour(my_string, reserv_word):
    word_in_string = 0
    for word in my_string.split():
        if word == reserv_word:
            word_in_string += 1
    return word_in_string


def lessonFive(my_string, reserv_word, new_word):
    my_new_string = ''
    for word in my_string.split():
        if word == reserv_word:
            word = new_word
        my_new_string += word + ' '
    return my_new_string


my_string = input('Введите вашу строку -> ')
print(lessonOne(my_string))
print(lessonTwo(my_string))
print(lessonThree(my_string, input('Введите зарезервированный знак - > ')))
print(lessonFour(my_string, input('Введите зарезервированное слово - > ')))
print(lessonFive(my_string, reserv_word=input('Введите зарезервированное слово - > '), new_word=input('Введите слово для замены - > ')))
