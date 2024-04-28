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
