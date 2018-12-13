import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QPushButton, QMainWindow


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('QtProject_design.ui', self)
        self.btn1.clicked.connect(self.Algebra)
        self.btn2.clicked.connect(self.Trigonometry)
        self.widget_2.hide()
        self.widget.hide()

    def Algebra(self):
        pass

    def Trigonometry(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
