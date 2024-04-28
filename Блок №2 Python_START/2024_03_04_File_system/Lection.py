# Работа с файлами

file = 'D:/Ivan_Kalinin/Python/2024_03_04_File_system/text.txt'  # Объявление путей должно начинаться с C:/dir/file
# Создание потока для открытия файлов и сохранение содержимого файла в переменную stream
string = ''
try:
    stream = open(file, mode='r', encoding=None)

    # r - чтение
    # w - запись
    # a - редактирование/дозапись
    # r+: чтение и дополнение
    # w+: запись и обновление

    for i in stream:
        string += i
    print(f"Простой способ\nСтроки в файле\n{string}")
    # Закрытие потока (его нужно закрывать всегда)
    stream.close()
except Exception as exc:
    print("cannot open file", exc)

# Так тоже будет работать. Но явное указание в коде черевато потерей безопасности, если вдруг ссылка должны быть
# в скрытой папке
print('=' * 10)
string = ''
try:
    file = open('D:/Ivan_Kalinin/Python/2024_03_04_File_system/text.txt', mode='r',
                encoding=None)  # Объявление путей должно начинаться с C:/dir/file
    # Создание потока для открытия файлов и сохранение содержимого файла в переменную stream

    # r - чтение
    # w - запись
    # a - редактирование/дозапись
    # r+: чтение и дополнение
    # w+: запись и обновление

    for i in file:
        string += i
    print(f"Цикл for\nСтроки в файле\n{string}")
    # Закрытие потока (его нужно закрывать всегда)
    file.close()
except Exception as exc:
    print("cannot open file", exc)
print('=' * 10)

# вариант с циклом while

try:
    # Создание потока для открытия файлов и сохранение содержимого файла в переменную stream
    stream = open('D:/Ivan_Kalinin/Python/2024_03_04_File_system/text.txt', mode='r',
                  encoding=None)  # Объявление путей должно начинаться с C:/dir/file

    ccnt = lcnt = 0
    line = stream.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = stream.readline()
    print('\nКоличество символов:', ccnt)
    print('Количество строк:', lcnt)
    print(f"Цикл while\nСтроки в файле\n{line}")
    stream.close()
# Закрытие потока (его нужно закрывать всегда)
except Exception as exc:
    print("cannot open file", exc)
print('=' * 10)

# Запись файлов
stream = open('D:/Ivan_Kalinin/Python/2024_03_04_File_system/text.txt', mode='w',encoding=None)
for i in range(10):
    s = "line #" + str(i+1) + '\n'
    for ch in s:
        stream.write(ch)

stream.close()

print('/'*20)

string = ''
stream = open('D:/Ivan_Kalinin/Python/2024_03_04_File_system/text.txt', mode='r',encoding=None)
for i in stream:
    string += i
print(f'Строки в файле:\n {string}')
stream.close()

# Функции
# file.fileno() - возвращает целочисленный декскриптор файла
# file.flush() - очищает внутренний буфер
# file.isatty() - возвращает True, если файл привязан к терминалу
# file.next() - возвращает следующую строку
# file.seek() - устнавливает текущю позицию указателя в файле
# file.seekable() - проверяет, поддерживает ли файл случайный доступ
# file.tell() - возвращает текущую позицию в файле
# file.truncate() - уменьшает размер файла, если т указана, то файл урезается на n байт, если нет, то до текущей позиции
# file.writelines() - добавляет последовательность строк файлов