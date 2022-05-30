import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 疑问，这里为什么只是定义了鼠标事件，而没有调用，但是却可以执行
# 而且没有点击移动的鼠标坐标显示的卡顿
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # 显示鼠标的状态
        self.button_label = QLabel('No Button Pressed', self)
        # 相对于QWidget的坐标
        self.xy_label = QLabel('x:0, y:0', self)
        # 相对于显示屏的坐标
        self.global_xy_label = QLabel('global x:0, global y:0', self)

        self.button_label.setAlignment(Qt.AlignCenter)
        self.xy_label.setAlignment(Qt.AlignCenter)
        self.global_xy_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout(self)
        self.v_layout.addWidget(self.button_label)
        self.v_layout.addWidget(self.xy_label)
        self.v_layout.addWidget(self.global_xy_label)
        self.setLayout(self.v_layout)

        self.resize(300, 300)
        # QWidget.setMouseTracking(bool)，为True则让窗口始终追踪鼠标，否则只有点击鼠标才会追踪
        self.setMouseTracking(True)

    def mouseMoveEvent(self, QMouseEvent):
        # 用这个获取相对于QWidget
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        # 注意，这里后面的字母是大写！！！！
        # 这个用于获得相对于显示屏的坐标，即屏幕左上角
        global_x = QMouseEvent.globalX()
        global_y = QMouseEvent.globalY()

        self.xy_label.setText(f'x:{x}, y{y}')
        self.global_xy_label.setText(f'global x:{global_x}, global y:{global_y}')

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Pressed')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Pressed')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Pressed')

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Released')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Double Clicked')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Released')

    def mouseDoubleClickEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Double Clikced')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Double Clicked')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Double Clikced')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

