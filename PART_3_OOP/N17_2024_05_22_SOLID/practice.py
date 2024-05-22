"""
Курс: «Введение в язык
программирования Python
Модуль 14. Solid
Тема: Solid
Задание
Создайте приложение для эмуляции работыпиццерии.
Приложение должно иметь следующую функциональность:
1. Пользователь может выбрать из пяти стандартных
рецептов пиццы или создать свой рецепт.
2. Пользователь может выбирать добавлять ли топпинги (сладкий лук, халапеньо, чили, соленный огурец,
оливки, прошутто и т.д.).
3. Информацию о заказанной пицце нужно отображать
на экран и сохранять в файл.
4. Расчет может производиться, как наличными, так и
картой.
5. Необходимо иметь возможность просмотреть количество проданных пицц, выручку, прибыль.
6. Классы приложения должны быть построены с учетом принципов SOLID и паттернов проектирования.
"""
from abc import abstractmethod
class Pizza:  # абстрактный класс
    recipte = None
    toppings = []
    @abstractmethod
    def add_reception(self, recipte):
        pass
    @abstractmethod
    def add_toping(self, toppings):
        pass

# class Pizza:  # Класс гже
#     def __init__(self):
#         self.dict_pizza = {
#             'Carbanara': ['Сыр Carbanara', 'Соус BbQ', 'Saira', 'Saira'],
#             'Rigatty': ['Сыр Riggati', 'Сыр Моцарело', 'Anchous', 'Холопенья'],
#             'Pesto': ['Тонкое тесто', 'Сыр моцарела', 'Соус песто', 'Пеперони'],
#             'Neopolitan': ['Пышное тесто', 'Сыр моцарела', 'Томаты', 'Оливки'],
#             'Calzone': ['Пышное тесто', 'Сыр моцарела', 'Сыр пармезан', 'Оливки']
#         }
#         self.toppings = []
#

class PizzaBuilder(Pizza):  # Класс для создания пицы

    def add_reception(self, recipte):
        self.recipte = recipte

    def add_toping(self, toppings):
        self.toppings.append(toppings)

class PizzaMenu:  # Класс Меню
    def __init__(self, builder):
        self.builder = builder

    def menuUser(self):
        menu = {"1": "Hello", "2": "1: Сделать из меню, 2: Собрать свою", }
        user_value_builder = int(input("Сделайте выбор по заказу - "))
        user_value_toppings = int(input("Введите количество добавок - "))
        for top in range(user_value_toppings):
            self.builder.add_toppings(input(f'{top}Введите добавку - '))

    def menuOrder(self, payment_method):
        pass



class Order:  # Класс Заказа
    def __init__(self, builder, payment_method=None):
        self.builder = builder
        self.payment_method = payment_method


class OrderHistory:  # Класс Истории заказа
    def __init__(self):
        self.orders = []
        self.revenue = 0
        self.profit = 0


    def add_order(self, order):  # Создание заказа
        self.orders.append(order)
        self.calculate_revenue(order)

    def calculate_revenue(self, order):  # Прибыль от заказов
        self.revenue += len(order.builder.toppings)*100 + 1000

    def calculate_profit(self):  # Выручка от заказов
        self.profit = self.revenue*0.2

    def view_statistic(self, order):  # Статистика заказов
        string_log = f'Заказ:{order.builder.recipte}\n, Ингридиенты:{order.builder.toppings}\n, Прибыль: {self.revenue}, Профит: {self.profit}\n, Спасибо за заказ!\n'
        return string_log

class FileHandler:  # Запись лога в файл
    file_check = 'check.txt'
    @staticmethod
    def save_order_to_file(order_statistics):  # Загрузка в файл
        file_check = 'check.txt'
        with open(file_check, "a") as f:
            f.write(order_statistics)
    @staticmethod
    def retrieve_order_from_file():  # Выгрузка из файла
        file_check = 'check.txt'
        with open(file_check, "r") as f:
            console_value = f.read()
        print(console_value)

pizzaBuilder = PizzaBuilder()
pizzamenu = PizzaMenu(pizzaBuilder)
order = Order(pizzaBuilder, None)
orderhistory = OrderHistory()
FileHandler.save_order_to_file(orderhistory.view_statistic(order))
FileHandler.retrieve_order_from_file()

# pizza = Pizza()
# menu = PizzaMenu(pizza)
# menu.menuUser()