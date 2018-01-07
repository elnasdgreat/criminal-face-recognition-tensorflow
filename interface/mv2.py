# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 501)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/screenshot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(".QWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(211, 16, 39, 255), stop:1 rgba(234, 56, 77, 255));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.appName = QtWidgets.QLabel(self.centralwidget)
        self.appName.setGeometry(QtCore.QRect(30, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setUnderline(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.appName.setFont(font)
        self.appName.setStyleSheet(".QLabel {\n"
"    color: #fff\n"
"}")
        self.appName.setIndent(3)
        self.appName.setObjectName("appName")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(20, 390, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.btnStart.setFont(font)
        self.btnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStart.setStyleSheet("QPushButton {\n"
"    border-radius: 3px;\n"
"    color: #fff;\n"
"    background-color: #ff3b3b;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: 2px solid #ff3b3b;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: 2px solid #ff3b3b;\n"
"}")
        self.btnStart.setIcon(icon)
        self.btnStart.setIconSize(QtCore.QSize(24, 24))
        self.btnStart.setObjectName("btnStart")
        self.highLabel = QtWidgets.QLabel(self.centralwidget)
        self.highLabel.setGeometry(QtCore.QRect(347, 65, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.highLabel.setFont(font)
        self.highLabel.setStyleSheet(".QLabel {\n"
"    color: #fff;\n"
"}")
        self.highLabel.setScaledContents(False)
        self.highLabel.setIndent(8)
        self.highLabel.setObjectName("highLabel")
        self.listHigh = QtWidgets.QListWidget(self.centralwidget)
        self.listHigh.setGeometry(QtCore.QRect(330, 108, 291, 181))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listHigh.setFont(font)
        self.listHigh.setStyleSheet(".QListWidget {\n"
"    border: 2px solid #ff3b3b;\n"
"    border-radius: 3px;\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.listHigh.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listHigh.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listHigh.setProperty("showDropIndicator", True)
        self.listHigh.setDragEnabled(False)
        self.listHigh.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listHigh.setObjectName("listHigh")
        self.labelBorder = QtWidgets.QLabel(self.centralwidget)
        self.labelBorder.setGeometry(QtCore.QRect(20, 10, 5, 31))
        self.labelBorder.setStyleSheet(".QLabel {\n"
"    background-color: #fff;\n"
"}")
        self.labelBorder.setText("")
        self.labelBorder.setObjectName("labelBorder")
        self.lowLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowLabel.setEnabled(True)
        self.lowLabel.setGeometry(QtCore.QRect(347, 293, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lowLabel.setFont(font)
        self.lowLabel.setStyleSheet(".QLabel {\n"
"    color: #fff;\n"
"}")
        self.lowLabel.setScaledContents(False)
        self.lowLabel.setIndent(8)
        self.lowLabel.setObjectName("lowLabel")
        self.listLow = QtWidgets.QListWidget(self.centralwidget)
        self.listLow.setGeometry(QtCore.QRect(330, 330, 291, 131))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listLow.setFont(font)
        self.listLow.setStyleSheet(".QListWidget {\n"
"    border: 2px solid #ff3b3b;\n"
"    border-radius: 3px;\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.listLow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listLow.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listLow.setProperty("showDropIndicator", True)
        self.listLow.setDragEnabled(False)
        self.listLow.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listLow.setObjectName("listLow")
        self.labelVidInput = QtWidgets.QLabel(self.centralwidget)
        self.labelVidInput.setGeometry(QtCore.QRect(47, 60, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelVidInput.setFont(font)
        self.labelVidInput.setStyleSheet(".QLabel {\n"
"    color: #fff;\n"
"}")
        self.labelVidInput.setScaledContents(False)
        self.labelVidInput.setObjectName("labelVidInput")
        self.radUsbCam = QtWidgets.QRadioButton(self.centralwidget)
        self.radUsbCam.setGeometry(QtCore.QRect(20, 110, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radUsbCam.setFont(font)
        self.radUsbCam.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radUsbCam.setStyleSheet("QRadioButton {\n"
"    color: #fff;\n"
"}\n"
"")
        self.radUsbCam.setIconSize(QtCore.QSize(16, 16))
        self.radUsbCam.setChecked(True)
        self.radUsbCam.setObjectName("radUsbCam")
        self.radIpCam = QtWidgets.QRadioButton(self.centralwidget)
        self.radIpCam.setGeometry(QtCore.QRect(20, 190, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radIpCam.setFont(font)
        self.radIpCam.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radIpCam.setStyleSheet("QRadioButton {\n"
"    color: #fff;\n"
"}\n"
"")
        self.radIpCam.setObjectName("radIpCam")
        self.radVidFile = QtWidgets.QRadioButton(self.centralwidget)
        self.radVidFile.setGeometry(QtCore.QRect(20, 270, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radVidFile.setFont(font)
        self.radVidFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radVidFile.setStyleSheet("QRadioButton {\n"
"    color: #fff;\n"
"}\n"
"")
        self.radVidFile.setObjectName("radVidFile")
        self.spinBoxUsbCam = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxUsbCam.setEnabled(True)
        self.spinBoxUsbCam.setGeometry(QtCore.QRect(20, 140, 281, 31))
        self.spinBoxUsbCam.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBoxUsbCam.setStyleSheet(".QSpinBox {\n"
"    color: #fff;\n"
"    border: 2px solid #ff3b3b;\n"
"    border-radius: 2px;\n"
"    background-color: transparent;\n"
"}")
        self.spinBoxUsbCam.setPrefix("")
        self.spinBoxUsbCam.setObjectName("spinBoxUsbCam")
        self.lineIpCam = QtWidgets.QLineEdit(self.centralwidget)
        self.lineIpCam.setGeometry(QtCore.QRect(20, 220, 281, 31))
        self.lineIpCam.setStyleSheet(".QLineEdit {\n"
"    color: #fff;\n"
"    border: 2px solid #ff3b3b;\n"
"    border-radius: 2px;\n"
"    background-color: transparent;\n"
"}")
        self.lineIpCam.setMaxLength(32767)
        self.lineIpCam.setObjectName("lineIpCam")
        self.lineVidFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineVidFile.setGeometry(QtCore.QRect(20, 300, 281, 31))
        self.lineVidFile.setStyleSheet(".QLineEdit {\n"
"    color: #fff;\n"
"    border: 2px solid #ff3b3b;\n"
"    border-radius: 2px;\n"
"    background-color: transparent;\n"
"}")
        self.lineVidFile.setObjectName("lineVidFile")
        self.btnBrowseFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowseFile.setGeometry(QtCore.QRect(240, 330, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setUnderline(True)
        self.btnBrowseFile.setFont(font)
        self.btnBrowseFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBrowseFile.setStyleSheet(".QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    color: #820707;\n"
"}\n"
"")
        self.btnBrowseFile.setObjectName("btnBrowseFile")
        self.labelCaretUp = QtWidgets.QLabel(self.centralwidget)
        self.labelCaretUp.setGeometry(QtCore.QRect(330, 78, 16, 16))
        self.labelCaretUp.setText("")
        self.labelCaretUp.setPixmap(QtGui.QPixmap("icons/caret-arrow-up.png"))
        self.labelCaretUp.setScaledContents(True)
        self.labelCaretUp.setIndent(0)
        self.labelCaretUp.setObjectName("labelCaretUp")
        self.labelCaretDown = QtWidgets.QLabel(self.centralwidget)
        self.labelCaretDown.setGeometry(QtCore.QRect(330, 301, 16, 16))
        self.labelCaretDown.setText("")
        self.labelCaretDown.setPixmap(QtGui.QPixmap("icons/caret-down.png"))
        self.labelCaretDown.setScaledContents(True)
        self.labelCaretDown.setIndent(0)
        self.labelCaretDown.setObjectName("labelCaretDown")
        self.labelCamIco = QtWidgets.QLabel(self.centralwidget)
        self.labelCamIco.setGeometry(QtCore.QRect(20, 73, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCamIco.setFont(font)
        self.labelCamIco.setStyleSheet(".QLabel {\n"
"    color: #fff;\n"
"}")
        self.labelCamIco.setText("")
        self.labelCamIco.setPixmap(QtGui.QPixmap("icons/photo-camera.png"))
        self.labelCamIco.setScaledContents(True)
        self.labelCamIco.setObjectName("labelCamIco")
        self.lblOpenFolder = QtWidgets.QLabel(self.centralwidget)
        self.lblOpenFolder.setGeometry(QtCore.QRect(222, 336, 12, 12))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOpenFolder.sizePolicy().hasHeightForWidth())
        self.lblOpenFolder.setSizePolicy(sizePolicy)
        self.lblOpenFolder.setText("")
        self.lblOpenFolder.setPixmap(QtGui.QPixmap("icons/open-folder.png"))
        self.lblOpenFolder.setScaledContents(True)
        self.lblOpenFolder.setObjectName("lblOpenFolder")
        self.lblRunning = QtWidgets.QLabel(self.centralwidget)
        self.lblRunning.setGeometry(QtCore.QRect(330, 12, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblRunning.setFont(font)
        self.lblRunning.setStyleSheet("QLabel {\n"
"    color: #ffa2a4;\n"
"}")
        self.lblRunning.setIndent(10)
        self.lblRunning.setObjectName("lblRunning")
        self.lblTimeStarted = QtWidgets.QLabel(self.centralwidget)
        self.lblTimeStarted.setGeometry(QtCore.QRect(330, 27, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblTimeStarted.setFont(font)
        self.lblTimeStarted.setStyleSheet("QLabel {\n"
"    color: #ffa2a4;\n"
"}")
        self.lblTimeStarted.setIndent(10)
        self.lblTimeStarted.setObjectName("lblTimeStarted")
        self.lblFPS = QtWidgets.QLabel(self.centralwidget)
        self.lblFPS.setGeometry(QtCore.QRect(330, 42, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblFPS.setFont(font)
        self.lblFPS.setStyleSheet("QLabel {\n"
"    color: #ffa2a4;\n"
"}")
        self.lblFPS.setIndent(10)
        self.lblFPS.setObjectName("lblFPS")
        self.lblRunVal = QtWidgets.QLabel(self.centralwidget)
        self.lblRunVal.setGeometry(QtCore.QRect(450, 12, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblRunVal.setFont(font)
        self.lblRunVal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblRunVal.setStyleSheet("QLabel {\n"
"    color: #fff;\n"
"}")
        self.lblRunVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblRunVal.setIndent(10)
        self.lblRunVal.setObjectName("lblRunVal")
        self.lblTimeVal = QtWidgets.QLabel(self.centralwidget)
        self.lblTimeVal.setGeometry(QtCore.QRect(450, 27, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTimeVal.setFont(font)
        self.lblTimeVal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTimeVal.setStyleSheet("QLabel {\n"
"    color: #fff;\n"
"}")
        self.lblTimeVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTimeVal.setIndent(10)
        self.lblTimeVal.setObjectName("lblTimeVal")
        self.lblFPSVal = QtWidgets.QLabel(self.centralwidget)
        self.lblFPSVal.setGeometry(QtCore.QRect(450, 42, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblFPSVal.setFont(font)
        self.lblFPSVal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblFPSVal.setStyleSheet("QLabel {\n"
"    color: #fff;\n"
"}")
        self.lblFPSVal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblFPSVal.setIndent(10)
        self.lblFPSVal.setObjectName("lblFPSVal")
        self.lblBg = QtWidgets.QLabel(self.centralwidget)
        self.lblBg.setGeometry(QtCore.QRect(330, 11, 290, 54))
        self.lblBg.setStyleSheet("QLabel {\n"
"    border-radius: 3px;\n"
"    border: 2px solid #ff3b3b;\n"
"}")
        self.lblBg.setText("")
        self.lblBg.setObjectName("lblBg")
        self.lblSettings = QtWidgets.QLabel(self.centralwidget)
        self.lblSettings.setGeometry(QtCore.QRect(559, 484, 12, 12))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSettings.sizePolicy().hasHeightForWidth())
        self.lblSettings.setSizePolicy(sizePolicy)
        self.lblSettings.setText("")
        self.lblSettings.setPixmap(QtGui.QPixmap("icons/settings.png"))
        self.lblSettings.setScaledContents(True)
        self.lblSettings.setObjectName("lblSettings")
        self.btnSettings = QtWidgets.QPushButton(self.centralwidget)
        self.btnSettings.setGeometry(QtCore.QRect(568, 478, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setUnderline(True)
        self.btnSettings.setFont(font)
        self.btnSettings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSettings.setStyleSheet(".QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    color: #820707;\n"
"}\n"
"")
        self.btnSettings.setFlat(False)
        self.btnSettings.setObjectName("btnSettings")
        self.lblBg2 = QtWidgets.QLabel(self.centralwidget)
        self.lblBg2.setGeometry(QtCore.QRect(0, 479, 641, 22))
        self.lblBg2.setStyleSheet("QLabel {\n"
"    background-color: #ff3b3b;\n"
"}")
        self.lblBg2.setText("")
        self.lblBg2.setObjectName("lblBg2")
        self.lblCamNo = QtWidgets.QLabel(self.centralwidget)
        self.lblCamNo.setGeometry(QtCore.QRect(21, 484, 47, 14))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lblCamNo.setFont(font)
        self.lblCamNo.setStyleSheet("QLabel {\n"
"    color: #820707;\n"
"}")
        self.lblCamNo.setObjectName("lblCamNo")
        self.lblCamNoVal = QtWidgets.QLabel(self.centralwidget)
        self.lblCamNoVal.setGeometry(QtCore.QRect(70, 482, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblCamNoVal.setFont(font)
        self.lblCamNoVal.setStyleSheet("QLabel {\n"
"    color: #fff;\n"
"}")
        self.lblCamNoVal.setObjectName("lblCamNoVal")
        self.lblStationId = QtWidgets.QLabel(self.centralwidget)
        self.lblStationId.setGeometry(QtCore.QRect(110, 484, 71, 14))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lblStationId.setFont(font)
        self.lblStationId.setStyleSheet("QLabel {\n"
"    color: #820707;\n"
"}")
        self.lblStationId.setObjectName("lblStationId")
        self.lblStationIdVal = QtWidgets.QLabel(self.centralwidget)
        self.lblStationIdVal.setGeometry(QtCore.QRect(177, 482, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblStationIdVal.setFont(font)
        self.lblStationIdVal.setStyleSheet("QLabel {\n"
"    color: #fff;\n"
"}")
        self.lblStationIdVal.setObjectName("lblStationIdVal")
        self.lblStationIdVal_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblStationIdVal_2.setGeometry(QtCore.QRect(307, 482, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lblStationIdVal_2.setFont(font)
        self.lblStationIdVal_2.setStyleSheet("QLabel {\n"
"    color: #fff;\n"
"}")
        self.lblStationIdVal_2.setObjectName("lblStationIdVal_2")
        self.lblStationId_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblStationId_2.setGeometry(QtCore.QRect(254, 484, 71, 14))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lblStationId_2.setFont(font)
        self.lblStationId_2.setStyleSheet("QLabel {\n"
"    color: #820707;\n"
"}")
        self.lblStationId_2.setObjectName("lblStationId_2")
        self.lblBg2.raise_()
        self.lblBg.raise_()
        self.appName.raise_()
        self.btnStart.raise_()
        self.highLabel.raise_()
        self.listHigh.raise_()
        self.labelBorder.raise_()
        self.lowLabel.raise_()
        self.listLow.raise_()
        self.labelVidInput.raise_()
        self.radUsbCam.raise_()
        self.radIpCam.raise_()
        self.radVidFile.raise_()
        self.spinBoxUsbCam.raise_()
        self.lineIpCam.raise_()
        self.lineVidFile.raise_()
        self.btnBrowseFile.raise_()
        self.labelCaretUp.raise_()
        self.labelCaretDown.raise_()
        self.labelCamIco.raise_()
        self.lblOpenFolder.raise_()
        self.lblRunning.raise_()
        self.lblTimeStarted.raise_()
        self.lblFPS.raise_()
        self.lblRunVal.raise_()
        self.lblTimeVal.raise_()
        self.lblFPSVal.raise_()
        self.lblSettings.raise_()
        self.btnSettings.raise_()
        self.lblCamNo.raise_()
        self.lblCamNoVal.raise_()
        self.lblStationId.raise_()
        self.lblStationIdVal.raise_()
        self.lblStationIdVal_2.raise_()
        self.lblStationId_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.listHigh.setCurrentRow(-1)
        self.listLow.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smooth Criminal"))
        self.appName.setText(_translate("MainWindow", "S M O O T H   C R I M I N A L"))
        self.btnStart.setText(_translate("MainWindow", "  S T A R T"))
        self.highLabel.setText(_translate("MainWindow", "H I G H   P R O B A B I L I T Y"))
        self.listHigh.setSortingEnabled(False)
        self.lowLabel.setText(_translate("MainWindow", "L O W   P R O B A B I L I T Y"))
        self.listLow.setSortingEnabled(False)
        self.labelVidInput.setText(_translate("MainWindow", "V I D E O   I N P U T"))
        self.radUsbCam.setText(_translate("MainWindow", "USB CAM"))
        self.radIpCam.setText(_translate("MainWindow", "IP CAM"))
        self.radVidFile.setText(_translate("MainWindow", "VIDEO FILE"))
        self.spinBoxUsbCam.setToolTip(_translate("MainWindow", "<html><head/><body><p>Change this value if you have more than 1 camera connected via USB. 0 is the default value.</p></body></html>"))
        self.spinBoxUsbCam.setSuffix(_translate("MainWindow", " (0 default)"))
        self.lineIpCam.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter this to the link of the IP Camera you want to use.</p></body></html>"))
        self.lineIpCam.setText(_translate("MainWindow", "http://"))
        self.lineVidFile.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter the path of the video file you want to use. Click the \'browse file\' to locate the video.</p></body></html>"))
        self.lineVidFile.setText(_translate("MainWindow", "C:/"))
        self.btnBrowseFile.setText(_translate("MainWindow", "BROWSE FILE"))
        self.lblRunning.setText(_translate("MainWindow", "Running:"))
        self.lblTimeStarted.setText(_translate("MainWindow", "Time Started:"))
        self.lblFPS.setText(_translate("MainWindow", "Frames per Second:"))
        self.lblRunVal.setText(_translate("MainWindow", "NO"))
        self.lblTimeVal.setText(_translate("MainWindow", "-----"))
        self.lblFPSVal.setText(_translate("MainWindow", "-----"))
        self.btnSettings.setText(_translate("MainWindow", "SETTINGS"))
        self.lblCamNo.setText(_translate("MainWindow", "CAM NO:"))
        self.lblCamNoVal.setText(_translate("MainWindow", "000"))
        self.lblStationId.setText(_translate("MainWindow", "STATION ID:"))
        self.lblStationIdVal.setText(_translate("MainWindow", "000000000"))
        self.lblStationIdVal_2.setText(_translate("MainWindow", "disabled"))
        self.lblStationId_2.setText(_translate("MainWindow", "LOGGING:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

