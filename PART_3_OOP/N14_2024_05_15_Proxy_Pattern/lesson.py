#pattern Proxy
import abc
import random

class Abstractclass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def sort_degits(self, reverse=False):
        pass

class RealClass(Abstractclass):
    def __init__(self) -> None:
        self.digits = []
        for i in range(1000000):
            self.digits.append(random.random())

    def sort_degits(self, reverse=False):
        self.digits.sort()


        if reverse:
            self.digits.reverse()



class ProxyClass(Abstractclass):
    ref_count = 0
    def __init__(self):
        if not getattr(self.__class__,'cached_object', None):
            self.__class__.cached_object = RealClass()
            print("Новый объекст создан")

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
            del self.__class__.ref_count
        print("ref_count: ", self.__class__.ref_count)


if __name__ == "__main__":
    proxA = ProxyClass()
    print()
    proxB = ProxyClass()
    print()
    proxC = ProxyClass()

    proxA.sort_degits(reverse=True)
    print()

    print("Delleting proxA")
    del proxA 

    print("Delleting proxB")
    del proxB 

    print("Delleting proxC")
    del proxC
