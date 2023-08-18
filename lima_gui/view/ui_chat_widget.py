# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_widgetuQQvJv.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_ChatWidget(object):
    def setupUi(self, ChatWidget):
        if not ChatWidget.objectName():
            ChatWidget.setObjectName(u"ChatWidget")
        ChatWidget.resize(800, 600)
        self.centralwidget = QWidget(ChatWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMovement(QListView.Free)
        self.listWidget.setResizeMode(QListView.Adjust)

        self.verticalLayout.addWidget(self.listWidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_msg_btn = QPushButton(self.widget)
        self.add_msg_btn.setObjectName(u"add_msg_btn")

        self.horizontalLayout.addWidget(self.add_msg_btn)

        self.delete_msg_btn = QPushButton(self.widget)
        self.delete_msg_btn.setObjectName(u"delete_msg_btn")

        self.horizontalLayout.addWidget(self.delete_msg_btn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.language = QComboBox(self.widget_2)
        self.language.setObjectName(u"language")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.language.sizePolicy().hasHeightForWidth())
        self.language.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.language, 2, 1, 1, 1)

        self.name = QLineEdit(self.widget_2)
        self.name.setObjectName(u"name")
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.n_tokens = QLabel(self.widget_2)
        self.n_tokens.setObjectName(u"n_tokens")
        sizePolicy1.setHeightForWidth(self.n_tokens.sizePolicy().hasHeightForWidth())
        self.n_tokens.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.n_tokens, 3, 1, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.msg_count = QLabel(self.widget_2)
        self.msg_count.setObjectName(u"msg_count")
        sizePolicy1.setHeightForWidth(self.msg_count.sizePolicy().hasHeightForWidth())
        self.msg_count.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.msg_count, 4, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_2)

        ChatWidget.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ChatWidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        ChatWidget.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ChatWidget)
        self.statusbar.setObjectName(u"statusbar")
        ChatWidget.setStatusBar(self.statusbar)

        self.retranslateUi(ChatWidget)

        QMetaObject.connectSlotsByName(ChatWidget)
    # setupUi

    def retranslateUi(self, ChatWidget):
        ChatWidget.setWindowTitle(QCoreApplication.translate("ChatWidget", u"MainWindow", None))
        self.add_msg_btn.setText(QCoreApplication.translate("ChatWidget", u"Add message", None))
        self.delete_msg_btn.setText(QCoreApplication.translate("ChatWidget", u"Delete message", None))
        self.label_3.setText(QCoreApplication.translate("ChatWidget", u"Tokens:", None))
        self.n_tokens.setText(QCoreApplication.translate("ChatWidget", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("ChatWidget", u"Language", None))
        self.label.setText(QCoreApplication.translate("ChatWidget", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("ChatWidget", u"Msg count", None))
        self.msg_count.setText(QCoreApplication.translate("ChatWidget", u"TextLabel", None))
    # retranslateUi

