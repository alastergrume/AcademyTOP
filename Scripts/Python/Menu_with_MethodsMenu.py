class MethodSort(type):

    def __new__(meta, name, bases, dct):
        methods = [name for name in dct if callable(dct[name]) and not name.startswith('__') and not name.startswith(
            '_') and not name == 'menu']
        dct['_methods'] = sorted(methods, key=lambda x: list(dct.keys()).index(x))
        return super().__new__(meta, name, bases, dct)

class MainMenu:
    _instance = None


    def __init__(self, class_name=None):
        if not MainMenu._instance:
            print("__init__ method called..")
        else:
            print("Instance already created", self.getInstance())
        self.class_name = class_name
        self.method_list = None

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
                    self.method_list = choice_class._methods
                    print(self.method_list)
                    self.methodsMenu(choice_class)
            except ValueError:
                print("Введен не верный символ")
            except IndexError:
                print("Такого класса не существует")

    def methodsMenu(self, choice_class):
        while True:
            print('Выбран Класс')
            list_menu = [
                '1. Добавить нового пользователя',
                '2. Удалить существующего пользователя',
                '3. Проверить существует ли пользователь',
                '4. Изменить логин существующего пользователя',
                '5. Изменить пароль существующего пользователя',
                '0. Выход'
            ]
            count = 1
            print('-' * 30, sep='\n')
            for i in list_menu:
                print(f'{count}. {i}')
                count += 1
            print('-' * 30, sep='\n')

            user_choice = int(input("Введите метод - "))
            if user_choice == count - 1:
                break
            choice_method = self.method_list[user_choice - 1]
            func = getattr(choice_class, choice_method)
            func()


#TODO: Нужно настроить отправку наименований методов выбранного класса

#INFO Настроено так чтобы, сначало был выбор классов, затем выбор методов класса. Для правильной работы нужно импортировать
#INFO модули, затем в каждом классе настроить наследование следующим образом - class MyClass(metaclass=MethodSort):