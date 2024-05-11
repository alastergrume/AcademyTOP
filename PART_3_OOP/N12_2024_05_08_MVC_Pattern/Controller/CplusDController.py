from OOP.N12_MVC_Pattern.View.CplusDView import CplusDView


# класс представляет реализацию контроллера.
# Согласовывает работу представления с моделью

class CplusDController():
    def __init__(self, inModel):
        # Конструктор принимает ссылку на модель, создает и отображает представление
        self.mModel = inModel
        self.mView = CplusDView(self, self.mModel)
        self.mView.show()

    def setC(self):
        # При завершении редактирования поля ввода данных для C контроллер изменяет свойство модели
        c = self.mView.ui.le_c.text()
        self.mModel.setC(c)

    def setD(self):
        # При завершении редактирования поля ввода данных для D контроллер изменяет свойство модели
        d = self.mView.ui.le_d.text()
        self.mModel.setD(d)


