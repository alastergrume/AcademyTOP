# print("Nothing\nwill work\nunless you do ")
# print('"Anyone who\n','\t','stops\n','\t'*2, 'learning is old,\n','\t'*3, 'whether at twenty or eighty"\n','\t'*10,' Henry Ford') # \t - переносит с применением TAB на n - раз
# a,b = input("Ведите целое число №1: -> "),  input("Ведите целое число №2: -> ")
# print(a + '+' + b +'='+ str(int(a) + int(b)),  a + '-' + b +'='+ str(int(a) - int(b)), a + '*' + b +'=' + str(int(a) * int(b)), sep="\n")
# a,b = input("Ведите целое число: -> "),  input("Ведите значение процента: -> ")
# print(b+"% от", a, "составит", str((int(b)/100)*int(a)))
# a,b = input("Введите длину стороны A: -> "),  input("Ведите длинну стороны B: -> ")
# print(f'Площадь прямоугольника = {int(a)*int(b)}')
# list1 = [input("Введите целое число -> ") for i in range(10)]
# value = input("Введите целое число -> ")
# for i in value:
#     print(i)
value_2 = input("Введите трехчначное число -> ")
new_value = ''
for i in value_2:
    new_value += i
    print(i, new_value)