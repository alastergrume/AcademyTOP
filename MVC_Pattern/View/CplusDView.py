# import MainWindow_rc

from PyQt5 import QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import pyqtSignal
from MVC_Pattern.Utility.CplusDObserver import CplusDObserver
from MVC_Pattern.Utility.CplusDMeta import CplusDMeta
from MVC_Pattern.View.MainWindow import Ui_MainWindow


class CplusDView(QtWidgets.QMainWindow, CplusDObserver, metaclass=CplusDMeta):

    def __init__(self, inController, inModel, parent=None):
        super().__init__(parent)
        #  Класс, отвечающий за визуальное

        self.mController = inController
        self.mModel = inModel
        # Подключение визуального прдставления
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Регистрируем педставление в качестве наблюдателя
        self.mModel.addObserver(self)
        # устанавливаем валидаторы полей ввода данных
        self.ui.le_c.setValidator(QDoubleValidator())
        self.ui.le_d.setValidator(QDoubleValidator())
        # связываем событие завершения редактирования с методом контроллера

        self.ui.le_c.editingFinished.connect(self.mController.setD)
        self.ui.le_d.editingFinished.connect(self.mController.setC)
        # self.connect(self.ui.le_c, pyqtSignal("editingFinished()"), self.mController.setC)
        # self.connect(self.ui.le_d, pyqtSignal("editingFinished()"), self.mController.setD)

    def modelIsChanged(self):
        # Реализация метода modelIsChanged
        pass  # или добавьте нужную логику здесь