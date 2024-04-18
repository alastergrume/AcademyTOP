from DZ_Classes_Objects_Part_1 import Car, Stadium, Book, newStadium

class MainMenu:
    def __init__(self, class_name=None, object_name=None):
        self.class_name = class_name
        self.object_name = object_name


    def menu(self):
        while True:
            print(f'Класс - {self.class_name}')
            print(self.object_name.menu())
            value = int(input("Введите номер из меню - "))
            if value == 0:
                break
            if value == 1:
                print(self.class_name, self.object_name)
            if value == 2:
                self.object_name.menu_SetNewData()
            if value == 3:
                self.object_name.inputData


if __name__ == "__main__":
    while True:
        print(f"1. Класс Стадион\n"
              f"2. Класс Книга\n"
              f"3. Класс Новый стадион\n"
              f"0. Выход\n")

        choice = int(input("Введите Ваш выбор - "))
        if choice == 1:
            stadium = Stadium("kn", "sdv", "sdv", "s", "s")
            menu_stadium = MainMenu("Класс - Stadium\n", stadium)
            menu_stadium.menu()
        if choice == 2:
            book = Book("kn", "sdv", "sdv", "s", "s")
            menu_book = MainMenu("Класс - Книга\n", book)
            menu_book.menu()
        if choice == 3:
            newStadium = newStadium()
            menu_newStadium = MainMenu("Новый - Стадион\n",newStadium)
            menu_newStadium.menu()
        if choice == 0:
            print("Увидимся позже")
            break



