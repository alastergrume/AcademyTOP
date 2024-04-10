class myQueue:
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
            return f'Стэк содержит {len(self.mySuperStack)} элементов.'

    def IsFull(self):
        if len(self.mySuperStack) == self.maxsize:
            return "Стек полон!"
        else:
            return f'В стеке ещё поместится {self.maxsize - len(self.mySuperStack)} элементов.'

    def Enqueue(self):
        if len(self.mySuperStack) < self.maxsize:
            new_item = input(f'Введите элемент - ')
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


# myqueue2 = myQueue()
# while True:
#     print("""
#         1. Проверить очередь очередь на пустоту.
#         2. Проверить очередь на заполнение.
#         3. Добавить элемент в очередь.
#         4. Удалить элемент из очереди.
#         5. Отобразить все элементы очереди на экран.
#     """)
#     choiсe = int(input("Введите номер меню - "))
#     if choiсe == 5:
#         print(myqueue2.Show())
#     if choiсe == 4:
#         print(myqueue2.Dequeue())
#     if choiсe == 3:
#         print(myqueue2.Enqueue())
#     if choiсe == 2:
#         print(myqueue2.IsFull())
#     if choiсe == 1:
#         print(myqueue2.IsEmpty())
#     if choiсe == 0:
#         break


class myQueue2:
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
            return f'Стэк содержит {len(self.mySuperStack)} элементов.'

    # INFO: 2 проверка очереди на заполнение
    def IsFull(self):
        if len(self.mySuperStack) == self.maxsize:
            return "Стек полон!"
        else:
            return f'В стеке ещё поместится {self.maxsize - len(self.mySuperStack)} элементов.'

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
            info_del_item = [f'Индекс - {self.index_max_item}', f'Элемент - {self.mySuperStack[self.index_max_item]}']
            self.mySuperStack.pop(self.index_max_item)
            return f'"Элемент {info_del_item} удален'
        if len(self.mySuperStack) == 1:
            info_del_item = [x for x in self.mySuperStack]
            self.mySuperStack.pop()
            return f'"Элемент {info_del_item} удален'
        else:
            return f'Стэк уже пустой, нечего из него удалять'

    # INFO: возврат самого большого по приоритету элемента
    def Peak(self):
        if len(self.mySuperStack) != 0:
            return self.Priority()
        else:
            return self.IsEmpty()

    # INFO: Показывает стэк
    def Show(self):
        if len(self.mySuperStack) == 0:
            return f"Стэк пустой - {self.mySuperStack}"
        else:

            return f"Cтэк {self.mySuperStack}"


# myqueue2 = myQueue2()
# while True:
#     print("""
#         1. Проверить очередь очередь на пустоту.
#         2. Проверить очередь на заполнение.
#         3. Добавить элемент в очередь.
#         4. Удалить элемент из очереди.
#         5. Отобразить элемент с самым высоким приоритетом в стэке
#         6. Отобразить все элементы очереди на экран.
#     """)
#     try:
#         choice = int(input("Введите номер меню - "))
#         if choice == 6:
#             print(myqueue2.Show())
#         if choice == 5:
#             print(myqueue2.Peak())
#         if choice == 4:
#             print(myqueue2.PullHighestPriorityElement())
#         if choice == 3:
#             print(myqueue2.InsertWithPriority())
#         if choice == 2:
#             print(myqueue2.IsFull())
#         if choice == 1:
#             print(myqueue2.IsEmpty())
#         if choice == 0:
#             break
#     except ValueError:
#         print("Попробуй ещё раз")
#
#
#
# # TODO Сделать третье задание

# TODO закончить третье задание
class loging_app:

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

    pass

# TODO Переделать потом в класс меню
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
                self.object_name.inputData()

# if __name__ == "__main__":
#     menu = MainMenu()
#     menu.menu()
