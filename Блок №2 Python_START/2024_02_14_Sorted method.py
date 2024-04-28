# 1 Метод пузырька
def buble_sort(list1):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                swapped = True


# 2 Метод сортировки вставками: берется первое значение сроавнивается со всеми значениями в списке.
# выбиратеся самое меньшее, и они меняются местами.
def insert_sort(list1):
    for i in range(1, len(list1)):
        item_to_insert = list1[i]
        j = i - 1
        while j >= 0 and list1[j] > item_to_insert:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = item_to_insert


# 3 Метод выборки/ Делит список на два списка, в правой отсортировано все, а с лева выбираються значения для сравнения с неотсортированным списком. Далее
# при следующих итерациях отсортированныый список уже не участвует в сравнении.

def select_sort(list1):
    for i in range(0, len(list1) - 1):
        smallist = i
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[smallist]:
                smallist = j
        list1[i], list1[smallist] = list1[smallist], list1[i]


# 4 Метод пирамидальной сортировки (сортировка кучей элементов) выполняет сегментацию списка не две части, создается дерево их чисел.

def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    # если левый потомок корня - допустимый индекс, а элемент больше, чем текущий наибольший, то обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    # Функиция вызывает сама себя, пока не выполниться условие.
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums

# 5 Метод сортировки слиянием

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


# Метод быстрой сортировки
def partition(list1, low, high):
    # выбираем средний элемент как опорный
    pivot = list1[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while list1[i] < pivot:
            i += 1
        j -= 1
        while list1[j] > pivot:
            j -= 1
        if i >= j:
            return j
        list1[i], list1[j] = list1[j], list1[i]


def quick_sort(list1):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(list1, 0, len(list1) - 1)


# мой не работающий код
# def partition(list1, low, high):
#     # выбираем средний элемент как опорный
#     pivot = list1[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while list1[i] < pivot:
#             i += 1
#         j -= 1
#         while list1[j] > pivot:
#             j -= 1
#         if i >= j:
#             return j
#         list1[i], list1[i] = list1[j], list1[i]
# def quick_sort(list1):
#     def _quick_sort(items, low, high):
#         if low < high:
#             split_index = partition(items, low, high)
#             _quick_sort(items, low, split_index)
#             _quick_sort(items, split_index + 1, high)
#     _quick_sort(list1, 0, len(list1)-1)


from random import randint

list1 = [randint(-99, 99) for i in range(30)]
# buble_sort(list1)
# list_1.sort(bubble_sort) встроенный мтеод сортировки в пайтон, тот же самый сортировка пузырьком
# insert_sort(list1)
# select_sort(list1)
print(heap_sort(list1))
# print(merge_sort(list1))
# print(quick_sort(list1))
# print(list1)
