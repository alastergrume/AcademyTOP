print("Hello")
print(__name__)

_counter = 0

def alpha(list):
    global _counter
    _counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum


def omega(list):
    global _counter
    _counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod


if __name__ == '__main__':
    print('I prefer to be a module')
    list123 = [i + 1 for i in range(5)]
    print(alpha(list123))
    print(omega(list123))
else:
    print('I like to be a module')
