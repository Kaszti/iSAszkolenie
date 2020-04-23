import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'My app'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(800, 200, 500, 500)

        self.button = QPushButton('Hello', self)
        self.button.move(100, 250)
        self.button.clicked.connect(self.click_button)

        self.textbox = QLineEdit(self)
        self.textbox.move(100, 200)

        self.label = QLabel(self)
        self.label.move(100, 300)
        self.label.setText('Siemka')
        self.label.resize(200, 50)

        self.show()

    def click_button(self):
        print('NIE KLIKAJ MNIE!')
        user_text = self.textbox.text()
        print(user_text)
        self.label.setText(f'Czesc {user_text}')

app = QApplication(sys.argv)
exe = App()
sys.exit(app.exec_())