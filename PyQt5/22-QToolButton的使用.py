import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton
from PyQt5.QtGui import QIcon

# 这个很像QPushButton，有点差别就是该类是按钮，但是不怎么放置文本而是图片
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # QToolButton这个类必须要加一个self参数，否则会出错
        self.test_button = QToolButton(self)
        self.test_button.setCheckable(True)
        self.test_button.setIcon(QIcon(r'C:\Users\DELL\Desktop\pictures\icon\3911775.jpg'))
        self.test_button.toggled.connect(self.button_state_func)
        # self.test_button.isCheckable()

    def button_state_func(self):
        print(self.test_button.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())