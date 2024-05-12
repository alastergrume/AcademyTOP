

class MainMenu:
    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if not MainMenu._instance:
    #         MainMenu._instance = super(MainMenu, cls).__new__(cls, *args, **kwargs)
    #     return MainMenu._instance
    def __init__(self, class_name=None):
        if not MainMenu._instance:
            print("__init__ method called..")
        else:
            print("Instance already created", self.getInstance())
        self.class_name = class_name

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls.__instance = MainMenu()
        return cls._instance

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