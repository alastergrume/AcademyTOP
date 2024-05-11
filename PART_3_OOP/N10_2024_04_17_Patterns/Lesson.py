# Паттерны проектирования
 # Singlton - Вид паттерна, для создания одной лишь копии класса

class Singleton(object):
    def __new__(cls): # cls - это выдуманная переменная, которая придумана
        if not hasattr(cls, "instance"):                        # метод который проверяет в создаваемом классе налиичие уже объявленного объекта, метода __new__.
            cls.instance = super(Singleton, cls).__new__(cls)   # Эта строчка работает при первой инициализии, она переопределяет мтод new в случае, если он не был создан
        return cls.instance                                     # если предыдущая проверка не прошла, и объект все же создан, то возвращается ссылка на тот самый созданный метод __new__.



# s = Singleton()
# print("Объект создан", s) # Объект создан <__main__.Singleton object at 0x0000024454084A10>
#
# s1 = Singleton() # В конечнном итоге новый объект ссылается на один и тот же объект
# print("Объект Создан", s) # Объект Создан <__main__.Singleton object at 0x0000024454084A10> ячейки памяти одинаковые


"""Отложенный Singleton"""

class Singlton:
    __instance = None
    def __init__(self):
        if not Singlton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

# s = Singlton()
# print("Object created:", Singlton.getInstance())
# s1 = Singlton()


""" Моностатический синглтон """

class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 0
print("Borg objeckt 'b' :", b)
print("Borg objeckt 'b1' :", b1)
print("Borg objeckt 'b' :", b.__dict__)
print("Borg objeckt 'b1' :", b1.__dict__)


"""Синглтон и метаклассы
Метакласс - это классы, экземплярами которых являются классы - Переопределенные классы
"""
class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("Here's my int", args)
        print("")
        return type.__call__(cls, *args, **kwargs)

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4,5)

b = int(5, 6)
int(7, 8)

# Примеры использования
class HealthCheck:
    """
    Давайте рассмотрим другой сценарий, в котором мы внедряем службы проверки работоспособности (например, Nagios)
    для нашей инфраструктуры. Мы создаем класс HealthCheck, который реализован как Singleton.
    Мы также будем поддерживать список серверов, для которых должна выполняться проверка работоспособности.
    Если сервер удален из этого списка, программное обеспечение для проверки работоспособности должно обнаружить его и удалить с серверов, настроенных для проверки.

    В следующем коде объекты hc1 и hc2 являются экземплярами класса в Singleton. Серверы добавляются в инфраструктуру для проверки работоспособности с помощью метода addServer().
    В начале выполняется, итерация проверки работоспособности для этих серверов. Затем метод changeServer() удаляет последний сервер и добавляет новый.
    А затем, когда снова запускается проверка во второй итерации то используется уже измененный список серверов.
    Все это делается с Singletons. Когда серверы добавляются или удаляются, проверка работоспособности должна быть таким объектом, который знает об изменениях, внесенных в инфраструктуру:
    
    """
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []
    def addServer(self):
        self._servers.append('Server 1')
        self._servers.append('Server 2')
        self._servers.append('Server 3')
        self._servers.append('Server 4')
    def changeServer(self):
        self._servers.pop()
        self._servers.append('Server 5')

hc1 = HealthCheck()
hc2 = HealthCheck()
hc1.addServer()

print("Schedule health check for servers(1)..")
for i in range(4):
    print("Cheking ", hc1._servers[i])

hc2.changeServer()
print("Schedule health check for servers(2)..")
for i in range(4):
    print("Cheking ", hc2._servers[i])