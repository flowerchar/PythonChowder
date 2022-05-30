import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.button = QPushButton('information', self)
        self.button.clicked.connect(self.show_messagebox)
        self.resize(200, 100)
        self.show()

    def show_messagebox(self):
        # 这个控件特殊一点，self传在第一个位置
        # 第一个参数是它自己，第二个是消息盒子的标题，第三个是盒子的内容，第四个是选项
        # 每一个选项之间用|分隔开来
        QMessageBox.warning(self, 'Title', 'Content', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        # 还有诸如OK,Yes,No,Close,Cancel,Open,Save,Warming


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())