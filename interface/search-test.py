import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)

model = QtCore.QStringListModel()
model.setStringList(['some', 'words','whales', 'in', 'my', 'dictionary'])

completer = QtWidgets.QCompleter()
completer.setModel(model)

lineedit = QtWidgets.QLineEdit()
lineedit.setCompleter(completer)
lineedit.show()

sys.exit(app.exec_())
