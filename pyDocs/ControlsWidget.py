# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControlsWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLCDNumber,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1004, 592)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.FirstColumn = QVBoxLayout()
        self.FirstColumn.setObjectName(u"FirstColumn")
        self.kwKvarGrid = QGridLayout()
        self.kwKvarGrid.setObjectName(u"kwKvarGrid")
        self.kwKvarGrid.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.kVarLabel = QLabel(Form)
        self.kVarLabel.setObjectName(u"kVarLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kVarLabel.sizePolicy().hasHeightForWidth())
        self.kVarLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.kVarLabel.setFont(font)
        self.kVarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.kwKvarGrid.addWidget(self.kVarLabel, 1, 0, 1, 1)

        self.kWLabel = QLabel(Form)
        self.kWLabel.setObjectName(u"kWLabel")
        sizePolicy.setHeightForWidth(self.kWLabel.sizePolicy().hasHeightForWidth())
        self.kWLabel.setSizePolicy(sizePolicy)
        self.kWLabel.setFont(font)
        self.kWLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.kwKvarGrid.addWidget(self.kWLabel, 0, 0, 1, 1)

        self.kWNumber = QLCDNumber(Form)
        self.kWNumber.setObjectName(u"kWNumber")
        sizePolicy.setHeightForWidth(self.kWNumber.sizePolicy().hasHeightForWidth())
        self.kWNumber.setSizePolicy(sizePolicy)

        self.kwKvarGrid.addWidget(self.kWNumber, 0, 1, 1, 1)

        self.kVarLabel_2 = QLCDNumber(Form)
        self.kVarLabel_2.setObjectName(u"kVarLabel_2")
        sizePolicy.setHeightForWidth(self.kVarLabel_2.sizePolicy().hasHeightForWidth())
        self.kVarLabel_2.setSizePolicy(sizePolicy)

        self.kwKvarGrid.addWidget(self.kVarLabel_2, 1, 1, 1, 1)


        self.FirstColumn.addLayout(self.kwKvarGrid)

        self.MetersButton = QPushButton(Form)
        self.MetersButton.setObjectName(u"MetersButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MetersButton.sizePolicy().hasHeightForWidth())
        self.MetersButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(18)
        self.MetersButton.setFont(font1)
        self.MetersButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.FirstColumn.addWidget(self.MetersButton)

        self.MainControlsButton = QPushButton(Form)
        self.MainControlsButton.setObjectName(u"MainControlsButton")
        self.MainControlsButton.setFont(font1)
        self.MainControlsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.FirstColumn.addWidget(self.MainControlsButton)

        self.OtherControlsButton = QPushButton(Form)
        self.OtherControlsButton.setObjectName(u"OtherControlsButton")
        self.OtherControlsButton.setFont(font1)
        self.OtherControlsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.FirstColumn.addWidget(self.OtherControlsButton)

        self.AdvFuncButton = QPushButton(Form)
        self.AdvFuncButton.setObjectName(u"AdvFuncButton")
        self.AdvFuncButton.setFont(font)
        self.AdvFuncButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.FirstColumn.addWidget(self.AdvFuncButton)

        self.RemXferButton = QPushButton(Form)
        self.RemXferButton.setObjectName(u"RemXferButton")
        self.RemXferButton.setFont(font1)
        self.RemXferButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.FirstColumn.addWidget(self.RemXferButton)

        self.InitButton = QPushButton(Form)
        self.InitButton.setObjectName(u"InitButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.InitButton.sizePolicy().hasHeightForWidth())
        self.InitButton.setSizePolicy(sizePolicy2)
        self.InitButton.setFont(font1)
        self.InitButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #D9534F;\n"
"    border: 3px outset #B33A3A;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #B33A3A;\n"
"}")

        self.FirstColumn.addWidget(self.InitButton)

        self.FirstColumn.setStretch(0, 1)
        self.FirstColumn.setStretch(1, 1)
        self.FirstColumn.setStretch(2, 2)
        self.FirstColumn.setStretch(3, 2)
        self.FirstColumn.setStretch(4, 2)
        self.FirstColumn.setStretch(5, 2)
        self.FirstColumn.setStretch(6, 2)

        self.horizontalLayout.addLayout(self.FirstColumn)

        self.MiddleColumn = QVBoxLayout()
        self.MiddleColumn.setObjectName(u"MiddleColumn")
        self.UpperLayout = QHBoxLayout()
        self.UpperLayout.setObjectName(u"UpperLayout")
        self.StartButton = QPushButton(Form)
        self.StartButton.setObjectName(u"StartButton")
        font2 = QFont()
        font2.setPointSize(36)
        self.StartButton.setFont(font2)
        self.StartButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #5CB85C;\n"
"    border: 3px outset #3F8F3F;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #3F8F3F;\n"
"}")

        self.UpperLayout.addWidget(self.StartButton)

        self.StopButton = QPushButton(Form)
        self.StopButton.setObjectName(u"StopButton")
        self.StopButton.setFont(font2)
        self.StopButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #D9534F;\n"
"    border: 3px outset #B33A3A;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #B33A3A;\n"
"}")

        self.UpperLayout.addWidget(self.StopButton)

        self.UpperLayout.setStretch(0, 1)
        self.UpperLayout.setStretch(1, 1)

        self.MiddleColumn.addLayout(self.UpperLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ModeLabel = QLabel(Form)
        self.ModeLabel.setObjectName(u"ModeLabel")
        self.ModeLabel.setFont(font1)

        self.horizontalLayout_7.addWidget(self.ModeLabel)

        self.ModeNUmber = QLCDNumber(Form)
        self.ModeNUmber.setObjectName(u"ModeNUmber")

        self.horizontalLayout_7.addWidget(self.ModeNUmber)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.MiddleColumn.addLayout(self.horizontalLayout_7)

        self.BlueGrid = QGridLayout()
        self.BlueGrid.setObjectName(u"BlueGrid")
        self.A2Label = QLabel(Form)
        self.A2Label.setObjectName(u"A2Label")
        self.A2Label.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.A2Label, 1, 2, 1, 1)

        self.A4Label = QLabel(Form)
        self.A4Label.setObjectName(u"A4Label")
        self.A4Label.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.A4Label, 3, 2, 1, 1)

        self.ChLimLabel = QLabel(Form)
        self.ChLimLabel.setObjectName(u"ChLimLabel")
        self.ChLimLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.ChLimLabel, 3, 0, 1, 1)

        self.disLimLabel = QLabel(Form)
        self.disLimLabel.setObjectName(u"disLimLabel")
        self.disLimLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.disLimLabel, 2, 0, 1, 1)

        self.LowLimNum = QLCDNumber(Form)
        self.LowLimNum.setObjectName(u"LowLimNum")
        self.LowLimNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.LowLimNum, 1, 1, 1, 1)

        self.A1Label = QLabel(Form)
        self.A1Label.setObjectName(u"A1Label")
        self.A1Label.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.A1Label, 0, 2, 1, 1)

        self.DisLimNum = QLCDNumber(Form)
        self.DisLimNum.setObjectName(u"DisLimNum")
        self.DisLimNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.DisLimNum, 2, 1, 1, 1)

        self.HiLimLabel = QLabel(Form)
        self.HiLimLabel.setObjectName(u"HiLimLabel")
        self.HiLimLabel.setFont(font)
        self.HiLimLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.HiLimLabel, 0, 0, 1, 1)

        self.HiLimNum = QLCDNumber(Form)
        self.HiLimNum.setObjectName(u"HiLimNum")
        self.HiLimNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.HiLimNum, 0, 1, 1, 1)

        self.ChLimNum = QLCDNumber(Form)
        self.ChLimNum.setObjectName(u"ChLimNum")
        self.ChLimNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.ChLimNum, 3, 1, 1, 1)

        self.LowLimLabel = QLabel(Form)
        self.LowLimLabel.setObjectName(u"LowLimLabel")
        self.LowLimLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.LowLimLabel, 1, 0, 1, 1)

        self.A3Label = QLabel(Form)
        self.A3Label.setObjectName(u"A3Label")
        self.A3Label.setStyleSheet(u"background-color: #ADD8E6;")

        self.BlueGrid.addWidget(self.A3Label, 2, 2, 1, 1)

        self.BlueGrid.setRowStretch(0, 1)
        self.BlueGrid.setRowStretch(1, 1)
        self.BlueGrid.setRowStretch(2, 1)
        self.BlueGrid.setRowStretch(3, 1)
        self.BlueGrid.setColumnStretch(0, 2)
        self.BlueGrid.setColumnStretch(1, 2)
        self.BlueGrid.setColumnStretch(2, 1)

        self.MiddleColumn.addLayout(self.BlueGrid)

        self.WhiteGrid = QGridLayout()
        self.WhiteGrid.setObjectName(u"WhiteGrid")
        self.VAMaxNum = QLCDNumber(Form)
        self.VAMaxNum.setObjectName(u"VAMaxNum")

        self.WhiteGrid.addWidget(self.VAMaxNum, 3, 1, 1, 1)

        self.VArLabel = QLabel(Form)
        self.VArLabel.setObjectName(u"VArLabel")

        self.WhiteGrid.addWidget(self.VArLabel, 4, 0, 1, 1)

        self.ChargeNumber = QLCDNumber(Form)
        self.ChargeNumber.setObjectName(u"ChargeNumber")

        self.WhiteGrid.addWidget(self.ChargeNumber, 2, 1, 1, 1)

        self.kWLabel2 = QLabel(Form)
        self.kWLabel2.setObjectName(u"kWLabel2")

        self.WhiteGrid.addWidget(self.kWLabel2, 2, 2, 1, 1)

        self.kVALabel = QLabel(Form)
        self.kVALabel.setObjectName(u"kVALabel")

        self.WhiteGrid.addWidget(self.kVALabel, 3, 2, 1, 1)

        self.kVArLabel = QLabel(Form)
        self.kVArLabel.setObjectName(u"kVArLabel")

        self.WhiteGrid.addWidget(self.kVArLabel, 4, 2, 1, 1)

        self.VArMaxNum = QLCDNumber(Form)
        self.VArMaxNum.setObjectName(u"VArMaxNum")

        self.WhiteGrid.addWidget(self.VArMaxNum, 4, 1, 1, 1)

        self.VALabel = QLabel(Form)
        self.VALabel.setObjectName(u"VALabel")

        self.WhiteGrid.addWidget(self.VALabel, 3, 0, 1, 1)

        self.ChargeLabel = QLabel(Form)
        self.ChargeLabel.setObjectName(u"ChargeLabel")

        self.WhiteGrid.addWidget(self.ChargeLabel, 2, 0, 1, 1)

        self.DisChgLabel = QLabel(Form)
        self.DisChgLabel.setObjectName(u"DisChgLabel")

        self.WhiteGrid.addWidget(self.DisChgLabel, 1, 0, 1, 1)

        self.kW1Label = QLabel(Form)
        self.kW1Label.setObjectName(u"kW1Label")

        self.WhiteGrid.addWidget(self.kW1Label, 1, 2, 1, 1)

        self.DisChgNum = QLCDNumber(Form)
        self.DisChgNum.setObjectName(u"DisChgNum")

        self.WhiteGrid.addWidget(self.DisChgNum, 1, 1, 1, 1)

        self.WhiteGrid.setRowStretch(0, 1)
        self.WhiteGrid.setRowStretch(1, 1)
        self.WhiteGrid.setRowStretch(2, 1)
        self.WhiteGrid.setRowStretch(3, 1)
        self.WhiteGrid.setRowStretch(4, 1)
        self.WhiteGrid.setColumnStretch(0, 2)
        self.WhiteGrid.setColumnStretch(1, 2)
        self.WhiteGrid.setColumnStretch(2, 1)

        self.MiddleColumn.addLayout(self.WhiteGrid)

        self.BlueGreyButtonLayout = QHBoxLayout()
        self.BlueGreyButtonLayout.setObjectName(u"BlueGreyButtonLayout")
        self.CMD2Button = QPushButton(Form)
        self.CMD2Button.setObjectName(u"CMD2Button")
        font3 = QFont()
        font3.setPointSize(16)
        self.CMD2Button.setFont(font3)
        self.CMD2Button.setStyleSheet(u"QPushButton {\n"
"    background-color: #6CA6CD;\n"
"    border: 3px outset #4A7FA5;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #4A7FA5;\n"
"}")

        self.BlueGreyButtonLayout.addWidget(self.CMD2Button)

        self.MaxButton = QPushButton(Form)
        self.MaxButton.setObjectName(u"MaxButton")
        self.MaxButton.setFont(font3)
        self.MaxButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: 3px outset #D4D4D4;\n"
"    border-radius: 3px;\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px inset #D4D4D4;\n"
"}")

        self.BlueGreyButtonLayout.addWidget(self.MaxButton)

        self.BlueGreyButtonLayout.setStretch(0, 1)
        self.BlueGreyButtonLayout.setStretch(1, 1)

        self.MiddleColumn.addLayout(self.BlueGreyButtonLayout)

        self.MiddleColumn.setStretch(0, 1)
        self.MiddleColumn.setStretch(1, 1)
        self.MiddleColumn.setStretch(2, 2)
        self.MiddleColumn.setStretch(3, 2)
        self.MiddleColumn.setStretch(4, 1)

        self.horizontalLayout.addLayout(self.MiddleColumn)

        self.ThirdColumn = QVBoxLayout()
        self.ThirdColumn.setObjectName(u"ThirdColumn")
        self.UpperGrid = QGridLayout()
        self.UpperGrid.setObjectName(u"UpperGrid")
        self.QSetNum = QLCDNumber(Form)
        self.QSetNum.setObjectName(u"QSetNum")
        self.QSetNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.QSetNum, 1, 1, 1, 1)

        self.UFNum = QLCDNumber(Form)
        self.UFNum.setObjectName(u"UFNum")
        self.UFNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.UFNum, 4, 1, 1, 1)

        self.PSetLabel = QLabel(Form)
        self.PSetLabel.setObjectName(u"PSetLabel")
        self.PSetLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.PSetLabel, 0, 0, 1, 1)

        self.UFVadjLabel = QLabel(Form)
        self.UFVadjLabel.setObjectName(u"UFVadjLabel")
        self.UFVadjLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.UFVadjLabel, 4, 0, 1, 1)

        self.PSetNum = QLCDNumber(Form)
        self.PSetNum.setObjectName(u"PSetNum")
        self.PSetNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.PSetNum, 0, 1, 1, 1)

        self.UFFADLabel = QLabel(Form)
        self.UFFADLabel.setObjectName(u"UFFADLabel")
        self.UFFADLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.UFFADLabel, 5, 0, 1, 1)

        self.VdcNum = QLCDNumber(Form)
        self.VdcNum.setObjectName(u"VdcNum")
        self.VdcNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.VdcNum, 3, 1, 1, 1)

        self.UFFadjNum = QLCDNumber(Form)
        self.UFFadjNum.setObjectName(u"UFFadjNum")
        self.UFFadjNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.UFFadjNum, 5, 1, 1, 1)

        self.RRLabel = QLabel(Form)
        self.RRLabel.setObjectName(u"RRLabel")
        self.RRLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.RRLabel, 2, 0, 1, 1)

        self.QSetLabel = QLabel(Form)
        self.QSetLabel.setObjectName(u"QSetLabel")
        self.QSetLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.QSetLabel, 1, 0, 1, 1)

        self.VdcCmdLabel = QLabel(Form)
        self.VdcCmdLabel.setObjectName(u"VdcCmdLabel")
        self.VdcCmdLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.VdcCmdLabel, 3, 0, 1, 1)

        self.RRNum = QLCDNumber(Form)
        self.RRNum.setObjectName(u"RRNum")
        self.RRNum.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.RRNum, 2, 1, 1, 1)

        self.WMaxLabel = QLabel(Form)
        self.WMaxLabel.setObjectName(u"WMaxLabel")
        self.WMaxLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.WMaxLabel, 0, 2, 1, 1)

        self.VarMaxLabel = QLabel(Form)
        self.VarMaxLabel.setObjectName(u"VarMaxLabel")
        self.VarMaxLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.VarMaxLabel, 1, 2, 1, 1)

        self.WRtgSecLabel = QLabel(Form)
        self.WRtgSecLabel.setObjectName(u"WRtgSecLabel")
        self.WRtgSecLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.WRtgSecLabel, 2, 2, 1, 1)

        self.V1Label = QLabel(Form)
        self.V1Label.setObjectName(u"V1Label")
        self.V1Label.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.V1Label, 3, 2, 1, 1)

        self.V2Label = QLabel(Form)
        self.V2Label.setObjectName(u"V2Label")
        self.V2Label.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.V2Label, 4, 2, 1, 1)

        self.HzLabel = QLabel(Form)
        self.HzLabel.setObjectName(u"HzLabel")
        self.HzLabel.setStyleSheet(u"background-color: #ADD8E6;")

        self.UpperGrid.addWidget(self.HzLabel, 5, 2, 1, 1)

        self.UpperGrid.setRowStretch(0, 1)
        self.UpperGrid.setRowStretch(1, 1)
        self.UpperGrid.setRowStretch(2, 1)
        self.UpperGrid.setRowStretch(3, 1)
        self.UpperGrid.setRowStretch(4, 1)
        self.UpperGrid.setRowStretch(5, 1)
        self.UpperGrid.setColumnStretch(0, 2)
        self.UpperGrid.setColumnStretch(1, 2)
        self.UpperGrid.setColumnStretch(2, 1)

        self.ThirdColumn.addLayout(self.UpperGrid)

        self.MiddleGrid = QGridLayout()
        self.MiddleGrid.setObjectName(u"MiddleGrid")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MiddleGrid.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MiddleGrid.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MiddleGrid.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MiddleGrid.addWidget(self.label_4, 1, 1, 1, 1)


        self.ThirdColumn.addLayout(self.MiddleGrid)

        self.ThirdColumn.setStretch(0, 2)
        self.ThirdColumn.setStretch(1, 2)

        self.horizontalLayout.addLayout(self.ThirdColumn)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.kVarLabel.setText(QCoreApplication.translate("Form", u"kVar", None))
        self.kWLabel.setText(QCoreApplication.translate("Form", u"kW", None))
        self.MetersButton.setText(QCoreApplication.translate("Form", u"Meters", None))
        self.MainControlsButton.setText(QCoreApplication.translate("Form", u"Main Controls", None))
        self.OtherControlsButton.setText(QCoreApplication.translate("Form", u"Other Controls", None))
        self.AdvFuncButton.setText(QCoreApplication.translate("Form", u"Advanced Functions", None))
        self.RemXferButton.setText(QCoreApplication.translate("Form", u"Remote Xfer", None))
        self.InitButton.setText(QCoreApplication.translate("Form", u"Init", None))
        self.StartButton.setText(QCoreApplication.translate("Form", u"Start", None))
        self.StopButton.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.ModeLabel.setText(QCoreApplication.translate("Form", u"Mode:", None))
        self.A2Label.setText(QCoreApplication.translate("Form", u"A", None))
        self.A4Label.setText(QCoreApplication.translate("Form", u"A", None))
        self.ChLimLabel.setText(QCoreApplication.translate("Form", u"Idc_ChLim", None))
        self.disLimLabel.setText(QCoreApplication.translate("Form", u"Idc_DisLim", None))
        self.A1Label.setText(QCoreApplication.translate("Form", u"A", None))
        self.HiLimLabel.setText(QCoreApplication.translate("Form", u"Vdc HI Lim", None))
        self.LowLimLabel.setText(QCoreApplication.translate("Form", u"Vdc Low Lim", None))
        self.A3Label.setText(QCoreApplication.translate("Form", u"A", None))
        self.VArLabel.setText(QCoreApplication.translate("Form", u"VAr Max", None))
        self.kWLabel2.setText(QCoreApplication.translate("Form", u"kW", None))
        self.kVALabel.setText(QCoreApplication.translate("Form", u"kVA", None))
        self.kVArLabel.setText(QCoreApplication.translate("Form", u"kVAr", None))
        self.VALabel.setText(QCoreApplication.translate("Form", u"VA Max", None))
        self.ChargeLabel.setText(QCoreApplication.translate("Form", u"Charge Limit", None))
        self.DisChgLabel.setText(QCoreApplication.translate("Form", u"DisChg Limit", None))
        self.kW1Label.setText(QCoreApplication.translate("Form", u"kW", None))
        self.CMD2Button.setText(QCoreApplication.translate("Form", u"CMD2", None))
        self.MaxButton.setText(QCoreApplication.translate("Form", u"Max", None))
        self.PSetLabel.setText(QCoreApplication.translate("Form", u"P Set", None))
        self.UFVadjLabel.setText(QCoreApplication.translate("Form", u"UF Vadj", None))
        self.UFFADLabel.setText(QCoreApplication.translate("Form", u"UF Fadj", None))
        self.RRLabel.setText(QCoreApplication.translate("Form", u"RR", None))
        self.QSetLabel.setText(QCoreApplication.translate("Form", u"Q Set", None))
        self.VdcCmdLabel.setText(QCoreApplication.translate("Form", u"Vdc Cmd", None))
        self.WMaxLabel.setText(QCoreApplication.translate("Form", u"%WMax", None))
        self.VarMaxLabel.setText(QCoreApplication.translate("Form", u"%VArMax", None))
        self.WRtgSecLabel.setText(QCoreApplication.translate("Form", u"%WRtg/Sec", None))
        self.V1Label.setText(QCoreApplication.translate("Form", u"V", None))
        self.V2Label.setText(QCoreApplication.translate("Form", u"V", None))
        self.HzLabel.setText(QCoreApplication.translate("Form", u"Hz", None))
        self.label.setText(QCoreApplication.translate("Form", u"Buffer Store", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Store Settings", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Watchdog Enable", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Abnormal VF Enable", None))
    # retranslateUi

