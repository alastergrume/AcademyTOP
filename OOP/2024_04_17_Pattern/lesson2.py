# Метод абстрактной фабрики
import random


class Factory:
    def __init__(self, class_factory=None):
        self.class_factory = class_factory

    def show(self):
        show_factory = self.class_factory()
        print("name", show_factory, "\n price:", show_factory.price())


class DSA:
    def price(self):
        return 111000

    def __str__(self):
        return 'DSA'


class STL:
    def price(self):
        return 15000

    def __str__(self):
        return "STL"


class SDE:
    def price(self):
        return 8000

    def __str__(self):
        return 'SDE'


def random_factory():
    return random.choice([SDE, STL, DSA])()


factory = Factory(random_factory)


#
# for i in range(5):
#     factory.show()


# Паттерн строитель (Builder)
class Phone:
    def __init__(self):
        self.os = None
        self.camera = None
        self.battery = None
        self.screen = None

    def __str__(self):
        return f"{self.os}, {self.camera}, {self.battery}, {self.screen}"


class Phone_Builder:
    def __init__(self):
        self.phone = Phone()

    def set_os(self, os):
        self.phone.os = os
        return self

    def set_camera(self, camera):
        self.phone.camera = camera
        return self

    def set_battery(self, battery):
        self.phone.battery = battery
        return self

    def set_screen(self, screen):
        self.phone.screen = screen
        return self

    def get_phone(self):
        print(self.phone)


builder = Phone_Builder()
phone = builder.set_os("Android").set_camera("50Mp").set_battery("6000 mA").set_screen("7.7i").get_phone()

'''
Модуль 12 Патерны проектирования 
Тема: Паттерны проектирования. Часть 1
'''

'''Задание №2'''


class Ingridients:
    def __init__(self):
        self.Type_of_pasta = None
        self.Sauce = None
        self.Filling = None
        self.Additives = None

    def __str__(self):
        return f'{self.Type_of_pasta}, {self.Sauce}, {self.Filling}, {self.Additives}'


class MakePasta():
    def __init__(self):
        self.ingridientes = Ingridients()

    def Type_of_pasta(self, Type_of_pasta):
        self.ingridientes.Type_of_pasta = Type_of_pasta
        return self

    def Sauce(self, Sauce):
        self.ingridientes.Sauce = Sauce
        return self

    def Filling(self, Filling):
        self.ingridientes.Filling = Filling
        return self

    def Additives(self, Additives):
        self.ingridientes.Additives = Additives
        return self

    def get_pizza(self):
        print(self.ingridientes)


a1 = {'Carbanara': ['Carbanara', 'BbQ', 'Saira', 'Saira'],
      'Rigatty': ['Riggati', 'Moloko', 'Anchous', ''],
      'Pesto': ['Riggati', 'Bdabequ', 'Saira', 'Клюква']
      }
a2 = ["Carbanara", "Rigatty", "Pesto"]
# print(a1['Carbanara'][0])
oven = MakePasta()
# Carbanara = oven.Type_of_pasta('Carbanara').Sauce('BbQ').Filling('Saira').Additives('Saira').get_pizza()

while True:
    count = 1
    for i in a2:
        print(f'{count} - {i}')
        count+=1
    try:
        user_choice = int(input("Введите название пасты - "))
        Carbanara = oven.Type_of_pasta(a1[a2[user_choice-1]][0]).Sauce(a1[a2[user_choice-1]][1]).Filling(a1[a2[user_choice-1]][2]).Additives(a1[a2[user_choice-1]][3]).get_pizza()
    except Exception as e:
        print("Ошибка -", e)