# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'param_itemIdSJNA.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLayout, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_ParamItem(object):
    def setupUi(self, ParamItem):
        if not ParamItem.objectName():
            ParamItem.setObjectName(u"ParamItem")
        ParamItem.resize(592, 164)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ParamItem.sizePolicy().hasHeightForWidth())
        ParamItem.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(ParamItem)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.widget = QWidget(ParamItem)
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
        self.paramNameLabel = QLabel(self.widget)
        self.paramNameLabel.setObjectName(u"paramNameLabel")

        self.horizontalLayout.addWidget(self.paramNameLabel)

        self.paramTypeLabel = QLabel(self.widget)
        self.paramTypeLabel.setObjectName(u"paramTypeLabel")

        self.horizontalLayout.addWidget(self.paramTypeLabel)

        self.requiredCheckBox = QCheckBox(self.widget)
        self.requiredCheckBox.setObjectName(u"requiredCheckBox")
        self.requiredCheckBox.setEnabled(False)

        self.horizontalLayout.addWidget(self.requiredCheckBox)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.widget)

        self.valueTextEdit = QTextEdit(ParamItem)
        self.valueTextEdit.setObjectName(u"valueTextEdit")
        sizePolicy1.setHeightForWidth(self.valueTextEdit.sizePolicy().hasHeightForWidth())
        self.valueTextEdit.setSizePolicy(sizePolicy1)
        self.valueTextEdit.setSizeIncrement(QSize(0, 0))
        self.valueTextEdit.setTabStopDistance(25.000000000000000)

        self.verticalLayout.addWidget(self.valueTextEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ParamItem)

        QMetaObject.connectSlotsByName(ParamItem)
    # setupUi

    def retranslateUi(self, ParamItem):
        ParamItem.setWindowTitle(QCoreApplication.translate("ParamItem", u"Form", None))
        self.paramNameLabel.setText(QCoreApplication.translate("ParamItem", u"Parameter name", None))
        self.paramTypeLabel.setText(QCoreApplication.translate("ParamItem", u"Parameter type", None))
        self.requiredCheckBox.setText(QCoreApplication.translate("ParamItem", u"Required", None))
        self.valueTextEdit.setPlaceholderText(QCoreApplication.translate("ParamItem", u"content", None))
    # retranslateUi

