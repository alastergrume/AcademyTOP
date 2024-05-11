file = 'D:/Ivan_Kalinin/Python/2024_03_04_File_system/text.txt'
file2 = 'D:/Ivan_Kalinin/Python/2024_03_04_File_system/text2.txt'
try:
    stream = open(file, mode='r', encoding='UTF-8')
    new_stream = ''
    for i in stream:
        new_stream += i
    stream_string = ''
    for i in new_stream.split(' '):
        if len(i) >= 7:
            stream_string += i + ' '
    file2 = open(file2, 'w', encoding='windows-1251')
    # for i in stream_string: # Один из возможных способов
    #     file2.write(i)
    file2.write(stream_string)
    file2.close()
    stream.close()
except Exception as exc:
    print("cannot open file", exc)

# Вариант решения Михаила
# МамаПапа\n
# мама\n
# папа\n

s = open("text.txt", mode='r')
line = s.readline()
n = 0
slova = ''
while line != '':
    for i in line:
        n += 1
        slova += i
    line = s.readline()
    if n >= 7:
        s2 = open("text2.txt", "a")
        s2.write(slova)
        s2.close()
    slova = ''
    n = 0
# 2 способ
with open("text.txt", 'r') as f1:
    with open("text2.txt", 'w') as f2:
        content = f1.read()
        words = content.split()
        for word in words:
            if len(word) >= 7:
                f2.write(word + ' ')


