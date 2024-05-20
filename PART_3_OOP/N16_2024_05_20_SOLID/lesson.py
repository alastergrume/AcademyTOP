# Pattern SOLID
import os.path


class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def display(self):
        print(f"{self.name}, {self.last_name}, {self.age}")

    def input_value(self):
        self.name = input("input Name - ")
        self.last_name = input("input Last Name - ")
        self.age = input("input Age - ")


# obj = User("bill", 'ozborn', 43)
# obj.display()
# obj.input_value()
# obj.display()

'''первый принцип - Защищенность данных.
для реализации данного принципа в коде выше, необходимо разбить на два класса. 
'''


class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


class Console:
    @staticmethod
    def display(obj):
        print(f"{obj.name}, {obj.last_name}, {obj.age}")

    @staticmethod
    def input_value():
        name = input("input Name - ")
        last_name = input("input Last Name - ")
        age = input("input Age - ")
        return User(name, last_name, age)


# obj = User("bill", 'ozborn', 43)
# Console.display(obj)
# obj = Console.input_value()
# Console.display(obj)

"""
Класс является контейнером каких то свойств, методов, атрибутов. А управляют им другие классы. Что является декомпозицией.

"""

"""
S - Принцип единой ответственности
необходимо распеделить задачи, организовать отдельные модули, делегирование обязанностей, вместо одного класса, 
нужно создавать вспомогательные классы или утилиты.
"""

"""# Следущий принцип
O - Принцип открытости. Классы и методы должны быть открытыми для расширения, но закрытыми для модификации.
Главное нарушение - рабочую программу модифиицруем, и программа перестает работать:"""


class Output:
    def __init__(self, data, output_type):
        self.data = data
        self.output_type = output_type

    def display(self):
        if self.output_type == 'console':
            print(f"{self.data}")
        elif self.output_type == 'file':
            file_dir = os.path.dirname(os.path.abspath(__file__))
            os.chdir(file_dir)
            with open("output_type.txt", "w") as f:
                f.write(self.data)
        else:
            raise ValueError('type output')


# obj = Output("some string", "data")
# obj.display()
# obj2 = Output("some string", "console")
# obj2.display()

"""Если модифицировать данный класс, то нам нужно будет добавлять кучу элифов, что меняет код и сама модификация является изменением
Главные принципы открытости и закрытости: Модель наследования, композиция, модель стратегия."""

import io
import os
from abc import ABC, abstractmethod


class Output(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def display(self):
        pass


class ConsoleOutput(Output):
    def display(self):
        print(self.data)


class FileOutput(Output):
    def display(self):
        with open("output_type.txt", "w") as f:
            f.write(self.data)


# obj = ConsoleOutput("some string")
# obj.display()
# obj2 = FileOutput("some string")
# obj2.display()

"""
Следующий принцип, замщения Лисков - подчеркивает, что объекты суперкласса должны заменятся объектами подкласса
"""
from typing import List


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def calculate_area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def calculate_area(self):
        return self._width * self._height


def calculate_total_area(rects: list[Rectangle]):
    total_area = 0
    for obj in rects:
        total_area += obj.calculate_area()

    return total_area


# rects = [Rectangle(5, 6), Square(10)]
# print(calculate_total_area(rects))

"""
Приводим коды выше к принципам Лисков
Данная запись позволяет наследовать классы от абстрактного класса, без опасности нанести ущерб другим классам после добавления дополнительных модулей
В случае, если нужно добавить ещё один метод, то без использования абстрактного метода необходимо будет переписывать тот класс, который использует методы
модифицируемого класса.
"""


class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


def calculate_total_area(figurse: list[Figure]):
    print(figurse)
    total_area = 0
    for obj in figurse:
        total_area += obj.calculate_area()

    return total_area


# rects = [Rectangle(5, 6), Square(10)]
# print(calculate_total_area(rects))


"""
'I' - Принцип разделения
если на сайте есть функция квадрат функции и т.д., то они распианы в разных вкладках
не должно быть такого когда при подсчете каких либо показателей, выводились ещё какие то левые данные, которые пользовтель не запрашивал
"""


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class Ostriche(Bird):
    def fly(self):
        raise Exception("Ostriche is not flying")

    def walk(self):
        print("Ostriche is walking")


class Eagle(Bird):
    def fly(self):
        print("Eagle is flying")

    def walk(self):
        print("Eagle is walking")


# try:
#     obj = Eagle()
#     obj.fly()
#     obj.walk()
#     obj2 = Ostriche()
#     obj2.walk()
#     obj2.fly()
#
#
#
# except Exception as e:
#     print(e)
#
"""
правильная реализация:
"""

class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Ostriche(Walkable):

    def walk(self):
        print("Ostriche is walking")


class Eagle(Walkable, Flyable):
    def fly(self):
        print("Eagle is flying")

    def walk(self):
        print("Eagle is walking")


try:
    obj = Eagle()
    obj.fly()
    obj.walk()
    obj2 = Ostriche()
    obj2.walk()

except Exception as e:
    print(e)


"""
Высокоуровневые уровни не должны зависеть от низкоуровневых. 
Вместо этого они должны быть завязаны на абстрактных классах
"""

class DataSource(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def read_data(self):
        pass
    @abstractmethod
    def write_data(self):
        pass

class TextDataSource(DataSource):
    def read_data(self):
        with open(self.path, 'r') as file:
            data = file.read()
        return data

    def write_data(self, data):
        with open(self.path, 'w') as file:
            file.write(data)


class DbDataSource(DataSource):
    def write_data(self, data):
        return "data from database"
    def read_data(self, data):
        print(f'write {data}')

class TextOperation:
    def __init__(self, data_source):
        self.data_source = data_source
        self.data = self.data_source.read_data()
    def searche_for_word(self, word):
        return word, self.data
    def count_ocurences(self, word):
        return self.data.count(word)

file = TextDataSource("D:\\data.txt")
db = DbDataSource("customerz")

obj = TextOperation(db)
print(obj.searche_for_word('more'))
print(obj.count_ocurences('be'))

obj = TextOperation(db)
print(obj.searche_for_word('data'))
print(obj.count_ocurences('from'))

"""Абстрагирование, Агрегация, и паттрен Адаптер"""