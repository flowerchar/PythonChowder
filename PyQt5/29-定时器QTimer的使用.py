import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel('0', self)
        # 让QLabel居中显示，addStretch(int)也可以达到相同的效果
        self.label.setAlignment(Qt.AlignCenter)

        self.step = 0

        self.timer = QTimer()
        # QTimer.timeout是超时了就发动槽函数
        self.timer.timeout.connect(self.update_func)

        self.ss_button = QPushButton('Start', self)
        # 在最开始时，点击按钮，因为定时器未激活，所以执行if语句，文字变为Start
        # 并且定时器启动，间隔为1秒
        self.ss_button.clicked.connect(self.start_stop_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.ss_button)

        self.setLayout(self.v_layout)

    def start_stop_func(self):
        # 用QTimer.isActive()判断定时器是否处于激活状态
        # 如果没有，则按钮上的文字为Stop
        if not self.timer.isActive():
            self.ss_button.setText('Stop')
            # 定时器激活，且间隔为1秒，如果不再点击按钮，一秒后定时器停止，又发出了timeout信号
            # 发动update_func函数，更新时间
            self.timer.start(100)
        # 如果处于激活状态，文字则变回Start，并通过QTimer的stop()停止计时
        else:
            self.ss_button.setText('Start')
            # 如果再次点击按钮，那计时器关闭
            self.timer.stop()

    def update_func(self):
        self.step += 1
        self.label.setText(str(self.step))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())