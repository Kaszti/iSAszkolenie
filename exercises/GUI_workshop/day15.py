from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
import GUI_workshop.excel as excel

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('excel.ui', self)

        self.setWindowTitle('My Excel')

        self.buttonOpen: QtWidgets.QAction = self.findChild(QtWidgets.QAction, 'actionOpen')
        self.buttonOpen.triggered.connect(self.action_open)

        self.buttonSave: QtWidgets.QAction = self.findChild(QtWidgets.QAction, 'actionSave')
        self.buttonSave.triggered.connect(self.action_save)

        self.buttonExit: QtWidgets.QAction = self.findChild(QtWidgets.QAction, 'actionExit')
        self.buttonExit.triggered.connect(self.action_exit)

        self.infoBar: QtWidgets.QLabel = self.findChild(QtWidgets.QLabel, 'statusBar')

        self.tableWidget: QtWidgets.QTableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.tableWidget.doubleClicked.connect(self.slotDoubleClicked)

        self.show()

    def slotDoubleClicked(self, mi: QtCore.QModelIndex):
        print('double click')
        self.infoBar.setText(f'Cell Row: {mi.row() + 1} Col: {mi.column() + 1}')

    def action_save(self):
        print('save')
        row_count = self.tableWidget.rowCount()
        col_count = self.tableWidget.columnCount()
        data = []
        for row in range(0, row_count):
            cols = []
            for col in range(0, col_count):
                cols.append(self.tableWidget.item(row, col).text())
            data.append(cols)

        excel.dump(self.file_path, data)

    def action_open(self):
        print('open')
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose file', filter='Excel files (*.xlsx)')
        self.file_path = file[0]
        if file[0] != '':
            data = excel.load(self.file_path)
            self.tableWidget.setRowCount(data['rowCount'])
            self.tableWidget.setColumnCount(data['columnCount'])
            for row_index, row in enumerate(data['data']):
                for col_index, col in enumerate(row):
                    self.tableWidget.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(col)))

        self.infoBar.setText(f'Loaded file: {self.file_path}')


    def action_exit(self):
        print('exit')
        exit()

app = QtWidgets.QApplication(sys.argv)
window = App()
app.exec_()