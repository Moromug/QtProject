import sys, math
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


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
        self.trigs = ["Двойной угол", "Сумма", "Разность"]
        # cleaning start screen
        self.alg_choose.currentTextChanged.connect(self.diskr)
        self.trig_choose.currentTextChanged.connect(self.triga)
        self.widget_2.hide()
        self.widget.hide()
        self.images.hide()
        self.back.hide()
        self.ubrat.hide()

    def Algebra(self):
        # algebra menu
        self.widget_3.hide()
        self.widget_2.show()
        self.back.show()

    def Trigonometry(self):
        #trigonometry menu
        self.widget_3.hide()
        self.widget.show()
        self.back.show()

    def undo(self):
        # how "back" button works
        self.widget_2.hide()
        self.widget.hide()
        self.images.hide()
        self.back.hide()
        self.widget_3.show()

    def bye(self):
        # ow "exit" button works
        sys.exit()

    def triga(self):
        # trigonometry menu cleaning
        self.img_1.setText('')
        self.img_2.setText('')
        self.img_3.setText('')
        self.img_4.setText('')
        self.img_5.setText('')
        self.img_6.setText('')
        self.img_7.setText('')
        if self.trig_choose.currentText() == self.trigs[0]:
            self.ubrat.hide()
        else:
            self.ubrat.show()

    def alg_math(self):
        # algebra menu cleaning
        self.images.show()
        self.img_1.setText('')
        self.img_2.setText('')
        self.img_3.setText('')
        self.img_4.setText('')
        self.img_5.setText('')
        self.img_6.setText('')
        self.img_7.setText('')
        if self.alg_choose.currentText() == self.algs[0]:
            # discriminant, x1 and x2 for a square equation
            try:
                self.koeffs = [float(self.input_1.text()), float(self.input_2.text()), float(self.input_3.text())]
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
        # arifmetic progression sum
        elif self.alg_choose.currentText() == self.algs[1]:
            self.koeffs = [float(self.input_1.text()), float(self.input_2.text()), float(self.input_3.text())]
            try:
                self.summa = ((self.koeffs[0] + self.koeffs[1]) / 2) * self.koeffs[2]
                if self.summa == int(self.summa):
                    self.summa = int(self.summa)
                self.img_4.setText(f'Сумма равна {self.summa}.')
            except Exception:
                pass
        # geometric progression sum
        else:
            self.koeffs = [float(self.input_1.text()), float(self.input_2.text()), float(self.input_3.text())]
            try:
                self.proizv = (self.koeffs[0] * (1 - self.koeffs[1] ** self.koeffs[2]) / (1 - self.koeffs[1]))
                if self.proizv == int(self.proizv):
                    self.proizv = int(self.proizv)
                self.img_4.setText('Сумма равна {0}.'.format(self.proizv))
            except Exception:
                try:
                    self.img_4.setText('Сумма равна {0}.'.format(self.koeffs[0] * self.koeffs[2]))
                except Exception:
                    pass

    def diskr(self):
        # algebra menu cleaning
        self.images.show()
        self.img_1.setText('')
        self.img_2.setText('')
        self.img_3.setText('')
        self.img_4.setText('')
        self.img_5.setText('')
        self.img_6.setText('')
        self.img_7.setText('')
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
        self.images.show()
        if self.trig_choose.currentText() == self.trigs[0]:
            # double ange
            try:
                self.x = float(self.trig_input.text())
            except Exception:
                pass
            else:
                try:
                    self.sin_2x = 2 * math.sin(self.x) * math.cos(self.x)
                    if self.sin_2x == int(self.sin_2x):
                        self.sin_2x = int(self.sin_2x)
                    self.img_1.setText('Синус двойного угла равен {0}.'.format(self.sin_2x))
                except Exception:
                    self.img_1.setText('Такого синуса не существует.')
                try:
                    self.cos_2x = math.cos(self.x) ** 2 - math.sin(self.x) ** 2
                    if self.cos_2x == int(self.cos_2x):
                        self.cos_2x = int(self.cos_2x)
                    self.img_3.setText('Косинус двойного угла равен {0}.'.format(self.cos_2x))
                except Exception:
                    self.img_3.setText('Такого косинуса не существует.')
                try:
                    self.tg_2x = 2 * math.tan(self.x) / (1 - math.tan(self.x) ** 2)
                    if self.tg_2x == int(self.tg_2x):
                        self.tg_2x = int(self.tg_2x)
                    self.img_5.setText('Тангенс двойного угла равен {0}.'.format(self.tg_2x))
                except Exception:
                    self.img_5.setText('Такого тангенса не существует.')
                try:
                    self.ctg_2x = (1 - math.tan(self.x) ** 2) / (2 * math.tan(self.x))
                    if self.ctg_2x == int(self.ctg_2x):
                        self.ctg_2x = int(self.ctg_2x)
                    self.img_7.setText('Котангенс двойного угла равен {0}.'.format(self.ctg_2x))
                except Exception:
                    self.img_7.setText('Такого котангенса не существует.')

        elif self.trig_choose.currentText() == self.trigs[1]:
            # sin, cos, tan and ctan of a sum
            try:
                self.x = float(self.trig_input.text())
                if self.x == int(self.x):
                    self.x = int(self.x)
                self.y = float(self.trig_input_2.text())
                if self.y == int(self.y):
                    self.y = int(self.y)
            except Exception:
                pass
            else:
                try:
                    self.sin_sum = math.sin(self.x) * math.cos(self.y) + math.cos(self.x) * math.sin(self.y)
                    if self.sin_sum == int(self.sin_sum):
                        self.sin_sum = int(self.sin_sum)
                    self.img_1.setText('Синус суммы {0} и {1} равен {2}.'.format(self.x, self.y, self.sin_sum))
                except Exception:
                    self.img_1.setText('Синус суммы {0} и {1} найти невозможно.'.format(self.x, self.y))
                try:
                    self.cos_sum = math.cos(self.x) * math.cos(self.y) - math.sin(self.x) * math.sin(self.y)
                    if self.cos_sum == int(self.cos_sum):
                        self.cos_sum = int(self.cos_sum)
                    self.img_3.setText('Косинус суммы {0} и {1} равен {2}.'.format(self.x, self.y, self.cos_sum))
                except Exception:
                    self.img_3.setText('Косинус суммы {0} и {1} найти невозможно.'.format(self.x, self.y))
                try:
                    self.tg_sum = (math.tan(self.x) + math.tan(self.y)) / (1 - math.tan(self.x) * math.tan(self.y))
                    if self.tg_sum == int(self.tg_sum):
                        self.tg_sum = int(self.tg_sum)
                    self.img_5.setText('Тангенс суммы {0} и {1} равен {2}.'.format(self.x, self.y, self.tg_sum))
                except Exception:
                    self.img_5.setText('Тангенс суммы {0} и {1} найти невозможно.'.format(self.x, self.y))
                try:
                    self.ctg_sum = (1 - math.tan(self.x) * math.tan(self.y)) / (math.tan(self.x) + math.tan(self.y))
                    if self.ctg_sum == int(self.ctg_sum):
                        self.ctg_sum = int(self.ctg_sum)
                    self.img_7.setText('Котангенс суммы {0} и {1} равен {2}.'.format(self.x, self.y, self.ctg_sum))
                except Exception:
                    self.img_7.setText('Котангенс суммы {0} и {1} найти невозможно.'.format(self.x, self.y))
        else:
            # sin, cos, tan and ctan of a difference
            try:
                self.x = float(self.trig_input.text())
                if self.x == int(self.x):
                    self.x = int(self.x)
                self.y = float(self.trig_input_2.text())
                if self.y == int(self.y):
                    self.y = int(self.y)
            except Exception:
                pass
            else:
                try:
                    self.sin_raz = math.sin(self.x) * math.cos(self.y) - math.cos(self.x) * math.sin(self.y)
                    if self.sin_raz == int(self.sin_raz):
                        self.sin_raz = int(self.sin_raz)
                    self.img_1.setText('Синус разности {0} и {1} равен {2}.'.format(self.x, self.y, self.sin_raz))
                except Exception:
                    self.img_1.setText('Синус разности {0} и {1} найти невозможно.'.format(self.x, self.y))
                try:
                    self.cos_raz = math.cos(self.x) * math.cos(self.y) + math.sin(self.x) * math.sin(self.y)
                    if self.cos_raz == int(self.cos_raz):
                        self.cos_raz = int(self.cos_raz)
                    self.img_3.setText('Косинус разности {0} и {1} равен {2}.'.format(self.x, self.y, self.cos_raz))
                except Exception:
                    self.img_3.setText('Косинус разности {0} и {1} найти невозможно.'.format(self.x, self.y))
                try:
                    self.tg_raz = (math.tan(self.x) - math.tan(self.y)) / (1 + math.tan(self.x) * math.tan(self.y))
                    if self.tg_raz == int(self.tg_raz):
                        self.tg_raz = int(self.tg_raz)
                    self.img_5.setText('Тангенс разности {0} и {1} равен {2}.'.format(self.x, self.y, self.tg_raz))
                except Exception:
                    self.img_5.setText('Тангенс разности {0} и {1} найти невозможно.'.format(self.x, self.y))
                try:
                    self.ctg_raz = (1 + math.tan(self.x) * math.tan(self.y)) / (math.tan(self.x) - math.tan(self.y))
                    if self.ctg_raz == int(self.ctg_raz):
                        self.ctg_raz = int(self.ctg_raz)
                    self.img_7.setText('Котангенс разности {0} и {1} равен {2}.'.format(self.x, self.y, self.ctg_raz))
                except Exception:
                    self.img_7.setText('Котангенс разности {0} и {1} найти невозможно.'.format(self.x, self.y))


if __name__ == '__main__':
    # application launch
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
