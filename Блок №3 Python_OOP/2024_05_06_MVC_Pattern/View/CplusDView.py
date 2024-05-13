# import MainWindow_rc

from pathlib import Path

Utility = Path("D:/Ivan_Kalinin/Python/GitHub_Repo/AcademyTOP/Блок №3 Python_OOP/2024_05_06_MVC_Pattern/Utility")
View = Path("D:/Ivan_Kalinin/Python/GitHub_Repo/AcademyTOP/Блок №3 Python_OOP/2024_05_06_MVC_Pattern/View")

from PyQt5.QtGui import QWindow, QDoubleValidator
from PyQt5.QtCore import PYQT_SIGNAL
from Utility.CplusDObserver import CplusDObserver
from Utility.CplusDMeta import CplusDMeta
from View.MainWindow import Ui_MainWindow
from
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
        self.connect(self.ui.le_c, PYQT_SIGNAL("editingFinished()"), self.mController.setC)
        self.connect(self.ui.le_d, PYQT_SIGNAL("editingFinished()"), self.mController.setD)
