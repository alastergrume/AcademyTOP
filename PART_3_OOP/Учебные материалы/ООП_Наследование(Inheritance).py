"В этом файле собраны примеры из Урока 10 Наследование. Исключения"


# пример вывода информации из класса
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):  # Метод призван выводить информацию из класса, без него будет выводиться
        # наименование ячейки памяти, в которой храниться класс
        return self.name + ' in ' + self.galaxy + ' Galaxy'


sun = Star("Sun", "Milky Way")
print(sun)


# Наследование классов - методы и атрибуты наследуются от классов к классу

# Данный класс является суперклассом
class Vehicle:
    pass


# Данный класс является одновременно подклассом для класса Vehicle и суперклассом для
# класса TrackedVehicle
class LandVehicle(Vehicle):
    pass


# Данный класс является подклассом для указанных выше классов и подклассов
class TrackedVehicle(LandVehicle):
    pass


# -------------- issubclass(ClassOne, ClassTwo) -
# функция, которая определяет принадлежность классов
# Функция возвращает True (Правда), если ClassOne
# является подклассом ClassTwo, в противном случае —
# False (Ложь)
# Сначала указывается подкласс, а потом уже суперкласс
print(issubclass(Vehicle, Vehicle))
print(issubclass(LandVehicle, Vehicle))
print(issubclass(TrackedVehicle, Vehicle))

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
# ---------- функция isinstance() - проверят принадлежит ли этот объект
# определенному классу или нет
# Функция возвращает True, если объект является экземпляром класса, в противном случае — False.

myVehicle = Vehicle()
myLandVehicle = LandVehicle
myTrackedVehicle = TrackedVehicle
print("Проверка isinstance -", isinstance(myVehicle, LandVehicle))
print("Цикл для определения приналежности объектов классам")
for obj in [myVehicle, myLandVehicle, myTrackedVehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()


# ------------- Оператор is - проверяет, относятся ли две переменные к одному и тому же объекту
class SampleClass:
    def __init__(self, val):
        self.val = val


ob1 = SampleClass(0) #
ob2 = SampleClass(2)
ob3 = ob1
ob3.val += 1

print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1) # Здесь доказательство того, что это один и тот же объект
print(ob1.val, ob2.val, ob3.val)

str1 = "Mary had a little "
str2 = "Mary had a little lamb"
str1 += "lamb"
print(str1)
print(str1 == str2, str1 is str2) # Здесь проверяется строка, что не является объектом.
