# Станадртные модули
import math
from platform import*

# Проходим по библиотеке math. Смотрим ее содержимое
for name in dir(math):
    print(name, end='\t')

# Библиотека, которая работает с операционной системой
for name in dir(platform):
    print(name, end='\t')

# функций у platsorm всего две,
platform(aliased = False, terse = False)
# aliased - предотвращяет показ нежелательных файлов
# terse - сокражает путь до файала
print('\n', platform(0, 1), '\n', machine(), '\n', processor())
print(system(), '\n', version())
