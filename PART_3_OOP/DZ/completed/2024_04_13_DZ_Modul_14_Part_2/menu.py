class MainMenu:
    _instance = None
    """
    Класс принимает список классов как аргумент.
    Выводит список классов и предоставляет возможность пользователю выбрать требуемый класс
    В модуле, содаржащем искомые классы, необходимо импортировать данный модуль,     
    from menu import MainMenu
    
    затем инициализировать класс
    menu = MainMenu([class1, class2, class3])
    
    После инициализации необходимо запустить метод menu класса MainMenu
        menu.menu()
    """

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