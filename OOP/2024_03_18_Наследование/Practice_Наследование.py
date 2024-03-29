
class Car:
    def __init__(self, namemodel, manufacture, year, color, price, engine_amount):
        self.namemodel = namemodel
        self.year = year
        self.manufacture = manufacture
        self.color = color
        self.price = price
        self.engine = engine_amount

    def getInput(self): # Внесение всей информации
        self.manufacture = input("Введите название производителя")
        self.namemodel = input("Введите название модели")
        self.color = input("Введите цвет")
        self.engine = input("Введите объем двигателя")
        self.year = input("Введите год выпуска")
        self.price = input("Введите цену")
        print(f'Операция выполнена!\n {"*" * 11}')

    def setInput(self, valeInput): # Изменение информации
        if valeInput == 1:
            self.manufacture = input("Введите название производителя")
        if valeInput == 2:
            self.namemodel = input("Введите название модели")
        if valeInput == 3:
            self.color = input("Введите цвет")
        if valeInput == 4:
            self.engine = input("Введите объем двигателя")
        if valeInput == 5:
            self.year = input("Введите год выпуска")
        if valeInput == 6:
            self.price = input("Введите цену")
        print(f'Операция выполнена!\n {"*" * 11}')

    def __str__(self): # Выводит информацию
        return f'''
Производитель: {self.manufacture}
Название модели: {self.namemodel}
Цвет: {self.namemodel}
Объём двигателя: {self.engine}
Год выпуска: {self.year}
Цена: {self.price}
'''

    def menu(self): # Функция меню
        return f'''
1. Посмотреть Информацию
2. Дополнить информацию
3. Изменить всю информацию
0. Выход'''

    def menuInput(self): # Меню для выбора полей для изменения
        print(f'''
1. Производитель: 
2. Название модели: 
3. Цвет: 
4. Объём двигателя: 
5. Год выпуска: 
6. Цена: 
''')
        valueinput = int(input("Ваш выбор СЭР - "))
        self.setInput(valueinput)


auto = Car('Boomer', 'BMW', '2023', 'red', '10 000 000', '3.5')
while True:
    print(auto.menu())
    value = int(input("Введите номер из меню - "))
    if value == 0:
        break
    if value == 1:
        print(auto)
    if value == 2:
        auto.menuInput()
    if value == 3:
        auto.getInput()

print("See you soone")
