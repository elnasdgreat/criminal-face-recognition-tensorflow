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
        MainWindow.resize(640, 480)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(".QWidget {\n"
"    background-color: #c62626\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.appName = QtWidgets.QLabel(self.centralwidget)
        self.appName.setGeometry(QtCore.QRect(30, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.appName.setFont(font)
        self.appName.setStyleSheet(".QLabel {\n"
"    color: #fff\n"
"}")
        self.appName.setIndent(3)
        self.appName.setObjectName("appName")
        self.addRecordBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addRecordBtn.setGeometry(QtCore.QRect(474, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addRecordBtn.setFont(font)
        self.addRecordBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addRecordBtn.setStyleSheet(".QPushButton {\n"
"    border: none;\n"
"    color: #fff;\n"
"    background-color: #e53935;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #c62626;\n"
"}")
        self.addRecordBtn.setFlat(False)
        self.addRecordBtn.setObjectName("addRecordBtn")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(20, 390, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.startBtn.setFont(font)
        self.startBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startBtn.setStyleSheet(".QPushButton {\n"
"    border: none;\n"
"    color: #fff;\n"
"    background-color: #e53935;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #c62626;\n"
"}")
        self.startBtn.setObjectName("startBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 281, 301))
        self.label.setStyleSheet(".QLabel {\n"
"    background-color: #e53935;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.highLabel = QtWidgets.QLabel(self.centralwidget)
        self.highLabel.setGeometry(QtCore.QRect(330, 60, 291, 41))
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
        self.highLabel.setObjectName("highLabel")
        self.highList = QtWidgets.QListWidget(self.centralwidget)
        self.highList.setGeometry(QtCore.QRect(330, 100, 291, 181))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.highList.setFont(font)
        self.highList.setStyleSheet(".QListWidget {\n"
"    border: none;\n"
"    color: #fff;\n"
"    background-color: #e53935;\n"
"}\n"
"")
        self.highList.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.highList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.highList.setProperty("showDropIndicator", True)
        self.highList.setDragEnabled(False)
        self.highList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.highList.setObjectName("highList")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 5, 31))
        self.label_2.setStyleSheet(".QLabel {\n"
"    background-color: #e53935;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lowLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowLabel.setGeometry(QtCore.QRect(330, 290, 291, 31))
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
        self.lowLabel.setObjectName("lowLabel")
        self.lowList = QtWidgets.QListWidget(self.centralwidget)
        self.lowList.setGeometry(QtCore.QRect(330, 330, 291, 131))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lowList.setFont(font)
        self.lowList.setStyleSheet(".QListWidget {\n"
"    border: none;\n"
"    color: #fff;\n"
"    background-color: #e53935;\n"
"}\n"
"")
        self.lowList.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lowList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lowList.setProperty("showDropIndicator", True)
        self.lowList.setDragEnabled(False)
        self.lowList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.lowList.setObjectName("lowList")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.highList.setCurrentRow(-1)
        self.lowList.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smooth Criminal"))
        self.appName.setText(_translate("MainWindow", "S M O O T H   C R I M I N A L"))
        self.addRecordBtn.setText(_translate("MainWindow", "ADD NEW RECORD"))
        self.startBtn.setText(_translate("MainWindow", "S T A R T"))
        self.highLabel.setText(_translate("MainWindow", "H I G H   P R O B A B I L I T Y"))
        self.highList.setSortingEnabled(False)
        self.lowLabel.setText(_translate("MainWindow", "L O W   P R O B A B I L I T Y"))
        self.lowList.setSortingEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    for i in range(1, 31):
        h = QtWidgets.QListWidgetItem("High Probability %i" % i)
        l = QtWidgets.QListWidgetItem("Low Probability %i" % i)
        ui.highList.addItem(h)
        ui.lowList.addItem(l)
    MainWindow.show()
    sys.exit(app.exec_())

