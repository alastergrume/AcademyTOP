from random import randint


def minElem(my_list, start):
    min_elem = int(start)
    for i in my_list:
        if i < min_elem:
            min_elem = i
    
    return f'Нахождени наименьшего числа:\nРешение функцией min() {min(my_list)},\nРешение циклом {min_elem}'



def maxElem(my_list, end):
    max_elem = int(end)
    for i in my_list:
        if i > max_elem:
            max_elem = i
    return f'Нахождение наибольшего числа:\nРешение функцией max() {max(my_list)},\nРешение циклом {max_elem}'


def negativeAmount(my_list):
    negativeElem = 0
    for i in my_list:
        if i < 0:
            negativeElem += 1
    negativeElem_comprihant = len([i for i in my_list if i < 0])
    return f'Количество отрицательных элементов в списке:\nРешение циклом - {negativeElem}\nРешение генератором списка - {negativeElem_comprihant}'

def positiveAmount(my_list):
    positiveElem = 0
    for i in my_list:
        if i > 0:
            positiveElem += 1
    positiveElemElem_comprihant = len([i for i in my_list if i > 0])
    return f'Количество положительных элементов в списке:\nРешение циклом - {positiveElem}\nРешение генратором списка - {positiveElemElem_comprihant}'

def zeroAmount(my_list):
    zeroElem = 0
    for i in my_list:
        if i == 0:
            zeroElem += 1
    zeroElem_comprihant = len([i for i in my_list if i == 0])
    return f'Количество нулевых элементов в списке:\nРешение циклом - {zeroElem}\nРешение генратором списка - {zeroElem_comprihant}'



start = randint(-5, 0)
end = randint(0, 5)
my_list = [randint(int(start), int(end)) for i in range(20)]
print(my_list)
print('\n', minElem(my_list, end))
print('\n', maxElem(my_list, start))
print('\n', negativeAmount(my_list))
print('\n', positiveAmount(my_list))
print('\n', zeroAmount(my_list))