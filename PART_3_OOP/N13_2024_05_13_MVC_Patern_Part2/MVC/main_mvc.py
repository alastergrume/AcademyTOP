from tkinter import *
from view import *
from controller import *


def main():
    root = Tk()  # Создание объекта окна
    root['bg'] = '#000'
    root.geometry('485x550+200+200')
    root.title('Калькулятор')
    root.resizable(False, False)
    app = MainApp(root)
    app.pack
    root.mainloop()  # Инициализация


if __name__ == '__main__':
    main()