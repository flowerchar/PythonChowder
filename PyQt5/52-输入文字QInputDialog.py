from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        # 弹出一个模态对话框，第一个参数为作用的父类，第二个为对话框标题，第三个为编辑行上面的文字
        # 对话框返回输入内容和一个布尔值
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        # 只有点击OK才会得到text，且获得的布尔值是字符串
        print(text, type(text))
        print(ok, type(text))
        if ok:
            self.le.setText((text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())