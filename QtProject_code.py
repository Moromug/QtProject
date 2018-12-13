import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QPushButton, QMainWindow


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('QtProject_design.ui', self)
        self.btn1.clicked.connect(self.Algebra)
        self.btn2.clicked.connect(self.Trigonometry)
        self.back_btn.clicked.connect(self.undo)
        self.count_algebra.clicked.connect(self.diskr)
        self.count_trig.clicked.connect(self.triga)
        self.exit_btn.clicked.connect(self.bye)
        self.widget_2.hide()
        self.widget.hide()
        self.images.hide()
        self.back.hide()

    def Algebra(self):
        self.widget_3.hide()
        self.widget_2.show()
        self.back.show()

    def Trigonometry(self):
        self.widget_3.hide()
        self.widget.show()
        self.back.show()

    def undo(self):
        self.widget_2.hide()
        self.widget.hide()
        self.images.hide()
        self.back.hide()
        self.widget_3.show()

    def bye(self):
        sys.exit()

    def diskr(self):
        pass

    def triga(self):
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
