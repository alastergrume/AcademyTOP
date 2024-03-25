class Soda:
    """
    Класс Soda определяет тип газированной воды.
    Принимает 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду)
    Реализован метод show_my_drink(), выводит на печать "Газировака и {добавка}"
    в случае наличия добавки, а иначе отображается фраза: Обычная газировка
    """

    def __init__(self, supplement=None):
        if isinstance(supplement, str):
            self.supplement = supplement
        else:
            self.supplement = None

    def show_my_drink(self):
        if self.supplement:
            print(f'Газировка и {self.supplement}')
        else:
            print(f'Обычная газировка')


soda = Soda()
soda.show_my_drink()


class TriangleChecker:
    """
    Задание 2.
    Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
    Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
    С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
    – Ура, можно построить треугольник!;
    – С отрицательными числами ничего не выйдет!;
    – Нужно вводить только числа!;
    – Жаль, но из этого треугольник не сделать.
    ***Построить треугольник из отрезков можно лишь в одном случае: сумма длин двух любых сторон
    всегда больше третьей.
    """
    def __init__(self, number1=None, number2=None, number3=None):
        self.type_number = False
        if type(number1)== int or type(number2)  == int or type(number3) == int:
             if number1 > 0 and number2 > 0 and number3 > 0:
                self.number1 = number1
                self.number2 = number2
                self.number3 = number3
             else:
                self.number1 = None
                self.number2 = None
                self.number3 = None
        else:
            self.type_number = True

    def is_triangle(self):
        if self.type_number:
            return f'Нужно вводить только числа'
        else:
            if (self.number1 == None) or (self.number2 == None) or (self.number3 == None):
                return f'С отрицательными числами ничего не выйдет'
            if (self.number1 + self.number2) < self.number3 or (self.number2+self.number3) < self.number1 or (self.number1 + self.number3) < self.number2:
                return f'Из этого построить нельзя'
            else:
                return f'Ура, можно построить треугольник!'

Tryangel = TriangleChecker(2, 2, 3)
print(Tryangel.is_triangle())


class Nikola:
    __slot__ = ["name", "age"]
    def __init__(self, name="Николай", age=27):
        self.name = name
        self.age = age
        if self.name == "Николай":
            print(f'Меня зовут {self.name} мне {self.age} лет')
        else:
            print(f'Я не {self.name}, а Николай, и тебе {self.age} лет')


NameNikola = Nikola("Максим", 18)
NameNikola

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

str1 = RealString("Абрикосы")
str2 = RealString("Абрикосы")
print(str1 == str2)







