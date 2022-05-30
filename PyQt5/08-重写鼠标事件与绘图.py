import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
    # distance_from_center = 0
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        # 该方法默认是False，为真则启用鼠标跟踪，否则需要按下鼠标来确定位置
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('花猹')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, event):
        distance_from_center = ((event.y()-250)**2+(event.x()-500)**2)**0.5
        self.label.setText(f'坐标：（x:{event.x()},y:{event.y()}）  距离中心的距离：{distance_from_center}')
        self.pos = event.pos()
        # 以为鼠标位置是实时变动的，所以需要这个来随时更新
        self.update()

    def paintEvent(self, event):
        if self.pos:
            q = QPainter(self)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())