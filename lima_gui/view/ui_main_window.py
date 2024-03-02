# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowAklWNB.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
        self.actionEdit_chat = QAction(MainWindow)
        self.actionEdit_chat.setObjectName(u"actionEdit_chat")
        self.actionSaveCurrent = QAction(MainWindow)
        self.actionSaveCurrent.setObjectName(u"actionSaveCurrent")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionCopy_chat = QAction(MainWindow)
        self.actionCopy_chat.setObjectName(u"actionCopy_chat")
        self.actionOpenAI_API = QAction(MainWindow)
        self.actionOpenAI_API.setObjectName(u"actionOpenAI_API")
        self.actionSave_New = QAction(MainWindow)
        self.actionSave_New.setObjectName(u"actionSave_New")
        self.actionSave_New.setMenuRole(QAction.NoRole)
        self.actionSave_to = QAction(MainWindow)
        self.actionSave_to.setObjectName(u"actionSave_to")
        self.actionExport_as_OpenAI_dataset = QAction(MainWindow)
        self.actionExport_as_OpenAI_dataset.setObjectName(u"actionExport_as_OpenAI_dataset")
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
        self.menu_New.addAction(self.actionSaveCurrent)
        self.menu_New.addAction(self.actionSave_to)
        self.menu_New.addAction(self.actionExport_as_OpenAI_dataset)
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
        self.actionEdit_chat.setText(QCoreApplication.translate("MainWindow", u"Edit chat", None))
        self.actionSaveCurrent.setText(QCoreApplication.translate("MainWindow", u"Save current", None))
#if QT_CONFIG(shortcut)
        self.actionSaveCurrent.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.actionCopy_chat.setText(QCoreApplication.translate("MainWindow", u"Copy chat", None))
#if QT_CONFIG(shortcut)
        self.actionCopy_chat.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenAI_API.setText(QCoreApplication.translate("MainWindow", u"OpenAI API", None))
        self.actionSave_New.setText(QCoreApplication.translate("MainWindow", u"Save New", None))
#if QT_CONFIG(tooltip)
        self.actionSave_New.setToolTip(QCoreApplication.translate("MainWindow", u"Save new", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave_New.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_to.setText(QCoreApplication.translate("MainWindow", u"Save to", None))
#if QT_CONFIG(shortcut)
        self.actionSave_to.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExport_as_OpenAI_dataset.setText(QCoreApplication.translate("MainWindow", u"Export as OpenAI dataset", None))
        self.menu_New.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuOpenAI_API.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

