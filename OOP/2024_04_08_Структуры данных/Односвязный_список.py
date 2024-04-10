class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SingList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    def remove(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
    def replace(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return
            current = current.next

singlist = SingList()
while True:
    print("""
    1. Add
    2. Display
    3. Cheked
    4. Remove
    5. Replace
    """)
    choice = int(input("Enter number of Menu -> "))
    if choice == 0:
        break
    if choice == 1:
        data = int(input("Введите элемент для добавления -> "))
        singlist.append(data)
    if choice == 2:
        singlist.display()
    if choice == 3:
        data = int(input("Введите элемент для поиска -> "))
        print(data, "в списке - ", singlist.search(data))
    if choice == 4:
        data = int(input("Введите элемент для удаления -> "))
        singlist.remove(data)
    if choice == 5:
        old_data = int(input("Введите старый элемент ->"))
        new_data = int(input("Введите новый элемент -> "))
        singlist.replace(old_data, new_data)
    if choice == 6:
        node = (Node())
        print(node.data)
    if choice == 7:
        node = (Node())
        print(node.next)


