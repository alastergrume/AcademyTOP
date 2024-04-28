print('\n', """ <Через цикл for>""", '\n')

floor = 1
energy = 70
print(f'Я на {floor} этаже')
for i in range(1, 5):
    step = 0
    for j in range(1, 20):
        step += 1
        energy -= 1
        if energy == 0:
            print('мне нужно отдохнуть')
            energy += 70
    floor += 1
    print(f'Я поднялся на {floor} этаж')
print(f'Я на {floor} этаже')

print('\n', """ <Через цикл while>""", '\n')

floor = 1
energy = 70
print(f'Я на {floor} этаже')

while floor != 5:
    step = 0
    while step != 20:
        step += 1
        energy -= 1
        if energy == 0:
            print('мне нужно отдохнуть')
            energy += 70
    floor += 1
    print(f'Я поднялся на {floor} этаж')
print(f'Я на {floor} этаже')

"""Следующее задание"""

for i in range(20):
    if i%2 == 0:
        print(i)
    else:
        continue
    print(f'i - Итерация и вывод числа для проверки четности')

"""Следующее задание"""

while True:
    try:
        value = int(input('Введите положительное число = '))
        if value < 0:
            continue
        elif value > 0:
            print(f'Ваше число: {value}')
        else:
            print(f'У Вас {value}, я заканчиваю программу')
            break
    except Exception as e:
        print(str(e))
        continue


"""след"""
while True:
    line = input()
    if 11 < len(line) > 11:
        print(f'Попробуй снова')
        continue
    else:
        break

line2 = '+'
for i in range(len(line)):
    if i == 0:
        line2 += "7"
    if i == 1:
        line2 += '-'+line[i]
    elif i == 4:
        line2 += '-'+line[i]
    elif i == 7:
        line2 += '-'+line[i]
    elif i == 9:
        line2 += '-'+line[i]
    else:
        line2 += line[i]
print(line2)
