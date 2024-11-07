# coding: utf-8
from PyQt5.QtCore import QSize, QTimer, Qt, QEventLoop
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import FluentWindow, SplashScreen,NavigationItemPosition, SubtitleLabel, setFont
from qfluentwidgets import FluentIcon as FIF
from app.view import HomeInterface
from app.resource import resources_rc



class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class MainWindow(FluentWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()

        self.homeInterface = HomeInterface(self)
        self.folderInterface = Widget('帮助', self)
        self.settingInterface = Widget('设置', self)

        # self.connectSignalToSlot()
        self.initNavigation()

        self.splashScreen.finish()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页')
        self.addSubInterface(self.folderInterface, FIF.FOLDER, '帮助', NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.settingInterface, FIF.SETTING, '设置', NavigationItemPosition.BOTTOM)
    def initWindow(self):
        self.resize(960, 780)
        self.setMinimumWidth(760)
        self.setWindowIcon(QIcon(':resource/images/logo.png'))
        self.setWindowTitle('四川省小型水库安全检测智能中心站系统')

        # create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(102, 102))
        self.splashScreen.raise_()

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()
        self.createSubInterface()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if hasattr(self, 'splashScreen'):
            self.splashScreen.resize(self.size())

    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(1000, loop.quit)
        loop.exec()
