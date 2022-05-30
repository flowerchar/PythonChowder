import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Ico(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200,400,200,300)
        self.setWindowTitle('花猹')
        self.setWindowIcon(QIcon(r'C:\Users\DELL\Desktop\格式工厂\3911775.ico'))

        qbtn = QPushButton('退出',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 父界面的宽高为：200,300
        # 按钮的宽高均为50，所以按钮的右下角跟父界面的右下角坐标刚好相等
        qbtn.resize(50,50)
        qbtn.move(150,250)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())