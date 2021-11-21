import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, \
    QMainWindow

#
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.pushButton = self.pushButton
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        a = randrange(10, 450)
        qp.setBrush(QBrush(QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256))))
        qp.drawEllipse(100, 100, a, a)
        qp.end()

    def paint(self):
        self.repaint()
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
