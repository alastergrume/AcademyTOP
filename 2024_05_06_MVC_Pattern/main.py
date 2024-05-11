# MVC Pattern
import sys
from PyQt5.QtWidgets import QApplication, QWidget

from Model.CplusDModel import CplusDModel
from Controller.CplusDController import CplusDController

def main():
    app = QApplication(sys.argv)
    # Создаем модель
    model = CplusDModel()
    # Создаем контроллер и передаем ему ссылку
    controller = CplusDController(model)
    # Запускаем приложение
    app.exec()

if __name__ == "__main__":
    main()

