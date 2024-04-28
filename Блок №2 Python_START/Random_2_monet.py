from random import randint

orel = 0
reshka = 0
range_monet = 0
while (range_monet < 200):
    a = randint(0, 1)
    if orel != 2:
        if a == 0:
            orel += 1
        else:
            reshka += 1
        range_monet += 1
    else:
        break
print(f'orel {orel}')
print(f'reshka {reshka}')
range_orel = 0
mat_ozhidanie = 0
while (range_orel <= orel):
    mat_ozhidanie += range_orel*((range_orel-1)/2**range_orel)
    range_orel += 1
print(mat_ozhidanie)



