import math
from random import randint


# Задание №1 Сортировка Шелла
def lesson_1(list1):
    print("Сортировка методом Шелла")

    def shellsort(list1):
        nlen = len(list1)
        k = int(math.log2(nlen))
        interval = 2 ** k - 1
        while interval > 0:
            for i in range(interval, nlen):
                temp = list1[i]
                j = i
                while j >= interval and list1[j - interval] > temp:
                    list1[j] = list1[j - interval]
                    j -= interval
                list1[j] = temp
            k -= 1
            interval = 2 ** k - 1
        return list1

    # list1 = [randint(-200, 200) for i in range(100)]
    print(shellsort(list1))


# Задание №2 Метод пирамиидальной сортировки
def lesson_2(list1):
    print("Пираимидальная сортировка")

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

    print(heap_sort(list1))


# Задание №3 Метод быстрой сортировки
def lesson_3(list1):
    print("Метод быстрой сортировки")

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
        return list1

    return quick_sort(list1)


# Задание №4 - Переворачивание блинчиков
def lesson_4():
    print("Переворачивание блинчиков")

    def pancakes_sort(arr):
        # поиск индекса блина с наибольшим радиусом
        def find_largest_index(arr, n):
            i = 0
            for j in range(n):
                if arr[j] > arr[i]:
                    i = j
            return i

        # Функция переворачивания блинчиков
        def flip(arr, k):
            return arr[:k][::-1] + arr[k:]

        result = []
        n = len(arr)
        while n > 1:
            i = find_largest_index(arr, n)
            if i < n - 1:
                arr = flip(arr, i + 1)
                result.append(i + 1)
                arr = flip(arr, n)
                result.append(n)
            n -= 1
        return result

    pancakes = [3, 5, 6, 7, 1, 5, 6, 8, 7, 2, 4]
    oper = pancakes_sort(pancakes)
    print("Блины:", pancakes)
    print("Операции:", oper)


print("№1 - Сортировка методом Шелла")
print("№2 - Пираимидальная сортировка")
print("№3 - Метод быстрой сортировки")
print("№4 - Переворачивание блинчиков")
print("Любое другое число - Выход")

list1 = [randint(1, 20) for i in range(20)]


def main():
    while True:
        lesson = int(input("Введите номер задания - "))
        if lesson == 1:
            lesson_1(list1)
        if lesson == 2:
            lesson_2(list1)
        if lesson == 3:
            print(lesson_3(list1))
        if lesson == 4:
            lesson_4()
        if lesson <= 0 or lesson > 4:
            break


if __name__ == '__main__':
    main()
