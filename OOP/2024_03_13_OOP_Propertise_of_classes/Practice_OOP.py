class Human:
    def __init__(self):
        self.date = ''
        self.fio = ''
        self.__tel = ''
        self.city = ''
        self.homeadres = ''
        self.country = ''
    def getTel(self):
        return self.__tel
    def setTel(self, tel):
        self._tel = tel
    def inputINFO(self):
        self.date = input('Введите дату рождения - ')
        self.fio = input("Введите ФИО - ")
        tel = input('Введите Телефон - ')
        self.setTel(tel)
        self.city = input('Введите Город - ')
        self.homeadres = input('Введите Домашний адрес - ')
        self.country = input('Введите Страну - ')

    def __str__(self):
        return f'\n{self.date}\n{self.fio}\n{self.getTel()}\n{self.city}\n{self.homeadres}\n{self.country}'


# listHuman = [Human() for i in range(3)]
# for i in range(len(listHuman)):
#     print("*" * 11)
#     print(f'Human{i}')
#     listHuman[i].inputINFO()
#     print(listHuman[i])


# human1 = Human()
# human1.inputINFO()
# print(human1)
# human2 = Human()
# human1.inputINFO()

class City:
    """
    Создайте класс «Город». Необходимо хранить в полях класса:
    название города, название региона, название
    страны, количество жителей в городе, почтовый индекс
    города, телефонный код города. Реализуйте методы класса
    для ввода данных, вывода данных, реализуйте доступ к
    отдельным полям через методы класса.
    """
    def __init__(self):
        self.city_name = ''
        self.region = ''
        self.country = ''
        self.populaton = ''
        self.amount_people = ''
        self.__post_index = ''
        self.__phone_code = ''

    def getInfo(self):
        return f'{self.__post_index}\n{self.__phone_code}'
    def setInput(self, post_index, phone_code):
        self.__post_index = post_index
        self.__phone_code = phone_code
    def inputInfo(self):
        self.city_name = input('Введите название города - ')
        self.region = input('Введите название региона - ')
        self.country = input('Введите название страны - ')
        self.populaton = input('Введите количество населения - ')
        post_index = input('Введите почтовый индекс - ')
        phone_code = input('Введите код города - ')
        self.setInput(post_index, phone_code)

    def __str__(self):
        return f'\n{self.city_name}\n{self.region}\n{self.country}\n{self.populaton}\n{self.getInfo()}\n'


# listCity = [City() for i in range(3)]
# for i in range(len(listCity)):
#     print('*' * 11)
#     print(f'City{i}')
#     listCity[i].inputInfo()
#     print(listCity[i])

listCity = City()
listCity.inputInfo()
print(listCity)

class Country:
    """
    Создайте класс «Страна». Необходимо хранить в
    полях класса: название страны, название континента,
    количество жителей в стране, телефонный код страны,
    название столицы, название городов страны.
    Реализуйте методы класса для ввода данных, вывода данных,
    реализуйте доступ к отдельным полям через методы класса.
    """

    def __init__(self):
        self.country = ''
        self.continent = ''
        self.amount_of_people = ''
        self.__phone_code = ''
        self.capital = ''
        self.cities = ''

    def input_fields(self): # Реализация метода ввода данных в поля класса
        self.country = input('Введите название страны - ')
        self.continent = input('Введите название континента - ')
        self.amount_of_people = input('Введите количество жителей - ')
        self.__phone_code = input('Введите телефонный код - ')
        self.capital = input('Введите название столица')
        self.cities = input('Введите названия городов')
    def __str__(self):
        return (f'{self.country}'
                f'{self.continent}'
                f'{self.amount_of_people}'
                f'{self.__phone_code}'
                f'{self.capital}'
                f'{self.cities}')


InfoCountry = Country()
InfoCountry.input_fields()
print(InfoCountry)