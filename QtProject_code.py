import sys, math
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
        self.algs = ['Дискриминант квадратного уравнения', "Сумма арифметической прогрессии", \
                     "Сумма геометрической прогрессии"]
        self.trigs = ['Двойной угол', "Сумма", "Разность"]
        self.alg_choose.currentTextChanged.connect(self.diskr)
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

    def alg_math(self):
        if self.alg_choose.currentText() == self.algs[0]:
            pass
        elif self.alg_choose.currentText() == self.algs[1]:
            pass
        else:
            pass

    def diskr(self):
        if self.alg_choose.currentText() == self.algs[0]:
            self.koeff_1.setText('Коэффициент a')
            self.koeff_2.setText('Коэффициент b')
            self.koeff_3.setText('Свободный коэффициент c')
        elif self.alg_choose.currentText() == self.algs[1]:
            self.koeff_1.setText('Первый элемент')
            self.koeff_2.setText('Нужный элемент')
            self.koeff_3.setText('Количество элементов (n)')
        else:
            self.koeff_1.setText('Первыый элемент')
            self.koeff_1.setText('Множитель прогрессии')
            self.koeff_3.setText('Количество элементов (n)')

    def trig_math(self):
        if self.trig_choose.currentText() == self.trigs[0]:
            pass
        elif self.trig_choose.currentText() == self.trigs[1]:
            pass
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
