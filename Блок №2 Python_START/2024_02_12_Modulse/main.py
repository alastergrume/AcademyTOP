from sys import path
path.append('../2024_02_12_Modulse/Modules') # Этот вариант используется для того, чтобы подкючать файл вне корневой директории

from Modules.module import alpha, omega # Этот метод используется для того, чтобы

zero_list = [0 for i in range(10)]
one_list = [1 for i in range(10)]
print(alpha(zero_list))
print(omega(one_list))


