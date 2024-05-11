from PyQt6.Core import pyqtWrapperType
from abc import ABCMeta

# Модуль реализации метта-класса необходимого для работы предсталения
# pyqtWrapperType - меттакласс, общий для оконных компонентов библиотеки QT
# ABCMeta - метакласс для реализации абстрактных суперклассов
# CplusDMeta - метакласс для представления.

class CplusDMeta(pyqtWrapperType, ABCMeta):
    pass