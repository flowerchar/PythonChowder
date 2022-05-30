import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.test_button = QPushButton('test', self)
        # 按钮是可标记的吗？是则为True，否则False
        self.test_button.setCheckable(True)
        # QPushButton也能设置图标
        self.test_button.setIcon(QIcon(r'C:\Users\DELL\Desktop\pictures\icon\3911775.jpg'))
        # 按钮标记状态发生变化就会发出toggled信号
        self.test_button.toggled.connect(self.button_state_func)

    def button_state_func(self):
        # 判定当前按钮的状态
        print(self.test_button.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())