# ----------------------ЛЕКЦИЯ-------------------------
# '''------------------ Строки ---------------------'''
from numpy import byte

userMessage = 'Hello'
userMessageEnc = userMessage.encode("utf-8") # Кодирование в формат UTF-8
print(userMessageEnc)
print(type(userMessageEnc))
print(id(userMessageEnc))
userMessageDec = userMessageEnc.decode("utf-8") # Декодирование обратно из формата UTF-8
print(userMessageDec)
print(type(userMessageDec))
print(id(userMessageDec)) # Выводит место в ячейке процессора

myStr = "hello"
myInt = 10
print(id(myStr))
print(type(myStr))
print(myStr)
print(id(myInt))
myInt = None
print(bin(id(myInt)))
myStr = 'Hello'
myStr2 = "Hello"

print(f'{"здесь можно написать текст"}') # Пример для f-строки. В ней можно писать текст и вводить функции

# Тройные кавычки необходимы для сохранения форматирования!
myStr4=''' 
                This is a multi-line string (text). 
                This is the first line of text.
                This is the second line of text.
                This is the third line of text with 'quotes'
 '''

print(myStr4)

my_word = 'footbar'
print(my_word[-1:7])
# Конкатенация

mystr1 = "Admin"
myStr2 = mystr1 + mystr1 # Сложение строк
print(myStr2)
print(myStr*11) # Перемножение строк, выводит строку несколько раз
print(len(myStr2)) # Выводит количество симоволов в строке

# Методы изменения строк

myStr = "Python was created in the late 1980's. by Guido Van Rossum"

# Метод .capitalize()
print(myStr.capitalize()) # Переводит первый символ в верхний регистр, а все остальные в нижний регистр. Метод исполнения - копирование.
# Метод .lower()
print(myStr.lower()) # Переводит все символы в нижний регистр. Метод исполнения - копирование.
# Метод .upper()
print(str.lower(myStr)) # У класса стринг, есть метод, который применит строку
# Метод .title()
print(myStr.title()) # Каждое слове делает с большой буквы
# Метод .swapcasr()
print(myStr.swapcase()) # Обращает регистры во всех словах

# Методы поиска подстроки в строке. по простому это поиск слов в предложении.
# метод .count() Возвращает индекс фрагмента подстроки. Т.Е. количество подстрок в строке. Можно передать два параметра, начало поиска и конец.

print(myStr.count("Python", 0, 56)) #Выводит количество укзанных подстрок в строке. В данном случае выведет сколько раз встречается указаное слове в строке, а так же начало и конце поиска

print(myStr.find("p")) # Метод .find() Выводит индекс первого вхождения элемента с начала строки. Можно указать начало и конец поиска. Ищет с начала.
print(myStr.rfind("a")) # Метод .rfind() Выводит индекс первого вхождения элемента с конца строки. Если нет значения выведет -1
print(myStr.rindex("P")) # Метод .rindex() Работает как rfind, но если не будет значения, то вернет ошибку

# Методы проверки начала или конца строк. Явлаются логичесиким, возвращают булево значение

print(myStr.endswith("a")) # Метод .andswitch() Заканчивается ли строка этим символом, принимает итервалы
print(myStr.startswith("P")) # Метод .startswitch() Заканчивается ли строка этим символом, принимает интервалы

# Методы проверки строк. Они все логические
print(myStr.isalnum()) # .isalnum() В качестве параметра передается пустота. состоит ли строка из букв или цифр
print(myStr.isalpha()) # .isalpha() Состоит ли строка только из букв
print(myStr.isdigit()) # .isdigit() Состоит ли строка только из цифр
print(myStr.islower()) # .islower() Состоит ли строка только символов нижнего регистра
print(myStr.isupper()) # .isupper() Состоит ли строка только из символов верхнего регистра
print(myStr.isspace()) # .isspace() Проверка на пробелы и табуляцию
print(myStr.istitle()) # .istitle() Начинается ли каждое последовательность символа после спецсимвола (пробела или переноса строки) с большой буквы

# методы формирования строк
mystr = "Python\t\t33"
print(mystr.center(33, "$"))  #Расширяет строку слева и справа указанными символами до указаного значения
print(mystr.center(33))  #Расширяет строку слева и справа пустотой до указаного значения
print(mystr.expandtabs(tabsize=4)) #Вставляет табы к имеющейся табуляции и переносам, по умолчанию 8 табов
print(mystr.ljust(30, '@')) #выравнивание по левому краю
print(mystr.rjust(30, "@")) #выравнивает по правому краю
a = (mystr.rjust(30, "@"))
print(a.ljust(60, '*')) # Применение нескольких методов одновременно

mystr = "             Python33                "
print(mystr.lstrip()) # Удаление символов слева в данном случае пробелы
print(mystr.rstrip()) # Удаление символов справа в данном случае пробелы
print(mystr.strip()) # Удаление симоволов со всех сторон в данном случае пробелы

mystr = "Python33"
print(mystr.zfill(25)) #Метод дополняет строку слева символами ноль на то количество, которое указано.