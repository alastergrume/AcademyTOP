import math
from random import randint


# Сортировка Шелла
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


list1 = [randint(-200, 200) for i in range(100)]
print(shellsort(list1))

# Практическое задание!
# 1. Найти блин с наибольшим радиусом
# 2. Перевернуть стопку так, чтобы блин с наибольшим радиусом оказался на верху
# 3. Перевернуть всю стопку, чтобы наибольший блин остался внизу
# 4. Повторить все действия уменьшая ассортимент блинов
def pancakes_sort(arr):
    # поиск индекса блина с наибольшим радиусом
    def find_largest_index(arr,n):
        i = 0
        for j in range(n):
            if arr [j] > arr [i]:
                i=j
        return i
    # Функция переворачивания блинчиков
    def flip(arr, k):
        return arr[:k][::-1] + arr[k:]
    result = []
    n = len(arr)
    while n > 1:
        i = find_largest_index(arr, n)
        if i < n - 1:
            arr = flip(arr, i+1)
            result.append(i+1)
            arr = flip(arr, n)
            result.append(n)
        n -= 1
    return result

pancakes = [3, 5, 6, 7, 1, 5, 6, 8, 7, 2, 4]
oper = pancakes_sort(pancakes)
print("Блины:", pancakes)
print("Операции:", oper)



