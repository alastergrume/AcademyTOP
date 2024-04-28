# ; '''Домашнее задание
# ; Курс: «Введение в язык программирования Python
# ; Модуль 4. Строки. Списки.
# ; Часть 2
# ; Задание 1:
# ; Пользователь вводит с клавиатуры арифметическое
# ; выражение. Например, 23+12.
# ; Необходимо вывести на экран результат выражения.
# ; В нашем примере это 35. Арифметическое выражение
# ; может состоять только из трёх частей: число, операция,
# ; число. Возможные операции: +, -,*,/
# ; Задание 2:
# ; В списке целых, заполненном случайными числами,
# ; определить минимальный и максимальный элементы,
# ; посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# ; количество нулей. Результаты вывести на экран.'''

def exercise_one(number):
    '''
    Функция принимает два целых числа и производит аррифметическую оперцаию, выбранную пльзователем
    '''
    znak = ''
    index = 0
    for i in number:
        if not i.isalpha() and not i.isdigit():
            znak = i
        if znak == '':
            index += 1
    if znak == '+':
        answer = int(number[0:index])+int(number[index+1:])       
    elif znak == '-':
        answer = int(number[0:index])-int(number[index+1:]) 
    elif znak == '*':
        answer = int(number[0:index])*int(number[index+1:]) 
    elif znak == '/':
        if int(number[index+1:]) == 0:
            return "На ноль делить нельзя"
        answer = int(number[0:index])/int(number[index+1:])
    return f'Решение через цикл for - {answer}'    
    
def exercise_two(number):
    number = number.replace(' ', '') # Избавляемся от пробелов.
    if '+' in number: # Проверка на содержание в списке указанного символа.
        number = number.split('+') # Разделение на значения в списке по указанному знаку.
        return f'Вариант решения через список - {int(number[0]) + int(number[1])}' # Возвращает соответствующее арифметическое выражение.
    elif '-' in number:
        number = number.split('-')
        return f'Вариант решения через список - {int(number[0]) - int(number[1])}'
    elif '*' in number:
        number = number.split('*')
        return f'Вариант решения через список - {int(number[0]) * int(number[1])}'
    elif '/' in number:
        number = number.split('/')
        if int(number[1]) == 0:
            return "Делить на ноль нельзя"
        else:
            return f'Вариант решения через список - {int(number[0]) / int(number[1])}'


print("Задание №1")
number = input("Введите арифметическое выражение - ")
print(exercise_one(number))
print(exercise_two(number))


