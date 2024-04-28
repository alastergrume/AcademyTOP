import os

print("""
1. Практическое задание Курс: «Введение в язык программирования Python Модуль 3. Циклы. Часть 1
2. Другое задание
3. Закрыть задание
""")

def change_number(command):
    os.system(f'start cmd /c "mode 80,50 && {command}"')
    print(command)

while True:
    change_numb = input("Выберите домашнее задание - ")
    if change_numb == "1":
        change_number(command='python pz_modul_03_cikly_part_3.py')
    if change_numb == "2":
        change_number(command='python dz_modul_03_cikly_part_1.py')
    if change_numb == "3":
        break
    else:
        print("Попробуй еще раз")