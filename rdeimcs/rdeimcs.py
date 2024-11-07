# coding:utf-8
import sys
from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtWidgets import QApplication

from qfluentwidgets import FluentTranslator
from app.view.main_window import MainWindow

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    translator = FluentTranslator(QLocale())
    app.installTranslator(translator)
    w = MainWindow()
    w.show()
    app.exec_()
