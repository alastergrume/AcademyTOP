from random import randint

orel = 0
reshka = 0
rebro = 0
range_monet = 0
while (range_monet < 200):
    a = randint(0, 2)
    if a == 0:
        orel += 1
    elif a == 1:
        reshka += 1
    elif a == 2:
        rebro += 1
    range_monet += 1
print(f'orel {orel}')
print(f'reshka {reshka}')
print(f'reshka {rebro}')
print(f'veroyatnost {orel / 200}')
print(f'range_monet {orel + reshka + rebro}')
if (orel + reshka + rebro) == 200:
    print(f'Проверка выполнена')
else:
    print('проверка не выполнена')
