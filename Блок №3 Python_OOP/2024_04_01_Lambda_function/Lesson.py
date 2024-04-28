"""Лямбда функиця - это функция для сздания котороых используется следующий синтаксис

lambda parametes:expression  говорим lambda передаем параметр parametes и выполняем операцию :expression

Где: parametes -  переменные, через запятую
    expression - условие, в которых ельзя использовать операторы и циклы, только условные выражения, нельзя вызывать return

Результатом выполнения лямбда выражения является анонимная функция, при вызове которой вычисляются значения при указанных параметрах.

    EXAMPLE:
    №1
        x = 1
        string = lambda x: 'k' if x ==1 else 's'
        print(string)
        вывод = k
    №2
        def area(b, n):
            return 0.5 * b * h
        area(6, 5)
        area2 = lambda b,h: 0.5 * b * h
        area2(5,6)
    №3
        elements = [(2, 12, "Mg"), (1, 3, "Li"), (1, 11, "Na"), (2, 4, "Be")]
        elements.sort(key=lambda e: (e[1], e[2]))
        elements.sort(key.lambda e: e[1:3])
    """

"""Example №2"""


def area(b, h):
    return 0.5 * b * h


area(6, 5)
area2 = lambda b, h: 0.5 * b * h
print(area2(5, 6))

"""Example №3"""
elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(elements)
elements.sort(key=lambda e: (e[1], e[
    2]))  # Функция sort шагает по списку, и каждый раз берёт аргумент из ламбды. Сравнивает элементы вложенного кортежа!
print(elements)
elements.sort(key=lambda e: e[1:3])
print(elements)
elements.sort(key=lambda e: (e[2].lower(), e[1]))
print(elements)


# """Аналог lambda, которая передается в метод sort, просто передается два элемента"""
def sorted_ar(elements):
    return elements[1], elements[2]


sorted_ar(elements=[(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")])

"""Example №4"""
c = lambda x=1, y=2, z=3: x + y + z  # Работа с параметрами по умолчанию
print(c(2, 3))

"""Example №5"""

y = lambda: 2 + 3  # Аргументы указывать необязательно
print(y())

"""Работа со встроенными функциями"""
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = list(filter(lambda x: x % 3 == 0, list1))  # выводит все нечетные числа
print(list2)
# Filter всегда принимает два аргумента: функцию и список для дальнейшей работы.
list3 = list(map(lambda x: x % 3 == 0, list1))
# map - вернет значение, после выполнения проверки выражения (условия) для каждого компонента в пределах списка
print(list3)
from functools import reduce

print(reduce(lambda x, y: y - x, list1))  # reduce - выбирает в качестве аргументов списка первые 2 значения,


# выполняет операцию и возвразает значение по операции на следующий виток цикла, до заврешения списка
# reduce - сводит элементы последовательности к одному значению, принимает два аргумента: фукнцию и список
def add(x, y):
    return x + y


sum = reduce(add, list1)
print(sum)