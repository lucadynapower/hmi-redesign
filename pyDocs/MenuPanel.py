# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuPanel.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_VerticalLayout(object):
    def setupUi(self, VerticalLayout):
        if not VerticalLayout.objectName():
            VerticalLayout.setObjectName(u"VerticalLayout")
        VerticalLayout.resize(385, 676)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VerticalLayout.sizePolicy().hasHeightForWidth())
        VerticalLayout.setSizePolicy(sizePolicy)
        VerticalLayout.setStyleSheet(u"background-color: #D3D3D3;")
        self.verticalLayout_2 = QVBoxLayout(VerticalLayout)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.CommandsButton = QPushButton(VerticalLayout)
        self.CommandsButton.setObjectName(u"CommandsButton")
        font = QFont()
        font.setPointSize(20)
        self.CommandsButton.setFont(font)
        self.CommandsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.CommandsButton)

        self.FaultsButton = QPushButton(VerticalLayout)
        self.FaultsButton.setObjectName(u"FaultsButton")
        self.FaultsButton.setFont(font)
        self.FaultsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.FaultsButton)

        self.AlarmsStatusButton = QPushButton(VerticalLayout)
        self.AlarmsStatusButton.setObjectName(u"AlarmsStatusButton")
        self.AlarmsStatusButton.setFont(font)
        self.AlarmsStatusButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.AlarmsStatusButton)

        self.MetersButton = QPushButton(VerticalLayout)
        self.MetersButton.setObjectName(u"MetersButton")
        self.MetersButton.setFont(font)
        self.MetersButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.MetersButton)

        self.VFPQButton = QPushButton(VerticalLayout)
        self.VFPQButton.setObjectName(u"VFPQButton")
        self.VFPQButton.setFont(font)
        self.VFPQButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.VFPQButton)

        self.VFUFButton = QPushButton(VerticalLayout)
        self.VFUFButton.setObjectName(u"VFUFButton")
        self.VFUFButton.setFont(font)
        self.VFUFButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.VFUFButton)

        self.CloseButton = QPushButton(VerticalLayout)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setFont(font)
        self.CloseButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.CloseButton)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)

        self.retranslateUi(VerticalLayout)

        QMetaObject.connectSlotsByName(VerticalLayout)
    # setupUi

    def retranslateUi(self, VerticalLayout):
        VerticalLayout.setWindowTitle(QCoreApplication.translate("VerticalLayout", u"Form", None))
        self.CommandsButton.setText(QCoreApplication.translate("VerticalLayout", u"Commands", None))
        self.FaultsButton.setText(QCoreApplication.translate("VerticalLayout", u"Faults", None))
        self.AlarmsStatusButton.setText(QCoreApplication.translate("VerticalLayout", u"Alarms + Status", None))
        self.MetersButton.setText(QCoreApplication.translate("VerticalLayout", u"Meters", None))
        self.VFPQButton.setText(QCoreApplication.translate("VerticalLayout", u"VF Tables (PQ)", None))
        self.VFUFButton.setText(QCoreApplication.translate("VerticalLayout", u"VF Tables (UF)", None))
        self.CloseButton.setText(QCoreApplication.translate("VerticalLayout", u"Close", None))
    # retranslateUi

