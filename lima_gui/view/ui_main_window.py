# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowhcZjkz.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 492)
        self.actionAdd_chat = QAction(MainWindow)
        self.actionAdd_chat.setObjectName(u"actionAdd_chat")
        self.actionDelete_chat = QAction(MainWindow)
        self.actionDelete_chat.setObjectName(u"actionDelete_chat")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionEdit_chat = QAction(MainWindow)
        self.actionEdit_chat.setObjectName(u"actionEdit_chat")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionCopy_chat = QAction(MainWindow)
        self.actionCopy_chat.setObjectName(u"actionCopy_chat")
        self.actionOpenAI_API = QAction(MainWindow)
        self.actionOpenAI_API.setObjectName(u"actionOpenAI_API")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 770, 22))
        self.menu_New = QMenu(self.menubar)
        self.menu_New.setObjectName(u"menu_New")
        self.menuOpenAI_API = QMenu(self.menubar)
        self.menuOpenAI_API.setObjectName(u"menuOpenAI_API")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_New.menuAction())
        self.menubar.addAction(self.menuOpenAI_API.menuAction())
        self.menu_New.addAction(self.actionOpen)
        self.menu_New.addAction(self.actionSave)
        self.menuOpenAI_API.addAction(self.actionOpenAI_API)
        self.menuOpenAI_API.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionAdd_chat)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDelete_chat)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy_chat)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_chat.setText(QCoreApplication.translate("MainWindow", u"Add chat", None))
        self.actionDelete_chat.setText(QCoreApplication.translate("MainWindow", u"Delete chat", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionEdit_chat.setText(QCoreApplication.translate("MainWindow", u"Edit chat", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.actionCopy_chat.setText(QCoreApplication.translate("MainWindow", u"Copy chat", None))
#if QT_CONFIG(shortcut)
        self.actionCopy_chat.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenAI_API.setText(QCoreApplication.translate("MainWindow", u"OpenAI API", None))
        self.menu_New.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuOpenAI_API.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

