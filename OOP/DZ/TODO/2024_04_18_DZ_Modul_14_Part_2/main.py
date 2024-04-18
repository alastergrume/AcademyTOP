class Numbers:
    def __init__(self):
        self.list_of_numbers = []

    def inputData(self):
        while True:
            input_data = input("Введите либо одно число, либо ряд числе через пробел (exit - выход):\n")
            if input_data != 'exit':
                if input_data.isdigit():
                    try:
                        self.list_of_numbers.append(int(input_data))
                        print(f'Число добавлено в список')
                    except ValueError:
                        print("Вводить нужено числа")
                else:
                    print("Можно вводить только числа")
            else:
                break

    def del_item(self):
        user_choice = input("Введите число для удаления - ")
        deleted_item = 0
        if int(user_choice) not in self.list_of_numbers:
            print(f'\n{15 * "<>"}\nТакой элемент отсутствует\n{15 * "<>"}\n')
        else:
            while int(user_choice) in self.list_of_numbers:
                self.list_of_numbers.remove(int(user_choice))
                deleted_item += 1
            print(
                f'\n{20 * "<>"}\nКоличество вхождений эллемента - {deleted_item}\nУдалеямый эллемент - {user_choice}\n{20 * "<>"}\n')

    def showListOfNumbers(self):
        print(
            f'\n{15 * "*"}\nКоличество элементов - {len(self.list_of_numbers)}\nВ памяти сейчас содержатся следующие эллементы\n{self.list_of_numbers}\n{15 * "*"}\n')

    def __searche_item(self, user_choice):
        index_list = []
        index = 0
        for i in self.list_of_numbers:
            if len(self.list_of_numbers) == 0:
                return index_list  # Возвращает пустой список индексов, если список эллементов пуст
            elif int(i) == int(user_choice):
                index_list.append(index)
            index += 1
        return index_list  # Возвращает список индексов искомых эллементов в списке

    def item_in_list(self):
        user_choice = input("Введите число для поиска - ")
        found_position = self.__searche_item(user_choice)
        if len(found_position) == 0:
            print(f'\n{30 * "<>"}\nЭллемент {user_choice} не найден\n{30 * "<>"}\n')
        else:
            print(
                f'\n{30 * "<>"}\nКоличество найденых эллементов {len(found_position)}\nИндекс найденных элементов в списке - {found_position}\n{30 * "<>"}\n')

    def rewrite_item(self):
        if len(self.list_of_numbers) == 0:
            print('Перезаписывать нечего')
        else:
            user_choice = input("Введите старое число - ")
            user_choice2 = input("Введите новое число - ")
            index_list = self.__searche_item(user_choice)
            old_index_list = index_list.copy()
            index_list.reverse()
            for i in index_list:
                self.list_of_numbers.pop(i)
            for i in old_index_list:
                self.list_of_numbers.insert(i, user_choice2)
            print(f'\nОбновленный список\n{self.list_of_numbers}\n')

    def menu(self):
        while True:
            list_menu = [
                'Добавить новое число в список',
                'Удалить все вхождения числа из списка',
                'Показать содержимое списка',
                'Проверить есть ли значение в списке',
                'Заменить значение в списке',
                'Выход'
            ]
            count = 1
            print('-' * 30, sep='\n')
            for i in list_menu:
                print(f'{count}. {i}')
                count += 1
            print('-' * 30, sep='\n')
            try:
                user_choice = int(input("Введите номер меню - "))
                if user_choice == 6:
                    break
                if user_choice == 1:
                    self.inputData()
                if user_choice == 2:
                    self.del_item()
                if user_choice == 3:
                    self.showListOfNumbers()
                if user_choice == 4:
                    self.item_in_list()
                if user_choice == 5:
                    self.rewrite_item()
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    numbers = Numbers()
    numbers.menu()
