import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QFont接收·一个字体类型和字号大小
        # 这个为后面的字体设置了QFont字体
        QToolTip.setFont(QFont('SansSerif', 10))

        # QWidget可以使用setToolTip创造富文本
        # 当鼠标停留在窗口内时，会提示
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        # 鼠标放在按钮上时，会提示
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # sizeHint()是一个按钮的默认大小
        btn.resize(btn.sizeHint())
        btn.move(0, 0)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())