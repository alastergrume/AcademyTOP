from random import randint

# Задание №1
def buble_sort(list1):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                swapped = True
    return list1

# Задание №2
def insert_sort(list1):
    for i in range(1, len(list1)):
        item_to_insert = list1[i]
        j = i - 1
        while j >= 0 and list1[j] > item_to_insert:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = item_to_insert
    return list1

# Задание №3
def buble_sort_separation(list1, param = None):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list1) - 1):
            if param == None:
                if list1[i] < list1[i + 1]:
                    list1[i], list1[i + 1] = list1[i + 1], list1[i]
                    swapped = True
            if param != None:
                if list1[i] > list1[i + 1]:
                    list1[i], list1[i + 1] = list1[i + 1], list1[i]
                    swapped = True
    return list1


def separation_list(list1):
    if len(list1) <= 1:
        return list1
    # Находим середину списка
    mid = len(list1) // 2
    # Сортируем и объединяем подсписки
    left_list = buble_sort_separation(list1[:mid], param=None)
    right_list = buble_sort_separation(list1[mid:], param=1)
    return left_list + right_list

# Задание №4
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_lenght, right_list_lenght = len(left_list), len(right_list)
    for i in range(left_list_lenght + right_list_lenght):
        if left_list_index < left_list_lenght and right_list_index < right_list_lenght:
            # Сравнивваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его в отсортированный список
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # если первый элемент правого списка меньше, то добавляем его в наш отсортированный список
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        # если достигнут конец левого списка, элементы правого добавляются в конец результирующего списка sorted_list
        elif left_list_index == left_list_lenght:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # если достигнут конец правого списка, элементы левого списка добавляются в конец результирующего списка sorted_list
        elif right_list_index == right_list_lenght:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def merge_sort(list1):
    # Возвращаем список, если в нем 1 элемент
    if len(list1) <= 1:
        return list1
    # Находим середину списка
    mid = len(list1) // 2
    # Сортируем и объединяем подсписки
    left_list = merge_sort(list1[:mid])
    right_list = merge_sort(list1[mid:])
    # объединяем и возвращаем один список
    return merge(left_list, right_list)

list1 = [randint(-100, 100) for i in range(13)]
print(f'\nСортировака списка целых методом пузырька:\nНеотсортированный список: {list1}\nОтсортированный список:   {buble_sort(list1)}')
list1 = [randint(-100, 100) for i in range(13)]
print(f'\nСортировака списка целых методом вставок:\nНеотсортированный список: {list1}\nОтсортированный список:   {insert_sort(list1)}')
list1 = [randint(-100, 100) for i in range(13)]
print(f'\nСортировка левой части по убыванию, правой части по возрастанию:\nНеотсортированный список: {list1}\nОтсортированный список:   {separation_list(list1)}')
list1 = [randint(-100, 100) for i in range(13)]
print(f'\nСортировка целых методом слияния:\nНеотсортированный список: {list1}\nОтсортированный список:   {merge_sort(list1)}')

