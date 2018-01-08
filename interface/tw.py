# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TrainWindow(object):
    def setupUi(self, TrainWindow):
        TrainWindow.setObjectName("TrainWindow")
        TrainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(TrainWindow)
        self.centralwidget.setStyleSheet(".QWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(211, 16, 39, 255), stop:1 rgba(234, 56, 77, 255));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(140, 80, 256, 192))
        self.listView.setObjectName("listView")
        TrainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TrainWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainWindow)

    def retranslateUi(self, TrainWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainWindow.setWindowTitle(_translate("TrainWindow", "Train Manager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrainWindow = QtWidgets.QMainWindow()
    ui = Ui_TrainWindow()
    ui.setupUi(TrainWindow)
    TrainWindow.show()
    sys.exit(app.exec_())

