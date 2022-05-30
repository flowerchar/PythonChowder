import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton,\
    QVBoxLayout, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # 实例化一个进度条，默认是水平的
        self.progressbar = QProgressBar()
        # 但是可以通过下面这个设置为竖直的
        # self.progressbar.setOrientation(Qt.Vertical)
        # 通过设置最小最大值来规定范围
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        # 也可以直接设置范围
        # self.progressbar.setRange(0,100)

        self.step = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_func)

        self.ss_button = QPushButton('Start', self)
        self.ss_button.clicked.connect(self.start_stop_func)
        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_func)

        self.h_layout = QHBoxLayout()
        self.v_layout= QVBoxLayout()

        self.h_layout.addWidget(self.ss_button)
        self.h_layout.addWidget(self.reset_button)
        self.v_layout.addWidget(self.progressbar)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def start_stop_func(self):
        # 如果什么都还没做
        if self.ss_button.text() == 'Start':
            self.ss_button.setText('Stop')
            self.timer.start(100)
        # 如果文本内容还不是Start，那么说明计时器并没激活
        else:
            self.ss_button.setText('Start')
            self.timer.stop()

    def update_func(self):
        self.step += 1
        self.progressbar.setValue(self.step)

        # 当step的值超过100时，1.按钮重置为Start，2.计时器停止，3.计数停止
        if self.step >= 100:
            self.ss_button.setText('Start')
            self.timer.stop()
            self.step = 0

    def reset_func(self):
        # QProgressBar.reset()是重置进度条
        self.progressbar.reset()
        self.ss_button.setText('Start')
        self.timer.stop()
        self.step = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())