class Programmer:
    # """
    # Рассмотрим объект «Программист», который задаётся именем, должностью и количеством отработанных часов.
    # Каждая должность имеет собственный оклад (заработную плату за час работы). В нашей импровизированной компании существуют 3 должности:
    # Junior — с окладом 10 тугриков в час;
    # Middle — с окладом 15 тугриков в час;
    # Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
    # Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю). Класс реализует следующие методы:
    # work(time) — отмечает новую отработку в количестве часов time;
    # rise() — повышает программиста;
    # info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных часов>ч. <накопленная зарплата> тгр.
    #
    # programmer = Programmer('Васильев Иван', 'Junior')
    # programmer.work(750)
    # print(programmer.info())
    # programmer.rise()
    # programmer.work(500)
    # print(programmer.info())
    # programmer.rise()
    # programmer.work(250)
    # print(programmer.info())
    # programmer.rise()
    # programmer.work(250)
    # print(programmer.info())
    # """
    def __init__(self, name, position, worked_houres=0, salary=0):
        self.name = name
        self.salary = salary
        self.position = position
        self.worked_houres = worked_houres
        self._hourly_rate = {"Junior": 10, "Middle": 15, "Senior": 20}
    def work(self, time=0):

        self.worked_houres += time
        self.salary += self._hourly_rate[self.position]*time
    def rise(self):
        print(self.position)
        if self.position == self._hourly_rate["Senior"]:
            self._hourly_rate["Senior"] += 1
        else:
            self._hourly_rate[self.position] += 5
            # if self.position ==                             # To do - Дописать логику повышения в должности
            #      self.position = self.position[i+1]
        print(self._hourly_rate["Junior"])
    def info(self):
        return (f'Имя - {self.name}, Количество отработанных часов - {self.worked_houres}, У него теперь вот столько тугриков - {self.salary}')


programmer = Programmer(name="Васильев Иван", position="Junior")
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
