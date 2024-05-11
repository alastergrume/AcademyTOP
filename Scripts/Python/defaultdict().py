from collections import defaultdict

'''
Автоматическое добавление ключа словарю
Уровень: #базовый

Используя модуль collections и тип данных defaultdict, можно создать 
словарь, который автоматически добавляет ключи при их обращении, 
если они еще не существуют в словаре.

В этом примере мы создаем словарь my_dict с помощью defaultdict(list), 
что означает, что при обращении к несуществующему ключу будет автоматически
создан новый элемент со значением по умолчанию, 
в данном случае - пустым списком.
'''

# Создадим defaltdict с типом list
my_dict = defaultdict(list)

# Добавление элемента в словарь
my_dict['key'].append('value')

# Вывод словаря
print(my_dict)

# Вывод: defaultdict(<class 'list'>, {'key': ['value']})

# Обращение к несуществующему ключу
print(my_dict['new_key'])  # Вывод: [] # Если элемента нет, то он добавляется в словарь

print(my_dict)
# Вывод: defaultdict(<class 'list'>, {'key': ['value'], 'new_key': []})

my_dict['new_key'].append('Learn')
# Добавление значения к элемента по ключу
print(my_dict)
# Вывод: defaultdict(<class 'list'>, {'key': ['value'], 'new_key': ['Learn']})
my_dict['new_key'].append('Glazov')
# Добавление ещё одного элемента в список к элементу словаря
print(my_dict)
# Вывод: defaultdict(<class 'list'>, {'key': ['value'], 'new_key': ['Learn', 'Glazov']})
print(my_dict['key'])
# Обращение к элементу словаря по ключу
# Вывод: ['value']

# Перебор значений по ключу элемента словаря
for item in my_dict['new_key']:
    print(item, end=' ')
# Вывод: Learn Glazov
