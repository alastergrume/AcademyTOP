import inspect
class Numbers:
    def __init__(self):
        self.list_of_numbers = []
        self.list_of_methods = ['inputData()', 'showListOfNumbers()']


    def inputData(self):
        while True:
            input_data = input("Введите либо одно число, либо ряд числе через пробел (exit - выход):\n")
            if input_data != 'exit':
                try:
                    self.list_of_numbers.append(int(input_data))
                    print(f'Число добавлено в список')
                except ValueError:
                    self.list_of_numbers += (input_data.split(' '))
                    print(f'Числа добавлены в список')
            else:
                break

    def del_item(self):
        pass
    def showListOfNumbers(self):
        print(self.list_of_numbers)

    def searche_item(self):
        pass

    def rewrite_item(self):
        pass
    def show_methods(self):
        method_list = sorted(Numbers.methods)
        print(method_list)
    def menu(self):
        while True:
            list_menu = [
                'Добавить новое число в список',
                'Удалить все вхождения числа из списка',
                'Показать содержимое списка',
                'Проверить есть ли значение в списке',
                'Заменить значение в списке',
                'exit - Выход'
            ]
            count = 1
            for i in list_menu:
                print(f'{count}. {i}')
                count += 1

            try:
                user_choice = int(input("Введите номер меню - "))
                if user_choice == 6:
                    break
                if user_choice == 1:
                    self.inputData()
                if user_choice == 2:
                    pass
                if user_choice == 3:
                    self.showListOfNumbers()
                if user_choice == 4:
                    pass
                if user_choice == 5:
                    self.show_methods()
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)


# numbers = Numbers()
# numbers.menu()
if __name__ == '__main__':
    numbers = Numbers()
    numbers.menu()
    # methods = list()
    # for meth in dir(numbers):
    #     # if callable(getattr(numbers, meth)):
    #
    #     methods.append(meth)
    # # print(methods)
    # method_list = inspect.getmembers(numbers, predicate=inspect.ismethod)
    # for i in method_list:
    #     print(i)
    # print(method_list)
    #
    # method_list = sorted(numbers.methods)
    # print(method_list)
    # print(Numbers.mro())