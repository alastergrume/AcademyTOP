class Car:
    """
    Реализуйте класс «Автомобиль».
    Необходимо хранить в полях класса:
    название модели,
    год выпуска,
    производителя,
    объем двигателя,
    цвет машины,
    цену.
    Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
    """

    def __init__(self, namemodel, manufacture, year, color, price, engine_amount):
        self.namemodel = namemodel
        self.year = year
        self.manufacture = manufacture
        self.color = color
        self.price = price
        self.engine = engine_amount

    def getInput(self):
        self.manufacture = input("Введите название производителя")
        self.namemodel = input("Введите название модели")
        self.color = input("Введите цвет")
        self.engine = input("Введите объем двигателя")
        self.year = input("Введите год выпуска")
        self.price = input("Введите цену")
        print(f'Операция выполнена!\n {"*" * 11}')

    def setInput(self, valeInput):
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

    def __str__(self):
        return f'''
Производитель: {self.manufacture}
Название модели: {self.namemodel}
Цвет: {self.color}
Объём двигателя: {self.engine}
Год выпуска: {self.year}
Цена: {self.price}
'''

    def menu(self):
        return f'''
1. Посмотреть Информацию
2. Дополнить информацию
3. Изменить всю информацию
0. Выход'''

    def menuInput(self):
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


class Book:
    """
    Реализуйте класс «Книга». Необходимо хранить в полях класса:
    название книги,  - name_book
    год выпуска, - publish_year
    издателя, - publisher
    жанр, - genre
    автора, - author
    цену. - price
    Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
    полям через методы класса
    """

    def __init__(self, name_book=None, publish_year=None, publisher=None, genre=None, author=None, price=None):
        self.name_book = name_book
        self.publish_year = publish_year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def inputData(self):
        self.name_book = input("Введите название книги - ")
        self.publish_year = input("Введите год издания - ")
        self.publisher = input("Введите издателя - ")
        self.genre = input("Введите жанр - ")
        self.author = input("Введите автора - ")
        self.price = input("Введите цену     - ")

    def SetNewData(self, book_data_value):
        if book_data_value == 1:
            self.name_book = input("Введите название книги - ")
        if book_data_value == 2:
            self.publish_year = input("Введите год издания - ")
        if book_data_value == 3:
            self.publisher = input("Введите издателя - ")
        if book_data_value == 4:
            self.genre = input("Введите жанр - ")
        if book_data_value == 5:
            self.author = input("Введите автора - ")
        if book_data_value == 6:
            self.price = input("Введите цену - ")
        print('Succes')

    def menu_SetNewData(self):
        print(f'Что нужно изменить?\n'
              f'1. Изменить название книги\n'
              f'2. Изменить год издания\n'
              f'3. Изменить издателя\n'
              f'4. Изменить жанр\n'
              f'5. Изменить автора\n'
              f'6. Изменить цену\n')

        book_data_value = int(input(("Ваш выбор - ")))
        self.SetNewData(book_data_value)

    def __str__(self):
        return (f'Название книги - {self.name_book}\n'
                f'Год выпуска - {self.publish_year}\n'
                f'Жанр - {self.genre}\n'
                f'Автор - {self.author}\n'
                f'Цена - {self.price}\n')

    def menu(self):
        return f'1. Вывести список\n2. Внести изменения в поля\n3. Ввести информацию о книге\n4. Выход'


class Stadium:
    """Реализуйте класс «Стадион». Необходимо хранить в полях класса:
    название стадиона, 
    дату открытия, 
    страну,
    город, 
    вместимость. 
    Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
    полям через методы класса
    """

    def __init__(self, name_stadium=None, date_of_open=None, country=None, city=None, capacity=None):
        self.name_stadium = name_stadium
        self.date_of_open = date_of_open
        self.country = country
        self.city = city
        self.capacity = capacity

    def inputData(self):
        self.name_stadium = input("Введите название стадиона - ")
        self.date_of_open = input("Введите дату открытия - ")
        self.country = input("Введите страну - ")
        self.city = input("Введите город - ")
        self.capacity = input("Введите вместимость - ")

    def SetNewData(self, book_data_value):
        if book_data_value == 1:
            self.name_stadium = input("Введите название стадиона - ")
        if book_data_value == 2:
            self.date_of_open = input("Введите дату открытия - ")
        if book_data_value == 3:
            self.country = input("Введите страну - ")
        if book_data_value == 4:
            self.city = input("Введите город - ")
        if book_data_value == 5:
            self.capacity = input("Введите вместимость - ")

        print('Succes')

    def menu_SetNewData(self):
        print(f'Что нужно изменить?\n'
              f'1. Изменить название стадиона\n'
              f'2. Изменить дату открытия\n'
              f'3. Изменить страну\n'
              f'4. Изменить город\n'
              f'5. Изменить вместимость\n'
              )

        stadium_data_value = int(input(("Ваш выбор - ")))
        self.SetNewData(stadium_data_value)

    def __str__(self):
        return (f'Название стадиона - {self.name_stadium}\n'
                f'Дата открытия - {self.date_of_open}\n'
                f'Страна - {self.country}\n'
                f'Город - {self.city}\n'
                f'Вместимость - {self.capacity}\n')

    def menu(self):
        return f'1. Вывести список\n2. Внести изменения в поля\n3. Ввести информацию о стадионе\n4. Выход'


# Перегрузка класса Стадион
class newStadium(Stadium):
    def __init__(self, name_of_builder):
        super().__init__(Stadium)
        self.name_of_builder = name_of_builder

    def __str__(self):
        return (f'Имя того кто построил стадион - {self.name_of_builder}\n'
                f'Название стадиона - {self.name_stadium}\n'
                f'Дата открытия - {self.date_of_open}\n'
                f'Страна - {self.country}\n'
                f'Город - {self.city}\n'
                f'Вместимость - {self.capacity}\n')



b = newStadium("Роберт")
print(b)
b.inputData()
print(b)


# def main():
#     while True:
#         print(f'Главное меню:\n'
#               f'1. Класс Автомобиль\n'
#               f'2. Класс Книга\n'
#               f'3. Класс Стадион\n'
#               f'0. Выход')
#         input_val = int(input("Введите номер задания - "))
#         if input_val == 1:
#             auto = Car('Boomer', 'BMW', '2023', 'red', '10 000 000', '3.5')
#             while True:
#                 print("Класс Автомобиль")
#                 print(auto.menu())
#                 value = int(input("Введите номер из меню - "))
#                 if value == 0:
#                     break
#                 if value == 1:
#                     print(auto)
#                 if value == 2:
#                     auto.menuInput()
#                 if value == 3:
#                     auto.getInput()
#         if input_val == 2:
#             print("Класс Книга")
#             book = Book()
#             while True:
#                 print(book.menu())
#                 menu_value = int(input("Введите номер меню - "))
#                 if menu_value == 1:
#                     print(book)
#                 if menu_value == 2:
#                     book.menu_SetNewData()
#                 if menu_value == 3:
#                     book.inputData()
#                 if menu_value == 4:
#                     break
#         if input_val == 3:
#             print("Класс Стадион")
#             stadium = Stadium()
#             while True:
#                 print(stadium.menu())
#                 value = int(input("Введите номер из меню - "))
#                 if value == 0:
#                     break
#                 if value == 1:
#                     print(stadium)
#                 if value == 2:
#                     stadium.menu_SetNewData()
#                 if value == 3:
#                     stadium.inputData()
#         if input_val == 0:
#             break
#     print("See you soone")
#
#
# if __name__ == "__main__":
#     main()
