from random import randint


# Задание №1
def lesson_one():
    def sorted_func_of_less(list1):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(list1) - 1):
                if list1[i] > list1[i + 1]:
                    list1[i], list1[i + 1] = list1[i + 1], list1[i]
                    swapped = True
        return list1

    def merge_sort(my_list):
        print(f'\nНеотсортированный список: \n{my_list}')
        if len(my_list) <= 1:
            return my_list
        len_sort_part = len(my_list) // 3
        arithm_meen = sum(my_list) / len(my_list)
        print('\nСреднеарифметическое =', arithm_meen)
        if arithm_meen > 0:
            print('Срденеарифметическое > 0. Сортируем первые 2/3 списка')
            sorted_my_list = sorted_func_of_less(my_list[:len_sort_part * 2]) + my_list[:len_sort_part * 2 - 1:-1]
            return f'\nОтсортированный список: {sorted_my_list}\n'
        else:
            print('Срденеарифметическое < 0. Сортируем первую 1/3 списка')
            sorted_my_list = sorted_func_of_less(my_list[:len_sort_part]) + my_list[:len_sort_part - 1:-1]
            return f'\nОтсортированный список: \n{sorted_my_list}\n'

    print(merge_sort([randint(-300, 300) for i in range(10)]))


# Задание №2
def lesson_two():
    def list_formation(ratings_list, n=0):
        """
        Функция выводит оценки студента
        :param ratings_list: список оценок
        :param n: порядковый номер оценки
        :return: запускает рекурсивно функцию, при помощи этого производится печать оценок
        """
        if len(ratings_list) == 0:
            return ratings_list
        else:
            print(f'Оценка № {n + 1} - {ratings_list[0]}')
            return list_formation(ratings_list[1:], n + 1)

    def formation(ratings_list):
        """
        Реализована возможность изменения оценок, после перечдачи.
        :param ratings_list: список оценок
        :return: возвращает изменный список
        """
        try:
            while True:
                n = int(input('Вы вошли в режим пересдачи. Для изменения оценок введите "1" (выход - "0") - '))
                if n == 1:
                    try:
                        print('Можно изменить оценки')
                        index_rating_list = int(input("Введите номер оценки - "))
                        rating_numb = int(input("Введите новую оценку - "))
                        ratings_list[index_rating_list - 1] = rating_numb
                        print(f'Изменения внесены')
                        return list_formation(ratings_list, n=0)
                    except Exception:
                        print("Читай внимательно")
                if n == 0:
                    break
        except Exception as e:
            print("Читай внимательно")

    def grant(ratings_list):
        """
        Функция считает есть ли у студента стипендия
        :param ratings_list: список оценок
        :return: возвращает сообщение в зависимости от среднего балла
        """
        # print(sum(ratings_list) / len(ratings_list))
        if sum(ratings_list) / len(ratings_list) >= 10.7:
            print("Степендия будет")
        else:
            print("Стипендии нет")

    def sorted_list_farmation(ratings_list):
        """
        Сортировка списка оценок по возрастанию
        :param ratings_list: список оценок
        :return: отсортированный список оценок
        """
        print("1 - сортировака по убыванию" + "\n2 - Сортировка по возрастанию")
        sort_oder = int(input("Выберите порядок сортировки - "))
        index_rating_list = [i for i in range(len(ratings_list))]
        n = dict(zip(index_rating_list, ratings_list))
        if sort_oder == 1:
            new = dict(sorted(n.items(), key=lambda x: x[1]))
        if sort_oder == 2:
            new = dict(sorted(n.items(), key=lambda x: -x[1]))
        for k, v in new.items():
            print(f'{v} - Оценка №{k + 1}')

    print("""
    Программа успеваемость:
    1. ■ Вывод оценок (вывод содержимого списка);
    2. ■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
    3. ■ Выходит ли стипендия (стипендия выходит, если средний бал не ниже 10.7);
    4. ■ Вывод отсортированного списка оценок: по возрастанию или убыванию.
        """)

    try:
        ratings_list = [int(x) for x in input("Введите оценки студента (через запятую) - ").split(', ')]
    except ValueError:
        print("Попробуй еще раз")

    while True:
        try:
            numb_less = int(input("Введите номер действия (0 - выход) - "))
            # ratings_list = ratings_list
            if numb_less == 0:
                break
            if numb_less == 1:
                list_formation(ratings_list)
            if numb_less == 2:
                formation(ratings_list)
            if numb_less == 3:
                grant(ratings_list)
            if numb_less == 4:
                sorted_list_farmation(ratings_list)
        except Exception as e:
            print(e)
            print("Попробуй еще раз")


# Задание №3
def lesson_three():
    """
    :return: Усовершенствованный метод сортировки пузырьком
    """

    def sorted_func_of_less3(list1):
        swapped = True
        steps_round = 0
        while swapped:
            swapped = False
            for i in range(len(list1) - 1):
                if list1[i] > list1[i + 1]:
                    list1[i], list1[i + 1] = list1[i + 1], list1[i]
                    swapped = True
            steps_round += 1
        return steps_round

    def sorted_func_of_less4(list2):
        swapped = True
        steps_round = 0
        while swapped:
            step = 0
            swapped = False
            for i in range(len(list2) - 1):
                if list2[i] > list2[i + 1]:
                    list2[i], list2[i + 1] = list2[i + 1], list2[i]
                    step += 1
                    swapped = True
            if step != 0:
                steps_round += 1
                continue
            else:
                break
        return steps_round

    list1 = [randint(1, 200) for i in range(10)]
    list2 = list1.copy()

    def main1(list1):
        return f'Обычный метод:\nКоличество шагов - {sorted_func_of_less3(list1)}, Список - {list1}'

    def main2(list2):
        return f'Усовершенствованный метод:\nКоличество шагов - {sorted_func_of_less4(list2)}, Список - {list2}'

    print(main1(list1))
    print(main2(list2))


def main():
    while True:
        lesson = int(input("Введите номер задания - "))
        if lesson == 1:
            lesson_one()
        if lesson == 2:
            lesson_two()
        if lesson == 3:
            lesson_three()
        if lesson <= 0 or lesson > 3:
            break


if __name__ == '__main__':
    main()
