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

class Arguments:
    """
    Создайте класс Circle (окружность). Для данного
    класса реализуйте ряд перегруженных операторов:
    ■ Проверка на равенство радиусов двух окружностей (операция = =);
    ■ Сравнения длин двух окружностей (операции >, <, <=,>=);
    ■ Пропорциональное изменение размеров окружности,
    путем изменения ее радиуса (операции + - += -=).
    """

    def __init__(self, atr):
        self.atr = atr

    def __eq__(self, other):  # =
        return self.atr == other

    def __lt__(self, other):  # <
        return self.atr < other

    def __gt__(self, other):  # >
        return self.atr > other

    def __le__(self, other):  # для <=
        return self.atr <= other

    def __ge__(self, other):  # для >=
        return self.atr >= other

    # def menu(self):
    #     list_of_menu = ["Сравнить на равенство", "Меньше", "Больше", "Меньше или равно", "Больше или равно"]
    #     dict_of_menu = {list_of_menu.index(i) + 1: i for i in list_of_menu}
    #     for key, values in dict_of_menu.items():
    #         print(f'{key}: {values}')
    #     user_choice = int(input("Введите номер меню - "))


class Circle(Arguments):

    def __init__(self, radius):
        super().__init__(self)
        self.atr = radius
        self.atr = (self.atr * 2) * 3.14


class Airplane(Arguments):

    def __init__(self, type_airplane):
        super().__init__(self)
        self.atr = type_airplane
        self.dict_of_pass = {"Boing": 150, "F16": 4, "TU150": 200}
        self.atr = self.dict_of_pass[self.atr]


class Flat(Arguments):
    def __init__(self, apartmet_area):
        super().__init__(self)
        self.atr = apartmet_area
        self.apartment_price = 325
        self.apartment_cost = None
        if self.apartment_cost:
            self.atr = self.apartment_cost

    def Cost(self):
        self.apartment_cost = self.apartment_price * self.atr

    def __ne__(self, other):
        return self.atr != other
class Complex:
    def __init__(self, real, image):  # Конструктор
        self.real = real
        self.image = image

    def __add__(self, other):  # Сложение
        return Complex(self.real + other.real, self.image + other.image)

    def __sub__(self, other):  # Разность
        return Complex(self.real - other.real, self.image - other.image)

    def __mul__(self, other):  # Умножение
        return Complex(self.real * other.real - self.image * other.image,
                       self.real * other.image + self.image * other.real)

    def __truediv__(self, other):
        divisor = other.real ** 2 + other.image ** 2
        real = (self.real * other.real + self.image * other.image) / divisor
        image = (self.image * other.real - self.real * other.image) / divisor
        print(divisor, (self.real * other.real + self.image * other.image), (self.image * other.real - self.real * other.image))
        return Complex(real, image)

    def __str__(self):  # Вывод
        return f'{self.real} {"+" if self.image >= 0 else "-"} {abs(self.image)}'


def complex():
    num1 = Complex(4, 3)
    num2 = Complex(2, 6)
    print(num1 + num2)
    print("Number1 - ", num1)
    print("Number2 - ", num2)
    print("Разность - ", num1 - num2)
    print("Деление - ", num1 / num2)
    print("Сумма - ", num1 + num2)
    print("Умножение - ", num1 * num2)


complex()

circle1 = Circle(25)
circle2 = Circle(26)
print(circle1 == circle2)
print(circle1 > circle2)
print(circle1 < circle2)
print(circle1 >= circle2)
print(circle1 <= circle2)

airplanes1 = Airplane("Boing")
airplanes2 = Airplane("TU150")
print(airplanes1 == airplanes2)
print(airplanes1 > airplanes2)
print(airplanes1 < airplanes2)
print(airplanes1 >= airplanes2)
print(airplanes1 <= airplanes2)


flat1 = Flat(25)
flat2 = Flat(35)

print(f"Проверка на равенство - {flat1 == flat2}")
print(f"Проверка на неравенство - {flat1 != flat2}")
print(f"Квартира 1 дороже квартиры 2 - {flat1 > flat2}")
print(f"Квартира 2 дороже квартиры 1 - {flat1 < flat2}")

