# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function_descriptionIcOijS.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_FunctionDescription(object):
    def setupUi(self, FunctionDescription):
        if not FunctionDescription.objectName():
            FunctionDescription.setObjectName(u"FunctionDescription")
        FunctionDescription.resize(992, 458)
        self.horizontalLayout_3 = QHBoxLayout(FunctionDescription)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.parametersListWidget = QListWidget(FunctionDescription)
        self.parametersListWidget.setObjectName(u"parametersListWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parametersListWidget.sizePolicy().hasHeightForWidth())
        self.parametersListWidget.setSizePolicy(sizePolicy)
        self.parametersListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.parametersListWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.parametersListWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.parametersListWidget.setMovement(QListView.Free)
        self.parametersListWidget.setResizeMode(QListView.Adjust)

        self.verticalLayout.addWidget(self.parametersListWidget)

        self.widget = QWidget(FunctionDescription)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addParamBtn = QPushButton(self.widget)
        self.addParamBtn.setObjectName(u"addParamBtn")

        self.horizontalLayout.addWidget(self.addParamBtn)

        self.deleteParamBtn = QPushButton(self.widget)
        self.deleteParamBtn.setObjectName(u"deleteParamBtn")

        self.horizontalLayout.addWidget(self.deleteParamBtn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.widget_2 = QWidget(FunctionDescription)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
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
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.fnDescription = QLabel(self.widget_2)
        self.fnDescription.setObjectName(u"fnDescription")

        self.gridLayout.addWidget(self.fnDescription, 2, 0, 1, 1)

        self.fnName = QLabel(self.widget_2)
        self.fnName.setObjectName(u"fnName")

        self.gridLayout.addWidget(self.fnName, 1, 0, 1, 1)

        self.fnDescriptionTextEdit = QTextEdit(self.widget_2)
        self.fnDescriptionTextEdit.setObjectName(u"fnDescriptionTextEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fnDescriptionTextEdit.sizePolicy().hasHeightForWidth())
        self.fnDescriptionTextEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.fnDescriptionTextEdit, 2, 1, 1, 1)

        self.fnNameTextEdit = QLineEdit(self.widget_2)
        self.fnNameTextEdit.setObjectName(u"fnNameTextEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fnNameTextEdit.sizePolicy().hasHeightForWidth())
        self.fnNameTextEdit.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.fnNameTextEdit, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.fnSaveBtn = QPushButton(self.widget_2)
        self.fnSaveBtn.setObjectName(u"fnSaveBtn")

        self.gridLayout_2.addWidget(self.fnSaveBtn, 1, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.retranslateUi(FunctionDescription)

        QMetaObject.connectSlotsByName(FunctionDescription)
    # setupUi

    def retranslateUi(self, FunctionDescription):
        FunctionDescription.setWindowTitle(QCoreApplication.translate("FunctionDescription", u"Form", None))
        self.addParamBtn.setText(QCoreApplication.translate("FunctionDescription", u"Add parameter", None))
        self.deleteParamBtn.setText(QCoreApplication.translate("FunctionDescription", u"Delete parameter", None))
        self.fnDescription.setText(QCoreApplication.translate("FunctionDescription", u"Description", None))
        self.fnName.setText(QCoreApplication.translate("FunctionDescription", u"Name", None))
        self.fnDescriptionTextEdit.setPlaceholderText(QCoreApplication.translate("FunctionDescription", u"Describe your function here", None))
        self.fnSaveBtn.setText(QCoreApplication.translate("FunctionDescription", u"Save function", None))
    # retranslateUi

