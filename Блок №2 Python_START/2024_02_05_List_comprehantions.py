import random

# --------------- Лекция --------------------
# -----------Генераторы списка---------------
mass = []
# mass = [(условие) (цикл)]
mass = [i*i for i in range(10)] # генератор
print(mass)
list1 = ["a", "b", "c", "d", "e", "f", "g"]
list2 = [i+" - буква" for i in list1] # Для поиска буквы в list1
print(list2)
list3 = [0 for i in range(10)] # Для обнуления списка

customers = ["Anna", "Bob", "Max", "Nick", "Bob", 'Joe']
cust = [i for i in customers if i !="Bob" and i != "Joe"]
print(cust)
list4 = [x*y for x in range(10) for y in range(10)]
list5 = [[x*y for x in range(10)] for y in range(10)]
print(list4)
print(list5)
# print(list5[5][6])
# list11 = [1, 2, 3, 4, 5]
# list22 = [10, 11, 12, 13]
# list33 = [[list11[i] * list22[j] for i in range(len(list11))] for j in range(len(list22))]
# print(list33)

# -------------------- Практика ---------------------
# -------- Модуль 3. Строки. Списки. Часть 3--------------

# """
# Задание №1
#     В списке целых, заполненном случайными числами
# вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и
# максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.

    # """
# my_list = [random.randint(-20, 20) for i in range(20)]
# print(f'Сгенерированный список случайных числе от -20 до 20 = {my_list}')
# # №1
# negative_sum = [i for i in my_list if i < 0]
# print(f'Сумма отричцательных чисел в списке случайных числе {sum(negative_sum)}')
# # проверка дедовским методом
# # neg = 0
# # for i in my_list:
# #     if i < 0:
# #         neg += int(i)
# # print(neg)
#
# #2
# even_sum = [i for i in my_list if i % 2 == 0]
# print(f'Сумма четных чисел = {sum(even_sum)}')
#
# #3
# # odd_sum = [i for i in my_list if i % 2 != 0]
# # print(f'Сумма неченых числе = {sum(odd_sum)}')
# # 4
# my_list = [random.randint(-20, 20) for i in range(20)]
# print(my_list)
# prod1 = 1
# prod_elements = [my_list[i] for i in range(len(my_list)) if i % 3 == 0 and i != 0]
# print(prod_elements)
# for i in prod_elements:
#     prod1 *= i
# print(f'Произведение числе индекс которых кратен 3 prod1 = {prod1}')
# 
# prod_elements2 = [i for i in range(len(my_list)) if i % 3 == 0 and i != 0]
# print(prod_elements2)
# prod = 1
# for j in prod_elements2:
#     for i in range(len(my_list)):
#         if i == j:
#             prod *= my_list[i]
# print(f'Произведение числе индекс которых кратен 3 prod2 = {prod}')









# my_list3 =[]
# for i in range(len(my_list)):
#     if my_list[i] % 3 == 0:
#         my_list3 += int(i)
# print(my_list3)




