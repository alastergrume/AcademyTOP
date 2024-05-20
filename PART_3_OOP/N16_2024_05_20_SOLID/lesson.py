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


obj = ConsoleOutput("some string")
obj.display()
obj2 = FileOutput("some string")
obj2.display()

"""
Следующий принцип, замщения Лисков 
"""

