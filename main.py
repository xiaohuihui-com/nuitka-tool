# coding:utf-8

import os
import sys

# 导入核心模块
from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtWidgets import QApplication

# 导入自定义样式组件
from qfluentwidgets import FluentTranslator

# 导入配置模块
from gallary.app.common.config import cfg
# 导入主窗口
from gallary.app.view.main_window import MainWindow

# 启用 DPI 缩放
# 根据配置调整 DPI 缩放
if cfg.get(cfg.dpiScale) == "Auto":
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
else:
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

# 创建应用程序
# 初始化应用程序对象
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

# 国际化支持
# 设置多语言支
locale = cfg.get(cfg.language).value
translator = FluentTranslator(locale)
galleryTranslator = QTranslator()
galleryTranslator.load(locale, "gallery", ".", ":/gallery/i18n")

app.installTranslator(translator)
app.installTranslator(galleryTranslator)

# 创建主窗口
# 创建并显示主窗口对象
w = MainWindow()
w.show()

# 启动应用程序的事件循环
app.exec_()
