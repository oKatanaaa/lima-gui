# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fn_parameter_widgetEPEnZs.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.paramRequiredCheckBox = QCheckBox(Form)
        self.paramRequiredCheckBox.setObjectName(u"paramRequiredCheckBox")

        self.gridLayout.addWidget(self.paramRequiredCheckBox, 5, 1, 1, 1)

        self.paramDescLineEdit = QTextEdit(Form)
        self.paramDescLineEdit.setObjectName(u"paramDescLineEdit")

        self.gridLayout.addWidget(self.paramDescLineEdit, 2, 1, 1, 1)

        self.paramTypeLineEdit = QLineEdit(Form)
        self.paramTypeLineEdit.setObjectName(u"paramTypeLineEdit")

        self.gridLayout.addWidget(self.paramTypeLineEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.paramNameLineEdit = QLineEdit(Form)
        self.paramNameLineEdit.setObjectName(u"paramNameLineEdit")

        self.gridLayout.addWidget(self.paramNameLineEdit, 0, 1, 1, 1)

        self.paramEnumListWidget = QListWidget(Form)
        self.paramEnumListWidget.setObjectName(u"paramEnumListWidget")

        self.gridLayout.addWidget(self.paramEnumListWidget, 3, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.enumAddBtn = QPushButton(self.widget)
        self.enumAddBtn.setObjectName(u"enumAddBtn")

        self.horizontalLayout.addWidget(self.enumAddBtn)

        self.enumDeleteBtn = QPushButton(self.widget)
        self.enumDeleteBtn.setObjectName(u"enumDeleteBtn")

        self.horizontalLayout.addWidget(self.enumDeleteBtn)


        self.gridLayout.addWidget(self.widget, 4, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.paramRequiredCheckBox.setText(QCoreApplication.translate("Form", u"Required", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Enum", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Type", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Description", None))
        self.enumAddBtn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.enumDeleteBtn.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

