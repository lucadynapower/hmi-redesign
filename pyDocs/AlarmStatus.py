# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AlarmStatus.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainLayout(object):
    def setupUi(self, MainLayout):
        if not MainLayout.objectName():
            MainLayout.setObjectName(u"MainLayout")
        MainLayout.resize(1070, 726)
        self.horizontalLayout_2 = QHBoxLayout(MainLayout)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TopLeftSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.TopLeftSpacer)

        self.GeneralFaultsButton = QPushButton(MainLayout)
        self.GeneralFaultsButton.setObjectName(u"GeneralFaultsButton")
        font = QFont()
        font.setPointSize(20)
        self.GeneralFaultsButton.setFont(font)
        self.GeneralFaultsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.GeneralFaultsButton)

        self.AlarmButton = QPushButton(MainLayout)
        self.AlarmButton.setObjectName(u"AlarmButton")
        self.AlarmButton.setFont(font)
        self.AlarmButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.AlarmButton)

        self.VFPQVFUFButton = QPushButton(MainLayout)
        self.VFPQVFUFButton.setObjectName(u"VFPQVFUFButton")
        font1 = QFont()
        font1.setPointSize(15)
        self.VFPQVFUFButton.setFont(font1)
        self.VFPQVFUFButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.VFPQVFUFButton)

        self.LastVFButton = QPushButton(MainLayout)
        self.LastVFButton.setObjectName(u"LastVFButton")
        self.LastVFButton.setFont(font)
        self.LastVFButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.verticalLayout_2.addWidget(self.LastVFButton)

        self.BottomLeftSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.BottomLeftSpacer)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 3)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.MidLeftLayout = QVBoxLayout()
        self.MidLeftLayout.setObjectName(u"MidLeftLayout")
        self.AlarmStatusLabel = QLabel(MainLayout)
        self.AlarmStatusLabel.setObjectName(u"AlarmStatusLabel")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.AlarmStatusLabel.setFont(font2)
        self.AlarmStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MidLeftLayout.addWidget(self.AlarmStatusLabel)

        self.MidLeftText = QTextBrowser(MainLayout)
        self.MidLeftText.setObjectName(u"MidLeftText")
        self.MidLeftText.setStyleSheet(u"background-color: #ADD8E6;")

        self.MidLeftLayout.addWidget(self.MidLeftText)


        self.horizontalLayout_2.addLayout(self.MidLeftLayout)

        self.MidRightLayout = QVBoxLayout()
        self.MidRightLayout.setObjectName(u"MidRightLayout")
        self.StatusHeader = QLabel(MainLayout)
        self.StatusHeader.setObjectName(u"StatusHeader")
        self.StatusHeader.setFont(font2)
        self.StatusHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MidRightLayout.addWidget(self.StatusHeader)

        self.MidRightText = QTextBrowser(MainLayout)
        self.MidRightText.setObjectName(u"MidRightText")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MidRightText.sizePolicy().hasHeightForWidth())
        self.MidRightText.setSizePolicy(sizePolicy)
        self.MidRightText.setStyleSheet(u"background-color: #ADD8E6;")

        self.MidRightLayout.addWidget(self.MidRightText)


        self.horizontalLayout_2.addLayout(self.MidRightLayout)

        self.ColiumRight = QVBoxLayout()
        self.ColiumRight.setObjectName(u"ColiumRight")
        self.label = QLabel(MainLayout)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: #ADD8E6;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ColiumRight.addWidget(self.label)

        self.TopRightSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.ColiumRight.addItem(self.TopRightSpacer)

        self.CoolDownLabel = QLabel(MainLayout)
        self.CoolDownLabel.setObjectName(u"CoolDownLabel")
        self.CoolDownLabel.setFont(font1)
        self.CoolDownLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ColiumRight.addWidget(self.CoolDownLabel)

        self.FirstSecLayout = QHBoxLayout()
        self.FirstSecLayout.setObjectName(u"FirstSecLayout")
        self.Sec1Num = QLCDNumber(MainLayout)
        self.Sec1Num.setObjectName(u"Sec1Num")

        self.FirstSecLayout.addWidget(self.Sec1Num)

        self.SecOneLabel = QLabel(MainLayout)
        self.SecOneLabel.setObjectName(u"SecOneLabel")

        self.FirstSecLayout.addWidget(self.SecOneLabel)

        self.FirstSecLayout.setStretch(0, 3)
        self.FirstSecLayout.setStretch(1, 1)

        self.ColiumRight.addLayout(self.FirstSecLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CPULabel = QLabel(MainLayout)
        self.CPULabel.setObjectName(u"CPULabel")
        self.CPULabel.setFont(font1)

        self.horizontalLayout_3.addWidget(self.CPULabel)

        self.CPUNum = QLCDNumber(MainLayout)
        self.CPUNum.setObjectName(u"CPUNum")

        self.horizontalLayout_3.addWidget(self.CPUNum)

        self.PercentLabel = QLabel(MainLayout)
        self.PercentLabel.setObjectName(u"PercentLabel")

        self.horizontalLayout_3.addWidget(self.PercentLabel)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)

        self.ColiumRight.addLayout(self.horizontalLayout_3)

        self.ReconnectLabel = QLabel(MainLayout)
        self.ReconnectLabel.setObjectName(u"ReconnectLabel")
        self.ReconnectLabel.setFont(font1)

        self.ColiumRight.addWidget(self.ReconnectLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Num3 = QLCDNumber(MainLayout)
        self.Num3.setObjectName(u"Num3")

        self.horizontalLayout_4.addWidget(self.Num3)

        self.Sec2Label = QLabel(MainLayout)
        self.Sec2Label.setObjectName(u"Sec2Label")

        self.horizontalLayout_4.addWidget(self.Sec2Label)


        self.ColiumRight.addLayout(self.horizontalLayout_4)

        self.Reconnect2Label = QLabel(MainLayout)
        self.Reconnect2Label.setObjectName(u"Reconnect2Label")
        font3 = QFont()
        font3.setPointSize(16)
        self.Reconnect2Label.setFont(font3)

        self.ColiumRight.addWidget(self.Reconnect2Label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Num4 = QLCDNumber(MainLayout)
        self.Num4.setObjectName(u"Num4")

        self.horizontalLayout_5.addWidget(self.Num4)

        self.Sec3Label = QLabel(MainLayout)
        self.Sec3Label.setObjectName(u"Sec3Label")

        self.horizontalLayout_5.addWidget(self.Sec3Label)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)

        self.ColiumRight.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_2.addLayout(self.ColiumRight)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.retranslateUi(MainLayout)

        QMetaObject.connectSlotsByName(MainLayout)
    # setupUi

    def retranslateUi(self, MainLayout):
        MainLayout.setWindowTitle(QCoreApplication.translate("MainLayout", u"Form", None))
        self.GeneralFaultsButton.setText(QCoreApplication.translate("MainLayout", u"General Faults", None))
        self.AlarmButton.setText(QCoreApplication.translate("MainLayout", u"Alarm+Status", None))
        self.VFPQVFUFButton.setText(QCoreApplication.translate("MainLayout", u" VF Faults PQ VF Faults UF", None))
        self.LastVFButton.setText(QCoreApplication.translate("MainLayout", u"Last VF Faults", None))
        self.AlarmStatusLabel.setText(QCoreApplication.translate("MainLayout", u"Alarm Status 1", None))
        self.MidLeftText.setHtml(QCoreApplication.translate("MainLayout", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Overload Warning</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Active C"
                        "ooldown</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\"><br />AC Over Current</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\"><br />IGBT Over Temp</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Cabinet Over Temp</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px"
                        "; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Idc Discharge</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Idc Charge</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Vdc High Voltage</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0p"
                        "x; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Vdc Low Voltage</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">AC-DC Pwr Mismatch</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">AC Phase Sequence</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                        "nt:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">40119 12</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">13</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">14</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">15</span></p></body></html>", None))
        self.StatusHeader.setText(QCoreApplication.translate("MainLayout", u"Status 1", None))
        self.MidRightText.setHtml(QCoreApplication.translate("MainLayout", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Dc Disconnect Closed</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">AC C"
                        "BK Closed</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Fans On </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Fans HIgh Speed</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-size:11pt;\">Ext AC Contractor Closed</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">AC Contractor Closed</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Watchdog Enabled</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; ma"
                        "rgin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Overload Active</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Cooldown Period Active</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Ext Contractor Enabled</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Auto Transfer Enabled</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Softramp Active</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">F-Watt Param Active</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-b"
                        "ottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Reconnect Timer Active </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Grid VF OK</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">UpGrid VF OK</span></p></bod"
                        "y></html>", None))
        self.label.setText(QCoreApplication.translate("MainLayout", u"Abnormal VF active", None))
        self.CoolDownLabel.setText(QCoreApplication.translate("MainLayout", u"OL Cool Down Counter:", None))
        self.SecOneLabel.setText(QCoreApplication.translate("MainLayout", u"SEC", None))
        self.CPULabel.setText(QCoreApplication.translate("MainLayout", u"CPU", None))
        self.PercentLabel.setText(QCoreApplication.translate("MainLayout", u"%", None))
        self.ReconnectLabel.setText(QCoreApplication.translate("MainLayout", u"Reconnect Timer:", None))
        self.Sec2Label.setText(QCoreApplication.translate("MainLayout", u"Sec", None))
        self.Reconnect2Label.setText(QCoreApplication.translate("MainLayout", u"Reconnect Counter:", None))
        self.Sec3Label.setText(QCoreApplication.translate("MainLayout", u"Sec", None))
    # retranslateUi

