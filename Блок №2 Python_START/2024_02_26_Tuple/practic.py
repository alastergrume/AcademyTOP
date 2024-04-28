# Задание №1
def amount_fruits_in_tuple(fruits_tuple):
    print(fruits_tuple)
    fruit = input("Введите название фрукта для поиска - ")
    amount_fruit = 0
    for i in fruits_tuple:
        if i == fruit:
            amount_fruit += 1
    print(f'Фрукт {fruit} встречается в списке количество раз = {amount_fruit} ')


# Задание №2

def find_substring_in_tuple(fruits_tuple):
    fruit = 'banana'  # input("Введите искомый фрукт - ")
    amount_fruit = 0
    for i in fruits_tuple:
        if i.find(fruit) >= 0:
            amount_fruit += 1
    return amount_fruit



# Задание №3
def bla_bla_tuple_car():
    my_tuple_car = ('mersedes', 'audi', 'BMV')
    my_car_list = list(my_tuple_car)
    # zamena, prodo = input("Введите производителя - "), input("Введите марку для замены")
    prodo = 'mersedes'
    zamena = 'lada'
    new_tuple_car = []
    for i in my_car_list:
        if i != prodo:
            new_tuple_car.append(i)
        else:
            new_tuple_car.append(zamena)
    return tuple(new_tuple_car)

def


fruits_tuple = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
# print(find_substring_in_tuple(fruits_tuple))
print(bla_bla_tuple_car())