from tkinter import *

class LOG:
    def __init__(self, app):
        self.log_lable = ''
        self.app = app

    def log(self):
        self.log_lable = ''
        self.app.lbl2 = Label(text=self.log_lable, font=('Times New Roman', 21, 'bold'), bg='#222', foreground='#FFF')
        self.app.lbl2.place(x=30, y=100)


    def log_update(self, app):
        self.log_lable += self.app.formula
        self.app.lbl2.configure(text=self.app.lbl)

