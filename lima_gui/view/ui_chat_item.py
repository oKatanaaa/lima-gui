# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_itemEqoCss.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_ChatItem(object):
    def setupUi(self, ChatItem):
        if not ChatItem.objectName():
            ChatItem.setObjectName(u"ChatItem")
        ChatItem.resize(592, 164)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChatItem.sizePolicy().hasHeightForWidth())
        ChatItem.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(ChatItem)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.widget = QWidget(ChatItem)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.comboBox)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(ChatItem)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.fnNameComboBox = QComboBox(self.widget_2)
        self.fnNameComboBox.setObjectName(u"fnNameComboBox")

        self.horizontalLayout_4.addWidget(self.fnNameComboBox)

        self.fnCallParamsPushButton = QPushButton(self.widget_2)
        self.fnCallParamsPushButton.setObjectName(u"fnCallParamsPushButton")

        self.horizontalLayout_4.addWidget(self.fnCallParamsPushButton)


        self.verticalLayout.addWidget(self.widget_2)

        self.textEdit = QTextEdit(ChatItem)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setSizeIncrement(QSize(0, 0))
        self.textEdit.setTabStopDistance(25.000000000000000)

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ChatItem)

        QMetaObject.connectSlotsByName(ChatItem)
    # setupUi

    def retranslateUi(self, ChatItem):
        ChatItem.setWindowTitle(QCoreApplication.translate("ChatItem", u"Form", None))
        self.label.setText(QCoreApplication.translate("ChatItem", u"Role", None))
        self.label_2.setText(QCoreApplication.translate("ChatItem", u"Function name", None))
        self.fnCallParamsPushButton.setText(QCoreApplication.translate("ChatItem", u"Fn call parameters", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("ChatItem", u"content", None))
    # retranslateUi

