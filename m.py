# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import camera

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
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
        self.btnAddRecord = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddRecord.setGeometry(QtCore.QRect(474, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddRecord.setFont(font)
        self.btnAddRecord.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddRecord.setStyleSheet(".QPushButton {\n"
"    border: 2px solid #ff3b3b;\n"
"    border-radius: 3px;\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #ff3b3b;\n"
"    border: none;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/plus-white-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddRecord.setIcon(icon)
        self.btnAddRecord.setIconSize(QtCore.QSize(10, 10))
        self.btnAddRecord.setFlat(False)
        self.btnAddRecord.setObjectName("btnAddRecord")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.clicked.connect(self.start_camera)
        self.btnStart.setGeometry(QtCore.QRect(20, 390, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.btnStart.setFont(font)
        self.btnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStart.setStyleSheet(".QPushButton {\n"
"    border: 2px solid #ff3b3b;\n"
"    border-radius: 3px;\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #ff3b3b;\n"
"    border: none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/screenshot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStart.setIcon(icon1)
        self.btnStart.setIconSize(QtCore.QSize(24, 24))
        self.btnStart.setObjectName("btnStart")
        self.highLabel = QtWidgets.QLabel(self.centralwidget)
        self.highLabel.setGeometry(QtCore.QRect(347, 60, 291, 41))
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
        self.listHigh.setGeometry(QtCore.QRect(330, 104, 291, 181))
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
        self.lowLabel.setGeometry(QtCore.QRect(347, 290, 291, 31))
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


        # create radio buttons group
        self.vidInputGrp = QtWidgets.QButtonGroup(self.centralwidget)


        
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




        # add radio buttons to group
        self.vidInputGrp.addButton(self.radUsbCam,1)
        self.vidInputGrp.addButton(self.radIpCam,2)
        self.vidInputGrp.addButton(self.radVidFile,3)




        
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
        self.btnBrowseFile.clicked.connect(self.browse_vid_file)
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
        self.labelCaretUp.setGeometry(QtCore.QRect(330, 73, 16, 16))
        self.labelCaretUp.setText("")
        self.labelCaretUp.setPixmap(QtGui.QPixmap("icons/caret-arrow-up.png"))
        self.labelCaretUp.setScaledContents(True)
        self.labelCaretUp.setIndent(0)
        self.labelCaretUp.setObjectName("labelCaretUp")
        self.labelCaretDown = QtWidgets.QLabel(self.centralwidget)
        self.labelCaretDown.setGeometry(QtCore.QRect(330, 298, 16, 16))
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
        self.labelOpenFolder = QtWidgets.QLabel(self.centralwidget)
        self.labelOpenFolder.setGeometry(QtCore.QRect(222, 336, 12, 12))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOpenFolder.sizePolicy().hasHeightForWidth())
        self.labelOpenFolder.setSizePolicy(sizePolicy)
        self.labelOpenFolder.setText("")
        self.labelOpenFolder.setPixmap(QtGui.QPixmap("icons/open-folder.png"))
        self.labelOpenFolder.setScaledContents(True)
        self.labelOpenFolder.setObjectName("labelOpenFolder")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.listHigh.setCurrentRow(-1)
        self.listLow.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smooth Criminal"))
        self.appName.setText(_translate("MainWindow", "S M O O T H   C R I M I N A L"))
        self.btnAddRecord.setText(_translate("MainWindow", "  ADD NEW RECORD"))
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

    def start_camera(self):
        captureMode = self.check_vid_input()        
        
        self.btnStart.setText("  Starting...")
        self.btnStart.setEnabled(False);
        
        # threading
        def callback():
            #camera.main(camera.parse_arguments(['ALL', 'pre-trained/20170512-110547.pb', 'classifier.pkl', '--interval=1', '--minsize=80', self]))
            camera.main('ALL', 'pre-trained/20170512-110547.pb', 'classifier.pkl', 10, 80, captureMode, self)

        t = threading.Thread(target=callback)
        t.start()

        # direct call
        #camera.main(camera.parse_arguments(['ALL', 'pre-trained/20170512-110547.pb', 'classifier.pkl', '--interval=1', '--minsize=80']))

    def browse_vid_file(self):
        filter = "images (*.mp4)"
        file_name = QtWidgets.QFileDialog()
        file_name.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        name = file_name.getOpenFileName(self.centralwidget, "Select Video File", "", filter)
        self.lineVidFile.setText(name[0])  

    def check_vid_input(self):
        choice = self.vidInputGrp.checkedId()

        if(choice == 1):
            captureMode = self.spinBoxUsbCam.value()
        elif(choice == 2):
            captureMode = self.lineIpCam.text()
        elif(choice == 3):
            captureMode = self.lineVidFile.text()

        return captureMode
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

