def priority(mySuperStack):
    max_len = []
    if len(mySuperStack) > 0:
        for i in mySuperStack:
            max_len.append(len(i))
        max_max_len = max(max_len)
        priority = max_max_len
        index_max_item = max_len.index(priority)
    else:
        priority = None
    # print("Приоритет по самому длинному элементу в очереди")
    return priority, index_max_item


def InsertWithPriority(mySuperStack, maxsize=20):
    if len(mySuperStack) < maxsize:
        new_item = input(f'Введите элемент - ')
        mySuperStack.append(new_item)
        return f'New item {new_item} added in stack {mySuperStack}'
    else:
        return f"Стэк полон! Добавить ничего нельзя!"


def Show(mySuperStack):
    if len(mySuperStack) == 0:
        return f"Стэк пустой - {mySuperStack}"
    else:
        print(f"Приоритет элемента в стэке - {priority()}")
        return mySuperStack


mySuperStack = ['input()', 'fvsdv', 'lm;lkmnds;fbknn;dfbn;dnfb' ,'sv']
print(priority(mySuperStack))
# print(InsertWithPriority(mySuperStack))
