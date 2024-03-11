# Классы
class Car:
    # __init__ - конструктор класса, для инициализации объектов класса
    def __init__(self, fuel, maxspeed): # Что такое self - указатель на экземпляр класса.
        self.fuel = fuel
        self.maxspeed = maxspeed

    def refuel(self, amount):
        self.fuel += amount
    def drive(self):
        if self.fuel > 0:
            print("Driving")
            self.fuel -= 1
        else:
            print("No Fuel")


# MAIN: инициализация классов, отправляются
# значения для атрибутов (переменных) классов
polo = Car(20, 185)
mini = Car(10, 170)
beetle = Car(0,150)

# вывод атрибутов объекта
print(f'Polo has {polo.fuel} of fuel')
# вызов функций объекта
polo.drive()
print(f'Polo has {polo.fuel} of fuel')

print(f'mini has {mini.fuel} of fuel')
mini.drive()
print(f'mini has {mini.fuel} of fuel')

print(f'beetle has {beetle.fuel} of fuel')
beetle.drive()
print(f'beetle has {beetle.fuel} of fuel')

beetle.refuel(20)
print(f'beetle has {beetle.fuel} of fuel')
beetle.drive()
print(f'beetle has {beetle.fuel} of fuel')

class DZmenu:
    def __init__(self, count):
        self.count = count

    def inputValue(self):
        m = input("номер задания")
        if m == 1:
            selector()
    def menu(self):
        print("Menu")
        inputValue()
    def selector(self, b):
        for i in range(b):
            print(f'{i} строка')


menu = DZmenu(3)
menu.selector(55)

