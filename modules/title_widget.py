# coding:utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout

from qfluentwidgets import  SearchLineEdit
from qframelesswindow import TitleBar,StandardTitleBar

class CustomTitleBar(TitleBar):
    """ Title bar with icon and title """
    def __init__(self, parent):
        super(CustomTitleBar,self).__init__(parent)
        self.setFixedHeight(48)
        self.hBoxLayout.removeWidget(self.minBtn)
        self.hBoxLayout.removeWidget(self.maxBtn)
        self.hBoxLayout.removeWidget(self.closeBtn)

        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(18, 18)
        self.hBoxLayout.insertSpacing(0, 20)
        self.hBoxLayout.insertWidget(
            1, self.iconLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(
            2, self.titleLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.titleLabel.setObjectName('titleLabel')
        self.window().windowTitleChanged.connect(self.setTitle)

        # add search line edit
        # self.searchLineEdit = SearchLineEdit(self)
        # self.searchLineEdit.setPlaceholderText('搜索应用、游戏、电影、设备等')
        # self.searchLineEdit.setFixedWidth(400)
        # self.searchLineEdit.setClearButtonEnabled(True)
        #
        self.vBoxLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(0)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setAlignment(Qt.AlignTop)
        self.buttonLayout.addWidget(self.minBtn)
        self.buttonLayout.addWidget(self.maxBtn)
        self.buttonLayout.addWidget(self.closeBtn)
        self.vBoxLayout.addLayout(self.buttonLayout)
        self.vBoxLayout.addStretch(1)
        self.hBoxLayout.addLayout(self.vBoxLayout, 0)

    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setIcon(self, icon):
        self.iconLabel.setPixmap(QIcon(icon).pixmap(18, 18))

    # def resizeEvent(self, e):
    #     self.searchLineEdit.move((self.width() - self.searchLineEdit.width()) //2, 8)
