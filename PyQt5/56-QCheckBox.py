from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        # cb.toggle()
        # 这个让checkbox的状态是选中的
        cb.stateChanged.connect(self.changeTitle)
        # stateChanged是状态改变则发出信号
        self.setGeometry(300, 300, 250, 150)
        # self.setWindowTitle('QCheckBox')
        self.show()

    # 这个槽函数会默认从信号那获得状态
    def changeTitle(self, state):
        # print(666)
        # 如果是Checked，则执行if里的语句
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())