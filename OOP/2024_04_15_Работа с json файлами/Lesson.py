# Работа JSON в Python
import datetime
import json

data = {"name": "jane", "age": 27, "city": "Perm"}
# Преобразование объекта Python в Строку Json
print(data)
print(type(data))
json_data = json.dumps(data, indent=4, sort_keys=True)
print(json_data)
print(type(json_data))

# dumps - преобразует словарь в строку в форме json
# indent - параметр отступа в строке
# sort_keys - сортировка ключей в json

json_data = '{"name": "jane", "age": 27, "city": "Perm"}'
data = json.loads(json_data)
print(data)
print(type(data))
print(data['name'])
### Запись контейнера JSON в файл
with open('data.json', 'w') as file:
    json.dump(data, file)
### Передача данных из файла JSON
with open('data.json', 'r') as file:
    data = json.load(file)

print('Передача данных из файла JSON -', data)

# Параметр Default
import datetime


def datetime_serializer(x):  # Без этой фукнции json  не сможет отработать вложенную в него функцию
    # isinstance - проверяет существование объекта в классах, объявленных в python
    if isinstance(x, datetime.datetime):
        return datetime.date.today().isoformat()
        # return x.strftime('%Y-%m-%d')


data = {"name": "jane", "age": 27, "city": "Perm", "birthday": datetime.datetime.now()}
json_data = json.dumps(data, indent=4, default=datetime_serializer)
print(json_data)


# Пользовательский класс

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Способ первый
def person_to_dict(person):
    return {"name": person.name, "age": person.age}


# Способ второй
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return {"name": person.name, "age": person.age}
        return super().default(o)


person = Person("Юра", 33)
print(json.dumps(person, default=person_to_dict, ensure_ascii=False))
print(json.dumps(person, cls=JSONEncoder, ensure_ascii=False))

# параметр skipkays
data = {(1, 2): "tuple_key", "normal_key": "value"}
print(json.dumps(data,
                 skipkeys=True))  # , skipkeys=True Необходимо для обработки исключений при использовании ключей, которые по типу не проходят сериализацию


class Article:
    """Создайте класс Статья. Необходимо хранить следующую информацию:
    ■ название статьи,
    ■ автор статьи,
    ■ количество знаков,
    ■ название издания или сайта,где статья была впервые опубликована,
    ■ краткое описание.
    Создайте необходимые методы для этого класса.
    """

    def __init__(self):
        self.article_dict = []

    def formate_dict(self):
        item_list = ['name', 'autor', 'count_item', 'site', 'description']
        my_dict = {k: f'{input(f"input {k} - ")}' for k in item_list}
        self.article_dict.append(my_dict)
        # print(self.article_dict)

    def Show(self):
        print(self.article_dict)

    def load_json(self):
        pass

artcile = Article()


def main():
    while True:
        print("1 - внести словарь, 2 - вывести словарь, 3 - Exite")
        choice = int(input("Input your choice"))
        if choice == 1:
            artcile.formate_dict()
        if choice == 2:
            artcile.Show()
        if choice == 3:
            break

if __name__ == "__main__":
    main()