# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_widgetsyhvXn.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_ChatWidget(object):
    def setupUi(self, ChatWidget):
        if not ChatWidget.objectName():
            ChatWidget.setObjectName(u"ChatWidget")
        ChatWidget.resize(1087, 587)
        self.centralwidget = QWidget(ChatWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
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
        self.widget_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(357, 0))
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.msg_count = QLabel(self.widget_2)
        self.msg_count.setObjectName(u"msg_count")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.msg_count.sizePolicy().hasHeightForWidth())
        self.msg_count.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.msg_count, 4, 1, 1, 1)

        self.language = QComboBox(self.widget_2)
        self.language.setObjectName(u"language")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.language.sizePolicy().hasHeightForWidth())
        self.language.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.language, 2, 1, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.name = QLineEdit(self.widget_2)
        self.name.setObjectName(u"name")
        sizePolicy3.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.n_tokens = QLabel(self.widget_2)
        self.n_tokens.setObjectName(u"n_tokens")
        sizePolicy2.setHeightForWidth(self.n_tokens.sizePolicy().hasHeightForWidth())
        self.n_tokens.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.n_tokens, 3, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tagList = QListWidget(self.widget_3)
        self.tagList.setObjectName(u"tagList")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tagList.sizePolicy().hasHeightForWidth())
        self.tagList.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.tagList)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy4.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy4)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addTagBtn = QPushButton(self.widget_4)
        self.addTagBtn.setObjectName(u"addTagBtn")

        self.horizontalLayout_4.addWidget(self.addTagBtn)

        self.deleteTagBtn = QPushButton(self.widget_4)
        self.deleteTagBtn.setObjectName(u"deleteTagBtn")

        self.horizontalLayout_4.addWidget(self.deleteTagBtn)

        self.tagComboBox = QComboBox(self.widget_4)
        self.tagComboBox.setObjectName(u"tagComboBox")

        self.horizontalLayout_4.addWidget(self.tagComboBox)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.gridLayout.addWidget(self.widget_3, 5, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_2)

        ChatWidget.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ChatWidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1087, 22))
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
        self.msg_count.setText(QCoreApplication.translate("ChatWidget", u"null", None))
        self.label.setText(QCoreApplication.translate("ChatWidget", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("ChatWidget", u"Msg count", None))
        self.label_2.setText(QCoreApplication.translate("ChatWidget", u"Language", None))
        self.n_tokens.setText(QCoreApplication.translate("ChatWidget", u"null", None))
        self.label_3.setText(QCoreApplication.translate("ChatWidget", u"Tokens:", None))
        self.label_4.setText(QCoreApplication.translate("ChatWidget", u"Tags", None))
        self.addTagBtn.setText(QCoreApplication.translate("ChatWidget", u"Add", None))
        self.deleteTagBtn.setText(QCoreApplication.translate("ChatWidget", u"Delete", None))
    # retranslateUi

