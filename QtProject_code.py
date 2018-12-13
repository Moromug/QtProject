import sys, math
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QPushButton, QMainWindow


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('QtProject_design.ui', self)
        self.setWindowTitle('Твой помощник в матане')
        self.btn1.clicked.connect(self.Algebra)
        self.btn2.clicked.connect(self.Trigonometry)
        self.back_btn.clicked.connect(self.undo)
        self.count_algebra.clicked.connect(self.alg_math)
        self.count_trig.clicked.connect(self.trig_math)
        self.exit_btn.clicked.connect(self.bye)
        self.algs = ["Дискриминант квадратного уравнения", "Сумма арифметической прогрессии", \
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
        self.images.show()
        if self.alg_choose.currentText() == self.algs[0]:  # оно не пашет
            try:
                self.koeffs = [int(self.input_1.text()), int(self.input_2.text()), int(self.input_3.text())]
                self.d = self.koeffs[1] ** 2 - 4 * self.koeffs[0] * self.koeffs[2]
                if self.d < 0:
                    self.img_4.setText('Дискриминант равен {0}. Корней нет.'.format(self.d))
                else:
                    try:
                        self.x1 = (-self.koeffs[1] + self.d ** 0.5) / (2 * self.koeffs[0])
                        self.x2 = (-self.koeffs[1] - self.d ** 0.5) / (2 * self.koeffs[0])
                    except Exception:
                        try:
                            self.img_4.setText('Это линейное уравнение. Единственный корень равен {0}'.format(
                                -self.koeffs[2] / self.koeffs[1]))
                        except Exception:
                            self.img_4.setText('Это даже не уравнение. Я перестал тебя уважать.')
                    else:
                        if self.d == 0:
                            self.img_4.setText('Дискриминант равен 0.\nКорень равен {0}.'.format(self.x1))
                        else:
                            text = 'Дискриминант равен {0}.\nКорни равны {1} и {2}.'.format(self.d, self.x1, self.x2)
                            self.img_4.setText(text)
            except Exception:
                pass
        elif self.alg_choose.currentText() == self.algs[1]:
            self.koeffs = [int(self.input_1.text()), int(self.input_2.text()), int(self.input_3.text())]
            try:
                self.summa = ((self.koeffs[0] + self.koeffs[1])/2)*self.koeffs[2]
                if self.summa == int(self.summa):
                    self.summa = int(self.summa)
                self.img_4.setText(f'Сумма равна {self.summa}.')
            except Exception:
                pass
        else:
            self.koeffs = [int(self.input_1.text()), int(self.input_2.text()), int(self.input_3.text())]
            try:
                self.proizv = (self.koeffs[0]*(1-self.koeffs[1]**self.koeffs[2])/(1-self.koeffs[1]))
                if self.proizv == int(self.proizv):
                    self.proizv = int(self.proizv)
                self.img_4.setText('Сумма равна {0}.'.format(self.proizv))
            except Exception:
                try:
                    self.img_4.setText('Сумма равна {0}.'.format(self.koeffs[0]*self.koeffs[2]))
                except Exception:
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
            self.koeff_1.setText('Первый элемент')
            self.koeff_2.setText('Множитель прогрессии')
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
