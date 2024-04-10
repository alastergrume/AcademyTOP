import os

string = {"Type": "str", "Value": "int"}


# with open("file.txt", "w") as f:
#     f.write(repr(string))

# string2 = open("file.txt", "r",  encoding="UTF-8")
# print(repr(string2.read()))                               # TODO Прочитать, что такое repr

class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Products Details: {self.name}, price: {self.price}"


# pr = Products('aaa', 2500)
# print(pr)

# EXAMPLE
import os

class CountryDict:
    def __init__(self, user_input=0):
        self.data = {}
        self.user_input = user_input
        self.new_country = ''
        self.new_capital = ''
        self.filename = 'county_capital_data.txt'

    def add_data(self):
        self.data[self.new_country] = self.new_capital

    def remove_data(self):
        if self.new_country in self.data:
            del self.data[self.new_country]
        else:
            return f'Нет такой страны'

    def search(self):
        if self.new_country in self.data:
            return self.data[self.new_country]
        else:
            return f'Нет такой страны'

    def edit_data(self):
        if self.new_country in self.data:
            self.data[self.new_country] = self.new_capital
        else:
            return f'Страна не найдена'

    def save_data(self):
        with open(self.filename, 'w') as f:
            f.write(repr(self.data))

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.data = eval(f.read())
        else:
            return f"file not exist"
    def menu(self):
        while True:
            print("Menu\n1.Add\n2.remove\n3.searche\n4.edit\n5.save\n6.load\n7.exit")
            load_value = input("Load file? Y/N")
            self.user_input = int(input("Выбери меню - "))
            if load_value == 'Y':
                self.load_data()
            if self.user_input == 1:
                self.new_country = input('New country - ')
                self.new_capital = input('New capital - ')
                self.add_data()
            if self.user_input == 2:
                self.new_country = input('Input REMOVE country - ')
                self.remove_data()
            if self.user_input == 3:
                self.new_country = input('Input SEARCHE country - ')
                print(self.search())
            if self.user_input == 4:
                self.new_country = input('Input Country')
                self.new_capital = input('Input NEW Capital')
                self.edit_data()
            if self.user_input == 5:
                self.save_data()
            # if self.user_input == 6:
            #     self.load_data()
            if self.user_input == 7:
                break


cd = CountryDict()
cd.menu()
# cd.add_data('USA', 'Washington')
# cd.add_data('UK', 'London')
# cd.add_data('Russia', 'Moscow')
# print(cd.search('Russia'))
# cd.edit_data('USA', 'Boston')
# print(cd.search('USA'))
# cd.save_data('county_capital_data.txt')
# cd.load_data('county_capital_data.txt')
# print(cd.data)