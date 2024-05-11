from random import randint


def zvezda(n):
    if n == 1:
        return '*'
    else:
        return '* ' + zvezda(n-1)


#

def habr(my_list):
    if not my_list:
        return my_list
    else:
        return habr(my_list[:10]) + 1



print(habr([randint(1, 5) for i in range(40)]))



