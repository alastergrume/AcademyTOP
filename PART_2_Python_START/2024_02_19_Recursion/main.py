# ----------------- Лекция ------------------
# ---------------- Рекурсия -----------------
from random import randint


# Функция, которая вызывает сама себя - это рекурсия
# Пример для нахождеия факториала числа
def faktorial(n):
    if n == 1:
        return n
    else:
        return n * faktorial(n-1)


# n = int(input("Введите число для факториала - "))
# print(faktorial(n))

# Пример:
# Необходимо найти функцию-сумматор, передается число в интервале от 1 до n выполняется сумма

def summator(n):
    if n == 1:
        return n
    else:
        return n + summator(n-1)

# n = int(input('Введите число - '))
# print(summator(n))

# Передается список целых, необходимо почистать разность элементов с нечетным индексом.

def dissum(list1):
    if not list1:
        return 0
    else:
        if list1[0] % 2 != 0:
            return list1[0] - dissum(list1[1:])
        else:
            return dissum(list1[1:])


def diss2(list1, n):
    if n == 0:
        return 0
    else:
        if n != 1:
            if n % 2 != 0:
                return (list1[n] + diss2(list1, n-1))
            else:
                return diss2(list1, n-1)
        else:
            return diss2(list1, n-1)


list1 = [i for i in range(10)]
# print(dissum(list1))
# n = len(list1)-1
# print(diss2(list1, n))

# Числа Фиббоначи - это серия чисел, которая начинается с 0 и 1.
# Каждое последующее число будет являться суммой двух предыдущих числе.

def fibb(n):
    if n <= 1:
        return n
    else:
        return fibb(n-1) + fibb(n-2)


# n = int(input("число - "))
# print(fibb(n))