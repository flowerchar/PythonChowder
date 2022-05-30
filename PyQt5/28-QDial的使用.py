import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QLabel, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('花猹')

        self.dial = QDial()
        # 这里必须要固定QDial的大小，否则在改变表盘的数值时，表盘大小会发生改变
        self.dial.setFixedSize(100, 100)
        self.dial.setRange(0, 100)
        # 这个setNotchesVisible()，True是显示刻度，False是不显示，默认是不显示
        self.dial.setNotchesVisible(False)
        # 当表盘数值发生改变时，触发valueChanged信号，从而发动槽函数，让QLabel读出数值
        self.dial.valueChanged.connect(self.on_change_func)

        self.label = QLabel('0', self)
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.dial)
        self.h_layout.addWidget(self.label)

        self.setLayout(self.h_layout)

    def on_change_func(self):
        self.label.setText(str(self.dial.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())