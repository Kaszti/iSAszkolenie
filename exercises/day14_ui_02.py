from PyQt5 import QtWidgets, uic
import sys

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('day14_ui.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'pButton')
        self.button.clicked.connect(self.click_button)

        self.show()

    def click_button(self):
        self.textEdit: QtWidgets.QLineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.label: QtWidgets.QLabel = self.findChild(QtWidgets.QLabel, 'label')

        self.label.setText(self.lineEdit.text())



app = QtWidgets.QApplication(sys.argv)
exe = App()
sys.exit(app.exec_())