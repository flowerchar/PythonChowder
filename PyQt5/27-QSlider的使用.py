import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel,\
    QVBoxLayout, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # 通过Qt.Hrizontal传入得到一个水平滑动条
        self.slider_1 = QSlider(Qt.Horizontal, self)
        # setRange()设置滑动条的范围
        self.slider_1.setRange(0, 100)
        # 当滑动时，数值发生变化，发动槽函数
        self.slider_1.valueChanged.connect(lambda :self.on_change_func(self.slider_1))

        # 通过Qt.Vertical传入一个垂直滑动条
        self.slider_2 = QSlider(Qt.Vertical, self)
        # 也可以通过setMinimum()和setMaximum()来设置最小最大值
        self.slider_2.setMinimum(0)
        self.slider_2.setMaximum(100)
        # 这里如果只用到了slider_1也会发生改变
        # 因为slider_1的值改变了，会通过槽函数来改变slider_2的值，这时slider_2改变了
        self.slider_2.valueChanged.connect(lambda :self.on_change_func(self.slider_2))

        self.label = QLabel('0', self)
        # setFont()为QLabel设置字体，QFont(字体，字号)
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.slider_2)
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.label)
        self.h_layout.addStretch(1)

        self.v_layout.addWidget(self.slider_1)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def on_change_func(self, slider):
        if slider is self.slider_1:
            self.slider_2.setValue(self.slider_1.value())
        else:
            self.slider_1.setValue(self.slider_2.value())
            self.label.setText(str(self.slider_2.value()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())