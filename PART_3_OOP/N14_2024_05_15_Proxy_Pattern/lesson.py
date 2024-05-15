#pattern Proxy
import abc
import random

class Abstractclass(metaclass=abc.ABCMeta):
    # Шаблон класса для RealClass and ProxyClass
    def __init__(self):
        pass
    @abc.abstractmethod
    def sort_degits(self, reverse=False):
        pass


class RealClass(Abstractclass):
    def __init__(self):
        print("Я инициализатор RealClass()")
        self.digits = []
        for i in range(1000000):
            self.digits.append(random.random())

    def sort_degits(self, reverse=False):
        self.digits.sort()


        if reverse:
            self.digits.reverse()
            
    def __str__(self):
        print("Я RealClass()")


class ProxyClass(Abstractclass):
    ref_count = 0
    def __init__(self):
        # Метод возвращает значение именованного атрибута объекта, 
        # если атрибут не найден - возвращает значение по умолчанию
        # Параметры: object, name, default. обычно используется, когда атрибут или объект
        # являеься переменной
        if not getattr(self.__class__,'cached_object', None):
            self.__class__.cached_object = RealClass()
            print("Новый объект создан")

        else:
            print("Используется существующий")

        self.__class__.ref_count += 1
        print("Использований: ", self.__class__.ref_count)

    def sort_degits(self, reverse=False):
        print("Метод сортировки")
        print(locals().items()) 
        self.__class__.cached_object.sort_degits(reverse=reverse)

    def __del__(self):
        self.__class__.ref_count -= 1
        if self.__class__.ref_count == 0:
            print("Удалены все объекты")
            del self.__class__.cached_object
        print("ref_count: ", self.__class__.ref_count)


if __name__ == "__main__":
    proxA = ProxyClass()
    print()
    proxB = ProxyClass()
    print()
    proxC = ProxyClass()
    print()

    proxA.sort_degits(reverse=True)
    print()
    proxB.sort_degits(reverse=True)
    print()
    proxC.sort_degits(reverse=True)
    print()

    print("Delleting proxA")
    del proxA 

    print("Delleting proxB")
    del proxB 

    print("Delleting proxC")
    del proxC
