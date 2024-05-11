#from main import spisok # импорт глобальной переменной
# заполнение оценок
def zap(spisok):
    #global spisok # при импорте не надо объявлять переменную
    for i in range(10):
        spisok[i] = int(input(f'Введите оценку {i+1} экзамена: '))