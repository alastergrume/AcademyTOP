# Создание рекурсивной функции для вычисления степени числа.
import time


def degree_of_numb(numb, degree):
    if degree == 0:
        return 1
    else:
        return numb * degree_of_numb(numb, degree - 1)


# print(degree_of_numb(2, 2))

# Написание рекурсивной функции для проверки палиндрома.

def palindrom(word):
    """
    Функция принимает значение в виде строки.
    переводит все символы в нижний регистр. Производит проверку на длину, если менее 1 сbмвола
    возвращает True
    Затем сравнивает первую подстроку с последней, если они не равны возвращает False.
    Если же символы одинаковы, то возвращает функцию со срезом строки,
    без проверяемых на предыдущем этапе символов.

    """
    word = word.lower()
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return palindrom(word[1:-1])


# print(palindrom('заказ')) #True

# Реализация рекурсивной функции для вычисления факториала числа.

def faktorial(n):
    if n == 1:
        return n
    else:
        return n * faktorial(n - 1)


# print(faktorial(11)) #39916800

# Написание рекурсивной функции для вычисления чисел Фибоначчи.

def fibb(n):
    """
    Числа Фибоначчи – это ряд чисел, в котором
    каждое последующее число равно сумме двух предыдущих:

    """
    if n <= 1:
        return n
    else:
        return fibb(n - 1) + fibb(n - 2)


# print(fibb(10))

# Создание рекурсивной функции для вычисления суммы элементов списка.

def summator(list):
    sum_list = 0
    for i in list:
        sum_list += i
    return sum_list


def summator_2(list, len_list):
    if len_list == 0:
        return 0
    else:
        # Функция возвращает сумму последнего элемента списка и вызов самой себя с длиной списка,
        # уменьшенной на 1
        return list[len_list - 1] + summator_2(list, len_list - 1)


my_list = [x for x in range(100)]
# print(summator(my_list))

my_list_2 = [y for y in range(100)]
# print(summator_2(my_list_2, len_list=len(my_list_2)))


# Реализация рекурсивной функции для нахождения наибольшего общего делителя двух чисел.

def gcd_fun(one_numb, two_numb):
    if(two_numb == 0):
        return one_numb
    else:
        return gcd_fun(two_numb, one_numb % two_numb)

num = gcd_fun(one_numb=int(input("Введите первое число - ")), two_numb=int(input("Введите второе число - ")))
print(num)
