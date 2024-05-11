print("Hello World!") # Функция вывода в консоль
print(25) # передаем intetger - целочисленный тип данных
print(1.25) # передаем тип float - дробное число
print(2+2)
print("Aw"+"orld")
print(2+2, end="###") # Параметр end = default = '\n' при изменении убирает перенос
print("Я помню чудное мнгновение: \n Передо мной явилась ты... ", 235, "ghjhbsdfvfbsk") #\n Перенос строки newline
print("Я помню чудное мнгновение", "hfdkhjdf", "fkbdnfbnl", sep='-') # Заменяет пробелы, в списке, только
a=4 # переменные, ячейка данных в которых хранится информация определенного типа и определенного размера
b=5
# Основные операторы в Python
print(a+b) # сложение
print(a-b) # вычитание
print(a*b) # умножение
print(a/b) # деление
print(a//b) # деление по модулю
print(a%b) # деление по остатку
print(a**b) # возведение в степень
# Правило объёвления переменных
# Нельзя использовать имена базовых функций
var = 1
var_2 = 2
print(var, var_2)
var_3 = var + var_2
var_4 = 3
print(var_4)
var_4 = var_4 + var_3 # переменная просто перезапислась
print(var_4)
value = int(input("Введите число 1: -> "))
value2 = int(input("Введите число 2: -> "))
print(value+value2, value-value2, value*value2, value/value2,  sep='\n')