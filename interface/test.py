import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(500,500)
        self.setWindowTitle("Test")
        self.home()

    def home(self):
        btn = QtWidgets.QPushButton("Ok", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(100,100)
        btn.move(100,100)
        self.show()
        
    def loadFiles(self):
        filter = "images (*.jpg *.jpeg *.png)"
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        names = file_name.getOpenFileNames(self, "Open files", "", filter)
        print(names)
        

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    GUI.loadFiles()
    sys.exit(app.exec_())


run()
