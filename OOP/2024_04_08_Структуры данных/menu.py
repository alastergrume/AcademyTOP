class MainMenu:
    def __init__(self, class_name=None):
        self.class_name = class_name

    def menu(self):
        while True:
            item_number = 1
            for item in self.class_name:
                print(f'Класс {item_number} - {item.__class__.__name__}')
                item_number += 1
            try:
                value = int(input("Введите номер класса из меню - "))
                if value == 0:
                    break
                else:
                    choice_class = self.class_name[value - 1]
                    choice_class.menu()
            except ValueError:
                print("Введен не верный символ")
            except IndexError:
                print("Такого класса не существует")