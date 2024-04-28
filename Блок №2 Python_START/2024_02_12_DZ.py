from random import random, randint  # """
import datetime

# Задание 1
# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве параметра.
# Полученный результат возвращается изфункции.
# """

def list_composition(my_int_list):
    composition_of_list = 1
    for elem in my_int_list:
        composition_of_list *= elem
    return composition_of_list

# .kalinin_sorted
def list_of_min(my_int_list):
    first_time = datetime.datetime.now()
    sorted_list = []
    for i in my_int_list:
        for j in my_int_list:
            if j > i and j not in sorted_list:
                sorted_list.append(j)
    end_time = datetime.datetime.now()

    return f'{sorted_list[0]} {end_time-first_time}'

def list_of_min_2(my_int_list):
    first_time = datetime.datetime.now()
    min_meaning = 100
    for i in my_int_list:
        if i < min_meaning:
            min_meaning = i
    end_time = datetime.datetime.now()
    return f'{min_meaning} {end_time-first_time}'


my_int_list = [randint(-999, 1000) for i in range(1, 100)]
print(list_of_min_2(my_int_list))
my_int_list = [randint(1, 1000) for i in range(1, 100000)]
print(list_of_min(my_int_list))
