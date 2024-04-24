# Творческий шаблон Prototype
# Главная цель - сократить количество классов для приложения
# Например:

from abc import ABCMeta, abstractmethod
import copy
class Courese_PJR(metaclass=ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def cource(self):
        pass
    def get_type(self):
        return self.type
    def get_id(self):
        return self.id
    def set_id(self):
        self.id = id
    def clone(self):
        return copy.copy(self)

class Python:
    def __init__(self):
        super().__init__()
        self.type = "Python"
    def course(self):
        print("Course Python method")

class Java:
    def __init__(self):
        super().__init__()
        self.type = "Java"
    def course(self):
        print("Course Java method")

class R:
    def __init__(self):
        super().__init__()
        self.type = "R"
    def course(self):
        print("Course R method")