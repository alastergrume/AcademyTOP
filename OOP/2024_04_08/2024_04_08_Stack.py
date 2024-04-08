class myQueue:
    """
    Задание 1
    Создайте класс очереди для работы с символьными значениями.
    Требуется создать реализации для операций над элементами:
    ■ IsEmpty —роверка очереди на пустоту.
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
    Задание 1
    Создайте класс очереди для работы с символьными значениями.
    Требуется создать реализации для операций над элементами:
    ■ IsEmpty —роверка очереди на пустоту.
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
        # Иницализация приоритета
        max_len = []
        if len(self.mySuperStack) > 0:
            for i in self.mySuperStack:
                max_len.append(len(i))
            max_max_len = max(max_len)
            self.priority = max_max_len
        else:
            self.priority = None
        print("Приоритет по самому длинному элементу в очереди")

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

    def InsertWithPriority(self):                           # TODO Переделать этот метод
        if len(self.mySuperStack) < self.maxsize:
            new_item = input(f'Введите элемент - ')
            self.mySuperStack.append(new_item)
            return f'New item {new_item} added in stack {self.Show()}'
        else:
            return f"Стэк полон! Добавить ничего нельзя!"

    def PullHighestPriorityElement(self):                   # TODO Переделать этот метод
        if len(self.mySuperStack) != 0:
            self.mySuperStack.pop()
            return f'"Эллемент удален {self.Show()}'
        else:
            return f'Стэк уже пустой, нечего из него удалять'

    def peak(self):                                         # TODO Переделать этот метод
        pass

    def Show(self):                                         # TODO Переделать этот метод
        if len(self.mySuperStack) == 0:
            return f"Стэк пустой - {self.mySuperStack}"
        else:
            return self.mySuperStack


myqueue2 = myQueue2()
while True:
    print("""
        1. Проверить очередь очередь на пустоту.
        2. Проверить очередь на заполнение.
        3. Добавить элемент в очередь.
        4. Удалить элемент из очереди.
        5. Отобразить все элементы очереди на экран.
    """)
    choiсe = int(input("Введите номер меню - "))
    if choiсe == 5:
        print(myqueue2.Show())
    if choiсe == 4:
        print(myqueue2.PullHighestPriorityElement())
    if choiсe == 3:
        print(myqueue2.InsertWithPriority())
    if choiсe == 2:
        print(myqueue2.IsFull())
    if choiсe == 1:
        print(myqueue2.IsEmpty())
    if choiсe == 0:
        break



Задание №3

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