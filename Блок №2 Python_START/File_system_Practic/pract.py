def pars_bad_word():
    """
    Дан текстовый файл. Необходимо создать новый файл
    убрав из него все неприемлемые слова.
    Список неприемлемых слов находится в другом файле.

    1. Открыть file_1 на чтение
    2. Пройтись по нему циклом
    2.1 Сохранять i в переменную
    3. При прохождении сравнивать i c имеющимися в файле bad_words словами
    4. Перезаписать имеющийся файл новыми данными
    """
    with open("file_1.txt", 'r') as new_file_1:
        content = new_file_1.read()
        words = content.split()
    with open('bad_words.txt', 'r') as bad_words:
        bad1 = bad_words.readline()
        bad = bad1.strip()
        new_content = ''
        for word in words:
            if word in bad:
                continue
            else:
                new_content += word + ' '

        print(new_content)
        with open('file_2.txt', 'w') as file_2:
            file_2.writelines(new_content)


# def mihail_func():
#     s = open('file_1.txt', 'r'):
#     lines = s.readlines()


if __name__ == "__main__":
    pars_bad_word()