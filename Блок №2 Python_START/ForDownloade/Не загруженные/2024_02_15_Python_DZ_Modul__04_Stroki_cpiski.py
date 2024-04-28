from random import randint



def list_summator(ls_1, ls_2):
    list_sum = []
    while ls_1 and ls_2:
        list_sum.append(ls_1.pop(0))
        list_sum.append(ls_2.pop(0))


    return f'Объединение списков\n{sorted(list_sum)}\n'

def summator_minus(ls_1, ls_2):
    list_sum = []
    while ls_1 and ls_2:
        if ls_1[0] not in list_sum:
            list_sum.append(ls_1[0])
        if ls_2[0] not in list_sum:
            list_sum.append(ls_2[0])
        ls_1.pop(0)
        ls_2.pop(0)

    return f'Объединение списков без повторений:\n{sorted(list_sum)}\n'

def summator_plus(ls_1, ls_2):
    list_sum_3 = []
    for i in ls_1:
        for j in ls_2:
            if j == i:
                list_sum_3.append(j)
                list_sum_3.append(i)
    return sorted(list_sum_3)


    return f'Объединение списков c общими элементами:\n{list_sum}\n'

def unic_list(ls_1, ls_2):
    list_sum_3 = []
    for i in ls_1:
        if i in ls_2 or i in list_sum_3:
            continue
        else:
            list_sum_3.append(i)
    for j in ls_2:
        if j in ls_1 or j in list_sum_3:
            continue
        else:
            list_sum_3.append(j)
    return sorted(list_sum_3)

def min_max_list(ls_1, ls_2):
    list_1 = ls_1 + ls_2
    return [min(list_1), max(list_1)]


numbers_list_1 = [randint(1, 100) for x in range(10)]
numbers_list_2 = [randint(1, 100) for x in range(10)]
print(list_summator(numbers_list_1, numbers_list_2))
numbers_list_1 = [randint(1, 100) for x in range(10)]
numbers_list_2 = [randint(1, 100) for x in range(10)]
print(summator_minus(numbers_list_1, numbers_list_2))
numbers_list_1 = [randint(1, 100) for x in range(10)]
numbers_list_2 = [randint(1, 100) for x in range(10)]
print("Список с общими элементами", summator_plus(numbers_list_1, numbers_list_2), sep="\n")
numbers_list_1 = [randint(1, 100) for x in range(10)]
numbers_list_2 = [randint(1, 100) for x in range(10)]
print("Список с уникальными элементами", unic_list(numbers_list_1, numbers_list_2), sep="\n")
numbers_list_1 = [randint(1, 100) for x in range(10)]
numbers_list_2 = [randint(1, 100) for x in range(10)]
print("Список с минимальным и максимальным значениями", min_max_list(numbers_list_1, numbers_list_2), sep="\n")