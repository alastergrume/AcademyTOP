from tkinter import *


class MainApp(Frame):
    def __init__(self, root):
        super(MainApp, self).__init__(root)
        self.build()

    def build(self):
        self.formula = '0'
        self.lbl = Label(text=self.formula, font=('Times New Roman', 21, 'bold'), bg='#000', foreground='#FFF')
        self.lbl.place(x=11, y=50)

        x = 10
        y = 140

        button_list = ['C', 'DEL', '*', '=',
                       '1', '2', '3', '/',
                       '4', '5', '6', '+',
                       '7', '8', '9', '-',
                       '0', '%', 'X^2', '.',
                       ]
        for btn in button_list:
            com = lambda x=btn: self.logicalc(x)
            Button(text=btn, bg='#FFF', font=('Times New Roman', 15), command=com).place(x=x, y=y, width=115, height=80)
            x += 110
            if x > 400:
                x = 10
                y += 80

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ''
        elif operation == 'DEL':
            self.formula = self.formula[0:-1]
        elif operation == '=':
            self.formula = str(eval(self.formula))
        elif operation == 'X^2':
            self.formula = str((eval(self.formula))**2)
        elif operation == '%':
            self.formula = str((eval(self.formula))/100)
        else:
            if self.formula == '0':
                self.formula = ''
            self.formula += operation

        self.update()

    def update(self):
        if self.formula == '':
            self.formula = '0'
        self.lbl.configure(text=self.formula)

# main.py
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
