# Структуры данных

#  bytearray
a=bytearray((12,7,5,3,5))
print(a)
print(a[1])
a.append(30)
print(a)
# Принимает числа в диапазоне 0<=x<256

# счётчик (Counter)
from collections import Counter
print(Counter(['A','A','B','C','B','B','A','C']))
counter=Counter({'A':3,'B':6,'C':2})
print(counter)
counter.update(['A'])
counter.update(['B'])
print(counter)

#DefaultDict
from collections import defaultdict
dict1=defaultdict(int)
list1=[1,2,3,4,5,6,7,8,9]
for i in list1:
    dict1[i]+=1
print(dict1)

# ChainMap
from collections import ChainMap
d1={'a':1,'b':2}
d2={'f':3,'m':4}
d3={'v':7,'d':4}
c=ChainMap(d1,d2,d3)
print(c)
print(c['a'])
#print(c['g'])

# Связанный список
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
 # создание элементов
list=LinkedList()
list.head=Node(1)
second=Node(2)
third=Node(3)
# ссылки на следующие элементы
list.head.next=second
second.next=third
# обход элементов
list.printList()

# СТЭК линейная структура данных (первым пришел-первым ушел)(первым пришел последним ушел)
# ППУ  ПППУ VIP
# Push () Pop() Top

# Стек списком

stack=[]
stack.append('g')
stack.append('V')
stack.append('C')
print('Реализация стека:')
print(stack)
print('Удаление элементов в стеке:')
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
print('Стек очищен:')


# Стек коллекцией
from collections import deque
stack=deque()
stack.append('g')
stack.append('V')
stack.append('C')
print('Реализация стека:')
print(stack)
print('Удаление элементов в стеке:')
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
print('Стек очищен:')


# Стек с использованием модуля очереди
from queue import LifoQueue
stack=LifoQueue(maxsize=3)
print(stack.qsize())
stack.put('g')
stack.put('c')
stack.put('s')
print('Весь стек:',stack.full())
print('Размер стека:',stack.qsize())
print(stack.get())
print(stack.get())
print(stack.get())
# Проверка на пустоту
print(stack.empty())

# очередь с приоритетом
class VipQueue(object):
    def __init__(self):
        self.queue=[]
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len (self.queue)==0
    def insert(self,data):
        self.queue.append(data)
    def delete(self):
        try:
            max=0
            for i in range(len(self.queue)):
                if self.queue[i]>self.queue[max]:
                    max=i
            item=self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
myQueue=VipQueue()
myQueue.insert(12)
myQueue.insert(1)
myQueue.insert(14)
myQueue.insert(17)
print(myQueue)
while not myQueue.isEmpty():
    print(myQueue.delete())
