from menu import MainMenu, MethodSort


class myQueue(metaclass=MethodSort):
    """
    Задание 1
    Создайте класс очереди для работы с символьными значениями.
    Требуется создать реализации для операций над элементами:
    ■ IsEmpty — проверка очереди на пустоту.
    ■ IsFull — проверка очереди на заполнение.
    ■ Enqueue — добавление элемента в очередь.
    ■ Dequeue — удаление элемента из очереди.
    ■ Show — отображение всех элементов очереди на экран.
    При старте приложения нужно отобразить меню с помощью,
    которого пользователь может выбрать необходимую операцию.
    """

    def __init__(self, maxsize=20):
        self.mySuperStack = []
        self.maxsize = maxsize

    def IsEmpty(self):
        if self.mySuperStack == 0:
            return "Стэк пуст!"
        else:
            return f'Стэк содержит {len(self.mySuperStack)} эллементов.'

    def IsFull(self):
        if len(self.mySuperStack) == self.maxsize:
            return "Стек полон!"
        else:
            return f'В стеке ещё поместится {self.maxsize - len(self.mySuperStack)} эллементов.'

    def Enqueue(self):
        if len(self.mySuperStack) < self.maxsize:
            new_item = input(f'Введите эллемент - ')
            self.mySuperStack.append(new_item)
            return f'New item {new_item} added in stack {self.Show()}'
        else:
            return f"Стэк полон! Добавить ничего нельзя!"

    def Dequeue(self):
        if len(self.mySuperStack) != 0:
            self.mySuperStack.pop()
            return f'"Эллемент удален {self.Show()}'
        else:
            return f'Стэк уже пустой, нечего из него удалять'

    def Show(self):
        if len(self.mySuperStack) == 0:
            return f"Стэк пустой - {self.mySuperStack}"
        else:
            return self.mySuperStack

    def menu(self):
        while True:
            print("""
                Вы вошли в класс myQueue!
                1. Проверить очередь очередь на пустоту.
                2. Проверить очередь на заполнение.
                3. Добавить эллемент в очередь.
                4. Удалить эллемент из очереди.
                5. Отобразить все эллементы очереди на экран.
                0. Выход
            """)
            choiсe = int(input("Введите номер меню - "))
            if choiсe == 5:
                print(self.Show())
            if choiсe == 4:
                print(self.Dequeue())
            if choiсe == 3:
                print(self.Enqueue())
            if choiсe == 2:
                print(self.IsFull())
            if choiсe == 1:
                print(self.IsEmpty())
            if choiсe == 0:
                break


class myQueue2(metaclass=MethodSort):
    """
    Создайте класс очереди с приоритетами для работы
    с символьными значениями.
    Требуется создать реализации для операций над элементами очереди:
    ■ IsEmpty — проверка очереди на пустоту.
    ■ IsFull — проверка очереди на заполнение.
    ■ InsertWithPriority — добавление элемента c приоритетом в очередь.
    ■ PullHighestPriorityElement - Удаление элемента с самымым высоким приоритетом из очереди.
    ■ Peek — возврат самого большого по приоритету элемента. Обращаем ваше внимание, что элемент не
    удаляется из очереди.
    ■ Show — отображение всех элементов очереди на экран.
    При показе элемента также необходимо отображать
    приоритет.
    При старте приложения нужно отобразить меню
    с помощью которого пользователь сможеть выбирать необходимую операцию
    """

    def __init__(self, maxsize=20):
        self.index_max_item = None
        self.mySuperStack = []
        self.maxsize = maxsize

    # INFO: Функция для определения приоритета
    def Priority(self):
        max_len = []
        if len(self.mySuperStack) > 0:
            for i in self.mySuperStack:
                max_len.append(len(i))
            max_max_len = max(max_len)
            self.priority = max_max_len
            self.index_max_item = max_len.index(self.priority)
        else:
            self.priority = None
        return f'Самый высокий приоритет в стеке {self.priority}, с индексом - {self.index_max_item}'

    # INFO: 1 проверка очереди на пустоту
    def IsEmpty(self):
        if self.mySuperStack == 0:
            return "Стэк пуст!"
        else:
            return f'Стэк содержит {len(self.mySuperStack)} эллементов.'

    # INFO: 2 проверка очереди на заполнение
    def IsFull(self):
        if len(self.mySuperStack) == self.maxsize:
            return "Стек полон!"
        else:
            return f'В стеке ещё поместится {self.maxsize - len(self.mySuperStack)} эллементов.'

    # INFO: 3 добавление элемента c приоритетом в очередь.
    def InsertWithPriority(self):
        if len(self.mySuperStack) < self.maxsize:
            new_item = input(f'Введите элемент - ')
            self.mySuperStack.append(new_item)
            return f'New item {new_item} added in stack\n{self.Show()}\n{self.Priority()}'
        else:
            return f"Стэк полон! Добавить ничего нельзя!"

    # INFO: 4 Удаление элемента с самымым высоким приоритетом из очереди
    def PullHighestPriorityElement(self):
        if len(self.mySuperStack) > 1:
            info_del_item = [f'Индекс - {self.index_max_item}', f'Эллемент - {self.mySuperStack[self.index_max_item]}']
            self.mySuperStack.pop(self.index_max_item)
            return f'"Эллемент {info_del_item} удален'
        if len(self.mySuperStack) == 1:
            info_del_item = [x for x in self.mySuperStack]
            self.mySuperStack.pop()
            return f'"Эллемент {info_del_item} удален'
        else:
            return f'Стэк уже пустой, нечего из него удалить'

    # INFO: возврат самого большого по приоритету элемента
    def Peak(self):
        if len(self.mySuperStack) != 0:
            return f'{self.Priority()}\nЭллемент: {self.mySuperStack[self.index_max_item]}'
        else:
            return self.IsEmpty()

    # INFO: Показывает стэк
    def Show(self):
        if len(self.mySuperStack) == 0:
            return f"Стэк пустой - {self.mySuperStack}"
        else:

            return f"Cтэк {self.mySuperStack}"

    def menu(self):
        while True:
            print("""
                Вы вошли в класс myQueue2!
                1. Проверить очередь очередь на пустоту.
                2. Проверить очередь на заполнение.
                3. Добавить элемент в очередь.
                4. Удалить элемент из очереди.
                5. Отобразить элемент с самым высоким приоритетом в стэке
                6. Отобразить все элементы очереди на экран.
                0. Выход
            """)
            try:
                choice = int(input("Введите номер меню - "))
                if choice == 6:
                    print(self.Show())
                if choice == 5:
                    print(self.Peak())
                if choice == 4:
                    print(self.PullHighestPriorityElement())
                if choice == 3:
                    print(self.InsertWithPriority())
                if choice == 2:
                    print(self.IsFull())
                if choice == 1:
                    print(self.IsEmpty())
                if choice == 0:
                    break
            except ValueError:
                print("Попробуй ещё раз")


class LogingApp(metaclass=MethodSort):
    """Задание №3
    Задание 3
    Необходимо разработать приложение, которое позволит сохранять информацию о логинах пользователей и их
    паролях. Каждому пользователю соответствует пара ло-
    ■ Добавить нового пользователя
    ■ Удалить существующего пользователя
    ■ Проверить существует ли пользователь
    ■ Изменить логин существующего пользователя
    ■ Изменить пароль существующего пользователя
    Для реализации задания обязательно используйте
    одну из структур данных. При выборе руководствуйтесь
    постановкой задачи.
    """

    def __init__(self):
        self.__article_dict = []
        self.item_list = ['login', 'password']

    def _searche_user(self, key):
        index = 0
        for i in self.__article_dict:
            if i['login'] == key:
                return self.__article_dict[index]
            index += 1

    def user_append(self):
        my_dict = {k: f'{input(f"input {k} - ")}' for k in self.item_list}
        for i in self.__article_dict:
            if i['login'] == my_dict['login']:
                return "Пользователь с таким имененем уже существует!"
        self.__article_dict.append(my_dict)
        return self.__article_dict

    def dell_user(self):
        key = input('Введите имя пользователя - ')
        index = 0
        for i in self.__article_dict:
            if i['login'] == key:
                del self.__article_dict[index]
                return "Пользователь удален"
            index += 1

    def show(self):
        key = input('Введите имя пользователя - ')
        for i in self.__article_dict:
            if i['login'] == key:
                return "Пользователь существует"
        return 'Пользователь не существует'

    def chaged_username(self):
        old_login = input("Input old loggin - ")
        for i in self.__article_dict:
            if i['login'] == old_login:
                new_login = input("Input new loggin - ")
                self._searche_user(old_login)['login'] = new_login
                return 'Имя пользователя изменено'
        return "Пользователь с таким именем не найден"

    def chaged_passwd(self):
        old_login = input("Input loggin - ")
        for i in self.__article_dict:
            if i['login'] == old_login:
                __new_password = input("Input new password - ")
                self._searche_user(old_login)['password'] = __new_password
                return "Пароль пользователя изменен"
        return "Пользователь с таким именем не найден"

    def menu(self):
        while True:
            print("""
                Вы вошли в класс LogginApp!
                1. Добавить нового пользователя
                2. Удалить существующего пользователя
                3. Проверить существует ли пользователь
                4. Изменить логин существующего пользователя
                5. Изменить пароль существующего пользователя
                0. Выход
            """)
            try:
                choice = int(input("Введите номер меню - "))
                if choice == 5:
                    print(self.chaged_passwd())
                if choice == 4:
                    print(self.chaged_username())
                if choice == 3:
                    print(self.show())
                if choice == 2:
                    print(self.dell_user())
                if choice == 1:
                    print(self.user_append())
                if choice == 0:
                    break
            except ValueError:
                print("Попробуй ещё раз")


if __name__ == "__main__":
    myqueue1 = myQueue()
    myqueue2 = myQueue2()
    logging_app = LogingApp()
    menu = MainMenu([myqueue1, myqueue2, logging_app])
    menu.menu()
    # myqueue1.menu()
    # myqueue2.menu()
    # LogingApp.menu()

    # print(menu)
    # menu.menu()
    # menu2 = MainMenu([logging_app])
    # print(menu2)
    # menu2.menu()
    # menu3 = MainMenu([myqueue1, myqueue2])
    # print(menu3)
    # menu3.menu()
