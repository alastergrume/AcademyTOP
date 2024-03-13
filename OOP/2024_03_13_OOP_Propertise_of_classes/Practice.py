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


listHuman = [Human() for i in range(3)]
for i in range(len(listHuman)):
    print("*" * 11)
    print(f'Human{i}')
    listHuman[i].inputINFO()
    print(listHuman[i])


# human1 = Human()
# human1.inputINFO()
# print(human1)
# human2 = Human()
# human1.inputINFO()