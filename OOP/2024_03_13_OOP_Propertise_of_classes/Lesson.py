class ExampleClass:
    counter = 0 # Глобальная переменная, которая всегда находится и её значение при предыдущем объявлении, переносится в следующий при его объявлении

    def __init__(self, val=1):
        self.__first = val
        self.__second = 0
        self.__third = 0
        ExampleClass.counter += 1

    def setSecond(self, val):
        self.__second = val

    def __str__(self):
        return f'{self.__first}, {self.__second}, {self.__third}'


example1 = ExampleClass()
example2 = ExampleClass(2)
example2.setSecond(3)
example3 = ExampleClass(4)
example3.setSecond(3)
example3.__third = 5

print(example1.__str__)  # Магический метод для строки
print(example1.__dict__)
print(example2.__dict__)  # а
print(example3.__dict__, example3.counter)
b = example3.__dict__
print("Атрибуты класса из переменной в формате словаря", b)
# Преобразование объекта в строку
print(example3)  # Здесь уже не надо указывать __str__ так как в классе явно олбъявлен метод



example1 = ExampleClass()
print(f'{example1.__dict__} {example1.counter} <- показывает сколько раз вызывается класс')
example2 = ExampleClass(2)
print(example2.__dict__, example2.counter)
example2.setSecond(3)
print(example2.__dict__, example2.counter)
example3 = ExampleClass(4)
print(example3.__dict__, example3.counter)


# преобразование объекта в строку
print(example3)

# Пример 2
class ExampleClass2:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example4 = ExampleClass2(2)
try:
    print(example4.a)
except AttributeError as e:
    print(e)
try:
    print(f'Атрибут b создан {example4.b}')
except AttributeError:
    pass
