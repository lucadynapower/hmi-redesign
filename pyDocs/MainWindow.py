# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 812)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainLayout = QVBoxLayout()
        self.MainLayout.setObjectName(u"MainLayout")
        self.pageStack = QStackedWidget(self.centralwidget)
        self.pageStack.setObjectName(u"pageStack")

        self.MainLayout.addWidget(self.pageStack)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MenuButton = QPushButton(self.centralwidget)
        self.MenuButton.setObjectName(u"MenuButton")
        font = QFont()
        font.setPointSize(16)
        self.MenuButton.setFont(font)
        self.MenuButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.horizontalLayout.addWidget(self.MenuButton)

        self.BufLabel = QLabel(self.centralwidget)
        self.BufLabel.setObjectName(u"BufLabel")
        font1 = QFont()
        font1.setPointSize(12)
        self.BufLabel.setFont(font1)

        self.horizontalLayout.addWidget(self.BufLabel)

        self.BottomSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.BottomSpacer)

        self.QuickControlButton = QPushButton(self.centralwidget)
        self.QuickControlButton.setObjectName(u"QuickControlButton")
        font2 = QFont()
        font2.setPointSize(14)
        self.QuickControlButton.setFont(font2)
        self.QuickControlButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.horizontalLayout.addWidget(self.QuickControlButton)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 4)
        self.horizontalLayout.setStretch(3, 1)

        self.MainLayout.addLayout(self.horizontalLayout)

        self.MainLayout.setStretch(0, 5)
        self.MainLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.MainLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 859, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MenuButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.BufLabel.setText(QCoreApplication.translate("MainWindow", u"Buf", None))
        self.QuickControlButton.setText(QCoreApplication.translate("MainWindow", u"Quick Control", None))
    # retranslateUi

