# Кортежи ()

tuple1 = tuple()

list1 = ['a', 'b', 'c']
tuple2 = tuple(list1)
tuple3 = tuple(('aa', 'bb', 'cc', 'dd'))

print(tuple3[0])

for i in tuple3:
    print(i)

# Операции с кортежами:
# len(tuple1) - длина кортежа
# all(tuple1) - Возвращает True если все элементы кортежа, оцениваются как True, Если кортеж пуст, возвращает тоже True
# any(tuple1) - проверка хотя бы одного значения как True, иначе возвращает False аналогично пустому кортежу
# # Стандратные функции
# max(tuple1)
# min(tuple1)
# sum(tuple1)
# sorted(tuple1)

# Set - Множества {}

our_set = set()
our_set2 = {0}
print(our_set, type(our_set))
# Добавлять значения во множество можно с помощью функции add()
our_set.add("tomato")
our_set2.add("potato")
print('our_set', our_set)
print('our_set2', our_set2)
# Множества можно сравнивать:
x = "tomato"
print(x in our_set)
print(x in our_set2)

# Функции множеств, проверка

print(our_set.isdisjoint(our_set2))  # Возвращает значение True, если в множестве нет общих элементов
our_set3 = our_set.union(our_set2)  # Объединяет множества
our_set.update(our_set2)  # Расширение множества
print("our_set -", our_set)
print("our_set3 -", our_set3)

# issubset() - проверка на содержание в себе другого множества
print("issubset -", our_set2.issubset(our_set3))  # Проверка 2 на содержание в 3
print("issuperset -", our_set2.issuperset(our_set3))  # Провервка 3 на содержание во 2

"----------------Практика-------------------"

our_products = {"Apple", "Tesla", "MacDonald's"}
range_of_the_company1 = {"Samsung", "Sony"}
range_of_the_company2 = {"Apple", "IBM", "Tesla"}
range_of_the_company3 = {"BMW", "Tesla", "Ferrari"}

print("intersection Предоставляет множество общих элементов(пересечение)")
print(our_products.intersection(range_of_the_company1))
print(our_products.intersection(range_of_the_company2))
print(our_products.intersection(range_of_the_company3))

print("# difference() - противоположно общим, разница множеств")
print(our_products.difference(range_of_the_company1))
print(our_products.difference(range_of_the_company2))
print(our_products.difference(range_of_the_company3))

print("# symmetric_difference() - Создает множество, которое содержит разницу двух множеств")
print(our_products.symmetric_difference(range_of_the_company1))
print(our_products.symmetric_difference(range_of_the_company2))
print(our_products.symmetric_difference(range_of_the_company3))

# intersection_update() - метод изменяет само множество
# difference_update() - метод изменяет само множество
# symmetric_difference_update() - метод изменяет само множество

# discard() - удаление элемента, может удалить не существующий элемент, ошибку выводить не будет
# remove() - удаление, не может удалить не существующий элемент, выведет ошибку

our_products.discard("Apple")
our_products.discard('Mercedes')
print(our_products)
our_products.remove("McDonald's") # Ошибка для примера
print(our_products)
our_products.remove("Mercedes")

our_products.pop()  # удаление случайного элемента

# frozenset - Неизменямый тип множеств

my_frozenset = frozenset()
