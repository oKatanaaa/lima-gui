# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsKrEUWD.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Settings)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.tokenizerName = QLineEdit(self.widget)
        self.tokenizerName.setObjectName(u"tokenizerName")

        self.horizontalLayout.addWidget(self.tokenizerName)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.setTokBtn = QPushButton(self.widget)
        self.setTokBtn.setObjectName(u"setTokBtn")

        self.horizontalLayout_2.addWidget(self.setTokBtn)


        self.verticalLayout.addWidget(self.widget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.label_2 = QLabel(Settings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.listWidget = QListWidget(Settings)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.widget_2 = QWidget(Settings)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.loadButton = QPushButton(self.widget_2)
        self.loadButton.setObjectName(u"loadButton")

        self.horizontalLayout_3.addWidget(self.loadButton)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Tokenizer", None))
        self.setTokBtn.setText(QCoreApplication.translate("Settings", u"Set tokenizer", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Tags", None))
        self.loadButton.setText(QCoreApplication.translate("Settings", u"Load config", None))
    # retranslateUi

