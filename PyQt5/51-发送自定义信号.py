import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


# Communicate类创建了一个pyatSingnal()属性的信号
class Communicate(QObject):
    # 创建了一个closeApp的信号
    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()
        # self.c.closeApp = pyqtSignal()
        # 因为这里要用到connect，如果只是单单让self.ccloseApp = pyqtSignal()就会出错
        # 因为只有QObject对象才有connect属性
        self.c.closeApp.connect(self.close)
        # 自定义信号连接关闭函数
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        # 鼠标按下则发送c.closeApp信号
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
