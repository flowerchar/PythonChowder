import sys
# QHBoxLayout是水平上排列小部件，QVBoxLayout是垂直布局
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('花猹')

        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)

        # 创建一个水平框布局，一个拉伸因子，三个按钮
        # 拉伸因子把它们推到窗口右边
        hbox = QHBoxLayout()
        # 这个方法是把水平框的空白部分（除开按钮块）分为7分，bt1前面那部分占1
        hbox.addStretch(1)
        hbox.addWidget(bt1)
        hbox.addWidget(bt2)
        hbox.addWidget(bt3)
        # bt3后面那部分占6
        hbox.addStretch(6)

        # 水平布局放置在垂直布局中，垂直框的拉伸因子把水平框推到窗口底部
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())