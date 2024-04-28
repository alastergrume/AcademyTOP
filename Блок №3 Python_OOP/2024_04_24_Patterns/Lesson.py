# Творческий шаблон Prototype
# Главная цель - сократить количество классов для приложения
# Например:
# Сначала мы делаем 3 класса, которые собираются классом Courese_PJR, эти классы храняться в классе Courses_cache и потом инициализируются из него.
# Как бы создается копия.

from abc import ABCMeta, abstractmethod
import copy
class Courese_PJR(metaclass=ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass
    def get_type(self):
        return self.type
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def clone(self):
        return copy.copy(self)

class Python(Courese_PJR):
    def __init__(self):
        super().__init__()
        self.type = "Python"
    def course(self):
        return "Course Python method"

class Java(Courese_PJR):
    def __init__(self):
        super().__init__()
        self.type = "Java"
    def course(self):
        return "Course Java method"

class R(Courese_PJR):
    def __init__(self):
        super().__init__()
        self.type = "R"
    def course(self):
        return "Course R method"


class Courses_cache:
    cache = {}

    @staticmethod
    def get_course(sid):
        COURSE = Courses_cache.cache.get(sid, None)
        return COURSE.clone()

    @staticmethod
    def load():
        my_Python = Python()
        my_Python.set_id("1")
        Courses_cache.cache[my_Python.get_id()] = my_Python

        my_Java = Java()
        my_Java.set_id("2")
        Courses_cache.cache[my_Java.get_id()] = my_Java

        my_R = R()
        my_R.set_id("3")
        Courses_cache.cache[my_R.get_id()] = my_R


# if __name__ == "__main__":
#     Courses_cache.load()
#     print(Courses_cache.cache)
#
#     myPython = Courses_cache.get_course('1')
#     print(myPython.course())
#
#     myJava = Courses_cache.get_course('2')
#     print(myJava.course())
#
#     myR = Courses_cache.get_course('3')
#     print(myR.course())


# Абстрактные методы (собачки)

import abc
# Подключаем класс abc, вызываем методы через @abstractmethod
class Shape(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @abc.abstractmethod
    def area(self):
        pass
    def print_point(self):
        print(f'X: {self.x}, Y: {self.y}')
class Rectange(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x,y)
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

rect = Rectange(5, 4, 10,20)
print(rect.area())


"""
@staticmethod - используется для создания метода, который ничего не знает о классе или экземпляре
, через который он был вызван. Он может передавать и получать аргументы, без неявного определения через наследование.
По-человечески: обычый метод внутри класса, который может быть вызван без создания объекта класса
"""
class Name:
    @staticmethod
    def print_name():
        print("Static method")


if __name__ == "__main__":
    Name.print_name()




#Паттерн Command
from sys import stdout as console

class SessionClosed(Exception):
    def __init__(self, value):
        self.value = value


# Интрефейс программы
class Command:
    def execute(self):
        raise NotImplementedError()
    def cancel(self):
        raise NotImplementedError()
    def name(self):
        raise NotImplementedError()

# Команда rm

class ReCommand(Command):
    def execute(self):
        console.write('You are executed \"rm \"rm command \n ')
    def cancel(self):
        console.write('You are executed \"rm \"rm command \n ')
    def name(self):
        return "rm"

# Команда uptime
class UptimeCommand(Command):
    def execute(self):
        console.write('You are executed \"rm \"rm command \n ')
    def cancel(self):
        console.write('You are executed \"rm \"rm command \n ')
    def name(self):
        return "rm"


# Команда UNDO
class UndoCommand(Command):
    def execute(self):
        try:
            cmd = HISTORY.pop()
            TRASH.append(cmd)
            console.write("Undo command \" {0} \" \n".format(cmd.name()))
            cmd.cancel()
        except IndexError:
            console.write("ERROR: HISTORY is empty \n")

    def name(self):
        return "undo"
# Команда redo
class RedoCommand(Command):
    def execute(self):
        try:
            cmd = HISTORY.pop()
            TRASH.append(cmd)
            console.write("Undo command \" {0} \" \n".format(cmd.name()))
            cmd.cancel()

        except IndexError:
            console.write("ERROR: HISTORY is empty \n")
    def name(self):
        return "redo"

# Команда History
class HistoryCommand(Command):
    def execute(self):
        i=0
        for cmd in HISTORY:
            console.write("{0}: {1}\n".format(i, cmd.name()))

    def name(self):
        print("History")

# Комманда excite
class ExitCommand(Command):
    def execute(self):
        raise SessionClosed("Goodbye!")
    def name(self):
        return "exit"

COMMANDS = {"rm":ReCommand(), "uptime": UptimeCommand(), "UNDO": UndoCommand(), "redo": RedoCommand(), "History": HistoryCommand(), "exite": ExitCommand()}

HISTORY = list()
TRASH = list()

def main():
    try:
        while True:
            console.flush()
            console.write("pysh>> ")
            cmd = input()
            try:
                command = COMMANDS[cmd]
                command.execute()
                if not isinstance(command, UndoCommand) and not isinstance(command, HistoryCommand):
                    TRASH = list()
                    HISTORY.append(command)
            except KeyError:
                console.write("ERROR: HISTORY is empty \n")
    except SessionClosed as e:
        console.write(e.value)

if __name__ == "__main__":
    main()
