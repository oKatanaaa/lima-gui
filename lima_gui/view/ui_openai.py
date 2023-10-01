# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'openaixTrFdP.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_openai(object):
    def setupUi(self, openai):
        if not openai.objectName():
            openai.setObjectName(u"openai")
        openai.setEnabled(True)
        openai.resize(400, 300)
        self.verticalLayout = QVBoxLayout(openai)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(openai)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 6, 1, 1, 1)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 8, 2, 1, 1)

        self.apiBase_lineEdit = QLineEdit(self.widget)
        self.apiBase_lineEdit.setObjectName(u"apiBase_lineEdit")

        self.gridLayout_2.addWidget(self.apiBase_lineEdit, 0, 2, 1, 1)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 5, 2, 1, 1)

        self.temperature_lineEdit = QLineEdit(self.widget)
        self.temperature_lineEdit.setObjectName(u"temperature_lineEdit")

        self.gridLayout_2.addWidget(self.temperature_lineEdit, 4, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 5, 1, 1, 1)

        self.modelName_lineEdit = QLineEdit(self.widget)
        self.modelName_lineEdit.setObjectName(u"modelName_lineEdit")

        self.gridLayout_2.addWidget(self.modelName_lineEdit, 2, 2, 1, 1)

        self.completionTokens_lineEdit = QLineEdit(self.widget)
        self.completionTokens_lineEdit.setObjectName(u"completionTokens_lineEdit")

        self.gridLayout_2.addWidget(self.completionTokens_lineEdit, 6, 2, 1, 1)

        self.apiKey_lineEdit = QLineEdit(self.widget)
        self.apiKey_lineEdit.setObjectName(u"apiKey_lineEdit")

        self.gridLayout_2.addWidget(self.apiKey_lineEdit, 1, 2, 1, 1)

        self.copyKey_pushButton = QPushButton(self.widget)
        self.copyKey_pushButton.setObjectName(u"copyKey_pushButton")

        self.gridLayout_2.addWidget(self.copyKey_pushButton, 7, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(openai)

        QMetaObject.connectSlotsByName(openai)
    # setupUi

    def retranslateUi(self, openai):
        openai.setWindowTitle(QCoreApplication.translate("openai", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("openai", u"Model", None))
        self.label_6.setText(QCoreApplication.translate("openai", u"Completion tokens", None))
        self.checkBox.setText(QCoreApplication.translate("openai", u"Enable API", None))
#if QT_CONFIG(tooltip)
        self.apiBase_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.temperature_lineEdit.setText(QCoreApplication.translate("openai", u"0.7", None))
        self.label_2.setText(QCoreApplication.translate("openai", u"API key", None))
        self.label_3.setText(QCoreApplication.translate("openai", u"API base", None))
        self.label_4.setText(QCoreApplication.translate("openai", u"Temperature", None))
        self.label_5.setText(QCoreApplication.translate("openai", u"API type", None))
#if QT_CONFIG(tooltip)
        self.modelName_lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.modelName_lineEdit.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.modelName_lineEdit.setText(QCoreApplication.translate("openai", u"gpt-3.5-turbo", None))
        self.completionTokens_lineEdit.setText(QCoreApplication.translate("openai", u"200", None))
        self.copyKey_pushButton.setText(QCoreApplication.translate("openai", u"Copy key from ENV", None))
    # retranslateUi

