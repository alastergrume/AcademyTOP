# import MainWindow_rc




from PyQt5.QtGui import QWindow, QDoubleValidator
from PyQt5.QtCore import pyqtSignal
from Utility.CplusDObserver import CplusDObserver
from Utility.CplusDMeta import CplusDMeta
from View import Ui_MainWindow


class CplusDView(QWindow, CplusDObserver, metaclass=CplusDMeta):

    def __init__(self, inController, inModel, parent=None):
        #  Класс, отвечающий за визуальное представление
        self.mController = inController
        self.mModel = inModel
        # Подключение визуального прдставления
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        # Регистриркуем педставление в качестве наблюдателя
        self.mModel.addObserver(self)
        # устанавливаем валидаторы полей ввода данных
        self.ui.le_c.setValidator(QDoubleValidator())
        self.ui.le_d.setValidator(QDoubleValidator())
        # связываем событие завершения редактирования с методом контроллера
        self.connect(self.ui.le_c, pyqtSignal("editingFinished()"), self.mController.setC)
        self.connect(self.ui.le_d, pyqtSignal("editingFinished()"), self.mController.setD)
