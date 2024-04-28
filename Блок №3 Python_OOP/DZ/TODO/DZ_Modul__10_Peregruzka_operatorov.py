class RealString:
    def __init__(self, some_str):
        self.some_str = some_str

    def __eq__(self, other):
        return len(self.some_str) == len(other)

    def __len__(self):
        return len(self.some_str)


# Методы опреторов сравнения
# __eq__() - для ==
# __ne__() - для !=
# __lt__() - для <
# __le__() - для <=
# __gt__() - для >
# __ge__() - для >=

# str1 = RealString("Абрикосы")
# str2 = RealString("Абрикосы")
# print(str1 == str2)

class Circle:
    """
    Создайте класс Circle (окружность). Для данного
    класса реализуйте ряд перегруженных операторов:
    ■ Проверка на равенство радиусов двух окружностей (операция = =);
    ■ Сравнения длин двух окружностей (операции >, <, <=,>=);
    ■ Пропорциональное изменение размеров окружности,
    путем изменения ее радиуса (операции + - += -=).
    """

    def __init__(self, radius):
        self.radius = radius
        self.lenght_circle = (self.radius * 2) * 3.14

    def __eq__(self, other):
        return self.radius == other

    def __lt__(self, other):  # <
        return self.lenght_circle < other

    def __gt__(self, other):  # >
        return self.lenght_circle > other

    def __le__(self, other):  # для <=
        return self.lenght_circle <= other

    def __ge__(self, other):  # для >=
        return self.lenght_circle >= other


circle1 = Circle(18)
circle2 = Circle(19)
print("Сравнение на равенство = ", circle1 == circle2)
if circle1 > circle2:
    print(f'Длинна окружности {circle1.lenght_circle} больше {circle2.lenght_circle}')
else:
    print(f'Длинна окружности {circle1.lenght_circle} меньше {circle2.lenght_circle}')
print("Сравнение на меньше = ", circle1 < circle2)
print("Сравнение на больше или равно = ", circle1 >= circle2)
print("Сравнение на меньше или равно = ", circle1 <= circle2)
