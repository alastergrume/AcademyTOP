# Задание 6
# Напишите функцию, которая проверяет является ли
# число простым. Число передаётся в качестве параметра.
# Если число простое нужно вернуть из метода true, иначе
# false.


def f(value):
    if value == 2 or value == 3 or value == 5 or value == 7:
        return True
    for i in range(2, value): # int(value**0.5)+1
        if (value % i == 0):
            return False
    return True


value = int(input(f'Введите число - '))
print(f'Результат - {f(value)}')
listvalue = [i for i in range(50)]
for i in listvalue:
    print(f'{value + i} это {f(value + i)}')