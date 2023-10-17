# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fn_parameter_widgetvYmGnI.ui'
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
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_fnParameter(object):
    def setupUi(self, fnParameter):
        if not fnParameter.objectName():
            fnParameter.setObjectName(u"fnParameter")
        fnParameter.resize(352, 254)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fnParameter.sizePolicy().hasHeightForWidth())
        fnParameter.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(fnParameter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.paramRequiredCheckBox = QCheckBox(fnParameter)
        self.paramRequiredCheckBox.setObjectName(u"paramRequiredCheckBox")

        self.gridLayout.addWidget(self.paramRequiredCheckBox, 5, 1, 1, 1)

        self.paramDescLineEdit = QTextEdit(fnParameter)
        self.paramDescLineEdit.setObjectName(u"paramDescLineEdit")
        sizePolicy.setHeightForWidth(self.paramDescLineEdit.sizePolicy().hasHeightForWidth())
        self.paramDescLineEdit.setSizePolicy(sizePolicy)
        self.paramDescLineEdit.setMaximumSize(QSize(1200, 50))

        self.gridLayout.addWidget(self.paramDescLineEdit, 2, 1, 1, 1)

        self.paramTypeLineEdit = QLineEdit(fnParameter)
        self.paramTypeLineEdit.setObjectName(u"paramTypeLineEdit")

        self.gridLayout.addWidget(self.paramTypeLineEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(fnParameter)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_2 = QLabel(fnParameter)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.paramNameLineEdit = QLineEdit(fnParameter)
        self.paramNameLineEdit.setObjectName(u"paramNameLineEdit")

        self.gridLayout.addWidget(self.paramNameLineEdit, 0, 1, 1, 1)

        self.paramEnumListWidget = QListWidget(fnParameter)
        self.paramEnumListWidget.setObjectName(u"paramEnumListWidget")
        sizePolicy.setHeightForWidth(self.paramEnumListWidget.sizePolicy().hasHeightForWidth())
        self.paramEnumListWidget.setSizePolicy(sizePolicy)
        self.paramEnumListWidget.setMaximumSize(QSize(1200, 50))

        self.gridLayout.addWidget(self.paramEnumListWidget, 3, 1, 1, 1)

        self.label = QLabel(fnParameter)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(fnParameter)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.widget = QWidget(fnParameter)
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

        self.gridLayout.setRowMinimumHeight(2, 50)
        self.gridLayout.setRowMinimumHeight(3, 50)

        self.retranslateUi(fnParameter)

        QMetaObject.connectSlotsByName(fnParameter)
    # setupUi

    def retranslateUi(self, fnParameter):
        fnParameter.setWindowTitle(QCoreApplication.translate("fnParameter", u"Form", None))
        self.paramRequiredCheckBox.setText(QCoreApplication.translate("fnParameter", u"Required", None))
        self.label_4.setText(QCoreApplication.translate("fnParameter", u"Enum", None))
        self.label_2.setText(QCoreApplication.translate("fnParameter", u"Type", None))
        self.label.setText(QCoreApplication.translate("fnParameter", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("fnParameter", u"Description", None))
        self.enumAddBtn.setText(QCoreApplication.translate("fnParameter", u"Add", None))
        self.enumDeleteBtn.setText(QCoreApplication.translate("fnParameter", u"Delete", None))
    # retranslateUi

