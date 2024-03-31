# Инкапсуляция

class Phone:
    number = "111-11-11"
    def print_number(self):
        print("Phone number: ", self.number)


# my_phone = Phone()
# my_phone.print_number()

# public - нет реализации синтаксиса, по умолчанию
# protected - одно нижнее подчеркивание
# private - два нижних подчеркивания

class Phone2:
    username = "Kate"
    __how_many_times_turned_on = 0
    def call(self):
        print("Ring-Ring")
        self.__turn_on() # если эту переменную закомментировать, то она не будет выводиться
    def __turn_on(self): # метод приватный, поэтому print, или любая другая переменная, или результат выполнения может быть выведен только в случае, если он объявлен в открытом методе.
        self.__how_many_times_turned_on += 1
        print("Times was turned on:", self.__how_many_times_turned_on)


# my_phone2 = Phone2()
# my_phone2.call()
# print("The username is", my_phone2.username)

# Полиморфизм
# перегрузка методов - создание методов с одним и тем же методом, с одним и тем же именем,
# но с разными типами агументов, -> в ПАЙТОНЕ НЕ ПОДДЕРЖИВАЕТСЯ

# Полиморфизм - передача параметров и методов класса другого значения тела функции,
# что и в родительском классе для того, чтобы создать единственную сущность (метод, оператор, объект)
# для представления различных типов в различных сценариях

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'i am a cat. My name is {self.name}, I am {self.age} years old')
    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'i am a dog. My name is {self.name}, I am {self.age} years old')
    def make_sound(self):
        print("Bark")

# cat1 = Cat('Kitty', 2.5)
# dog1 = Dog("Fluffy", 4)
# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()


# пример переопределения метода (перегрузка)

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am two-dimensional shape"
    def __str__(self):
        return self.name

class Squre(Shape):
    def __init__(self, lenght):
        super().__init__("Squre") # super() - специальный метод для обращеия к классу родителю.
        self.lenght = lenght
    def area(self):
        return self.lenght**2
    def fact(self):
        return "Squares have each angle equal to 90 degrees"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return pi*self.radius**2


a = Squre(4)
b = Circle(7)
# print(20*"*", "пример", 20*"*")
# print(b, "Вывод 1")
print(b.fact(), 'Вывод два')
# print(a.fact(), 'Вывод три')
# print(b.area(), 'Вывод четыре')

