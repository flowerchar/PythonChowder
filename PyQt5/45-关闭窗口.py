import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
# QCoreApplication是在QApplication里创建的
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # self是Example类的一个实例
        qbtn = QPushButton('Quit', self)
        # instance()创建了QCoreApplication的实例
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())