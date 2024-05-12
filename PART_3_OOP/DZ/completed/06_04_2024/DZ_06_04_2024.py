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

class Programmer:
    # """
    # Рассмотрим объект «Программист», который задаётся именем, должностью и количеством отработанных часов.
    # Каждая должность имеет собственный оклад (заработную плату за час работы). В нашей импровизированной компании существуют 3 должности:
    # Junior — с окладом 10 тугриков в час;
    # Middle — с окладом 15 тугриков в час;
    # Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
    # Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю). Класс реализует следующие методы:
    # work(time) — отмечает новую отработку в количестве часов time;
    # rise() — повышает программиста;
    # info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных часов>ч. <накопленная зарплата> тгр.
    #
    # programmer = Programmer('Васильев Иван', 'Junior')
    # programmer.work(750)
    # print(programmer.info())
    # programmer.rise()
    # programmer.work(500)
    # print(programmer.info())
    # programmer.rise()
    # programmer.work(250)
    # print(programmer.info())
    # programmer.rise()
    # programmer.work(250)
    # print(programmer.info())
    # """
    def __init__(self, name, position, worked_houres=0, salary=0):
        self.name = name
        self.salary = salary
        self.position = position
        self.worked_houres = worked_houres
        self._hourly_rate = {"Junior": 10, "Middle": 15, "Senior": 20}
    def work(self, time=0):

        self.worked_houres += time
        self.salary += self._hourly_rate[self.position]*time
    def rise(self):
        print(self.position)
        if self.position == self._hourly_rate["Senior"]:
            self._hourly_rate["Senior"] += 1
        else:
            self._hourly_rate[self.position] += 5
            # if self.position ==                             # To do - Дописать логику повышения в должности
            #      self.position = self.position[i+1]
        print(self._hourly_rate["Junior"])
    def info(self):
        return (f'Имя - {self.name}, Количество отработанных часов - {self.worked_houres}, У него теперь вот столько тугриков - {self.salary}')


programmer = Programmer(name="Васильев Иван", position="Junior")
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())


"""Опишите ряд классов, необходимых для реализации противников в компьютерной игре:
NPC – базовый класс
Swordsman – мечник (наследует класс NPC). Наносит случайный урон из заданного диапазона.
Mage – маг (наследует класс NPC). Наносит урон равный удвоенному количеству маны. Не может атаковать, если мана закончилась.

Пример:
Explain
Имя: Бильбо, Очки здоровья: 15
Не могу атаковать!
Имя: Гендальф, Очки здоровья: 100
Маг Гендальф нанёс 10 урона!
Имя: Арагорн, Очки здоровья: 50
Мечник Арагорн нанёс 8 урона!
Имя: Гендальф, Очки здоровья: 100
Не могу атаковать! Мана закончилась."""

class NPC: # Базовый класс
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def __str__(self):
        return f'Имя: {self.name}, Очки здоровья: {self.hp}'
    def attack(self:int):
        return f'Не могу атаковать'

class Swordsman(NPC): # Мечник

    def __init__(self, name, hp):
        super().__init__(name, hp)


class Mage(NPC): # Маг

    def __init__(self, name, hp):
        super().__init__(name, hp)


npc = NPC("Bilbo", 0)
swordsman = Swordsman("Aragorn", 10)
mage = Mage("Gendalf", 10)
print(npc)
print(npc.attack())
print(swordsman)
print(mage)
